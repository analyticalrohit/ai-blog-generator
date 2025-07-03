from textwrap import dedent

from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools

from ai_blog_generator.model import Model
from ai_blog_generator.response_model import ScrapedArticle, SearchResults


class BlogAgents:
    """Agents for blog post generation workflow"""

    def __init__(self, llm: Model):
        """Initialize the agents for blog post generation workflow"""
        self.llm = llm.get()
        self.searcher_agent = self._create_searcher_agent()
        self.article_scraper_agent = self._create_article_scraper_agent()
        self.writer_agent = self._create_writer_agent()

    # Search Agent: Handles intelligent web searching and source gathering
    def _create_searcher_agent(self) -> Agent:
        """Create the search agent for finding relevant articles"""
        return Agent(
            model=self.llm,
            tools=[DuckDuckGoTools()],
            description=dedent("""\
         You are BlogResearch-X, an elite research assistant specializing in discovering
         high-quality sources for compelling blog content. Your expertise includes:

         - Finding authoritative and trending sources
         - Evaluating content credibility and relevance
         - Identifying diverse perspectives and expert opinions
         - Discovering unique angles and insights
         - Ensuring comprehensive topic coverage\
         """),
            instructions=dedent("""\
         1. Search Strategy 🔍
            - Find 10-15 relevant sources and select the 5-7 best ones
            - Prioritize recent, authoritative content
            - Look for unique angles and expert insights
         2. Source Evaluation 📊
            - Verify source credibility and expertise
            - Check publication dates for timeliness
            - Assess content depth and uniqueness
         3. Diversity of Perspectives 🌐
            - Include different viewpoints
            - Gather both mainstream and expert opinions
            - Find supporting data and statistics\
         """),
            response_model=SearchResults,
        )

    # Content Scraper: Extracts and processes article content
    def _create_article_scraper_agent(self) -> Agent:
        """Create the article scraper agent for extracting content from articles"""
        return Agent(
            model=self.llm,
            tools=[Newspaper4kTools()],
            description=dedent("""\
         You are ContentBot-X, a specialist in extracting and processing digital content
         for blog creation. Your expertise includes:

         - Efficient content extraction
         - Smart formatting and structuring
         - Key information identification
         - Quote and statistic preservation
         - Maintaining source attribution\
         """),
            instructions=dedent("""\
         1. Content Extraction 📑
            - Extract content from the article
            - Preserve important quotes and statistics
            - Maintain proper attribution
            - Handle paywalls gracefully
         2. Content Processing 🔄
            - Format text in clean markdown
            - Preserve key information
            - Structure content logically
         3. Quality Control ✅
            - Verify content relevance
            - Ensure accurate extraction
            - Maintain readability\
         """),
            response_model=ScrapedArticle,
        )

    # Content Writer Agent: Crafts engaging blog posts from research
    def _create_writer_agent(self) -> Agent:
        """Create the content writer agent for generating blog posts"""
        return Agent(
            model=self.llm,
            description=dedent("""\
         You are BlogMaster-X, an elite content creator combining journalistic excellence
         with digital marketing expertise. Your strengths include:

         - Crafting viral-worthy headlines
         - Writing engaging introductions
         - Structuring content for digital consumption
         - Incorporating research seamlessly
         - Optimizing for SEO while maintaining quality
         - Creating shareable conclusions\
         """),
            instructions=dedent("""\
         1. Content Strategy 📝
            - Craft attention-grabbing headlines
            - Write compelling introductions
            - Structure content for engagement
            - Include relevant subheadings
            - 800-1200 words per post
         2. Writing Excellence ✍️
            - Balance expertise with accessibility
            - Use clear, engaging language
            - Include relevant examples
            - Incorporate statistics naturally
         3. Source Integration 🔍
            - Cite sources properly
            - Include expert quotes
            - Maintain factual accuracy
         4. Digital Optimization 💻
            - Structure for scanability
            - Include shareable takeaways
            - Optimize for SEO
            - Add engaging subheadings\
         """),
            expected_output=dedent("""\
         # {Viral-Worthy Headline}

         ## Introduction
         {Engaging hook and context}

         ## {Compelling Section 1}
         {Key insights and analysis}
         {Expert quotes and statistics}

         ## {Engaging Section 2}
         {Deeper exploration}
         {Real-world examples}

         ## {Practical Section 3}
         {Actionable insights}
         {Expert recommendations}

         ## Key Takeaways
         - {Shareable insight 1}
         - {Practical takeaway 2}
         - {Notable finding 3}

         ## Sources
         {Properly attributed sources with links}\
         """),
            markdown=True,
        )
