import json
from textwrap import dedent
from typing import Dict, Iterator, Optional

from agno.utils.log import logger
from agno.workflow import RunEvent, RunResponse, Workflow

from ai_blog_generator.response_model import ScrapedArticle, SearchResults


class BlogPostGenerator(Workflow):
    """Advanced workflow for generating professional blog posts with proper research and citations."""

    description: str = dedent("""\
    An intelligent blog post generator that creates engaging, well-researched content.
    This workflow orchestrates multiple AI agents to research, analyze, and craft
    compelling blog posts that combine journalistic rigor with engaging storytelling.
    The system excels at creating content that is both informative and optimized for
    digital consumption.
    """)

    def __init__(self, blog_agents, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.searcher = blog_agents.searcher_agent
        self.article_scraper = blog_agents.article_scraper_agent
        self.writer = blog_agents.writer_agent

    def get_search_results(self, topic: str, num_attempts: int = 3) -> Optional[SearchResults]:
        # Use the searcher to find the latest articles
        for attempt in range(num_attempts):
            try:
                searcher_response: RunResponse = self.searcher.run(topic)
                if (
                    searcher_response is not None
                    and searcher_response.content is not None
                    and isinstance(searcher_response.content, SearchResults)
                ):
                    article_count = len(searcher_response.content.articles)
                    logger.info(f"Found {article_count} articles on attempt {attempt + 1}")
                    return searcher_response.content
                else:
                    logger.warning(f"Attempt {attempt + 1}/{num_attempts} failed: Invalid response type")
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{num_attempts} failed: {str(e)}")

        logger.error(f"Failed to get search results after {num_attempts} attempts")
        return None

    def scrape_articles(self, topic: str, search_results: SearchResults) -> Dict[str, ScrapedArticle]:
        scraped_articles: Dict[str, ScrapedArticle] = {}
        for article in search_results.articles:
            if article.url in scraped_articles:
                logger.info(f"Found scraped article in cache: {article.url}")
                continue

            article_scraper_response: RunResponse = self.article_scraper.run(article.url)
            if (
                article_scraper_response is not None
                and article_scraper_response.content is not None
                and isinstance(article_scraper_response.content, ScrapedArticle)
            ):
                scraped_articles[article_scraper_response.content.url] = article_scraper_response.content
                logger.info(f"Scraped article: {article_scraper_response.content.url}")
        return scraped_articles

    def run(
        self,
        topic: str,
    ) -> Iterator[RunResponse]:
        """Run the blog post generation workflow."""
        logger.info(f"Generating a blog post on: {topic}")

        # Search the web for articles on the topic
        search_results: Optional[SearchResults] = self.get_search_results(topic)
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Scrape the search results
        scraped_articles: Dict[str, ScrapedArticle] = self.scrape_articles(topic, search_results)

        # Prepare the input for the writer
        writer_input = {
            "topic": topic,
            "articles": [v.model_dump() for v in scraped_articles.values()],
        }

        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
