<p align="center">
  <a href="https://www.linkedin.com/in/analyticalrohit" style="text-decoration:none;">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://awesomeneuron.substack.com/" style="text-decoration:none;">
    <img src="https://img.shields.io/badge/Substack-%23006f5c.svg?style=for-the-badge&logo=substack&logoColor=FF6719" alt="Substack">
  </a>
   <a href="https://x.com/_rohit_tiwari_" style="text-decoration:none;">
    <img src="https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white" alt="X">
  </a>
     <a href="https://www.youtube.com/@awesomeneuron?sub_confirmation=1" style="text-decoration:none;">
    <img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" alt="Youtube">
  </a>
     <a href="https://topmate.io/analyticalrohit" style="text-decoration:none;">
    <img src="https://raw.githubusercontent.com/analyticalrohit/analyticalrohit/refs/heads/main/assets/topmate_logo.png" alt="Topmate">
  </a>
</p>

# AI Blog Generator

AI Blog Generator is an advanced, multi-agent system for generating professional, well-researched blog posts using the [Agno framework](https://github.com/agno-agi/agno). It supports leading LLM providers including **OpenAI**, **Gemini**, **Claude**, and **Grok**.

<p align="center">
  <a href="https://awesomeneuron.substack.com/">
    <img src="./assets/multi_agent_blog_generator.gif">
  </a>
</p>
<p align="center">
  <a href="https://awesomeneuron.substack.com/">
    <img src="./assets/multi_agent_blog_generator_usage.gif" />
  </a>
</p>
<p align="center">
  🚀 Launch App &rarr; <a href="https://huggingface.co/spaces/analyticalrohit/ai-blog-generator">https://huggingface.co/spaces/analyticalrohit/ai-blog-generator</a>
</p>

## Features

- **Multi-Agent Workflow:** Orchestrates research, content extraction, and writing using specialized agents.
- **Provider Flexibility:** Easily switch between OpenAI, Gemini, Claude, and Grok models.
- **Research Driven Content:** Finds, evaluates, and cites authoritative sources.
- **Content Scraping:** Extracts and summarizes article content for reference.
- **Gradio UI:** Simple web interface for generating and viewing blog posts.

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/analyticalrohit/ai-blog-generator.git
cd ai-blog-generator
```

### 2. Install Dependencies

```sh
uv venv --python 3.12

uv sync
```

### 3. Run the App

```sh
uv run app.py
```

The Gradio interface will launch in your browser.

## Usage

1. Select your preferred LLM provider and model.
2. Enter your API key.
3. Choose an example topic or enter your own.
4. Click Generate Blog to create a post.

[![Watch on Youtube](./assets/thumbnail_youtube.png)](https://www.youtube.com/watch?v=smzPuZZMBvs)

## Example Prompts

- How Generative AI is Changing the Way We Work
- The Science Behind Why Pizza Tastes Better at 2 AM
- How Rubber Ducks Revolutionized Software Development

## Project Structure

```
.
├── app.py                        # Gradio web app
├── src/
│   └── ai_blog_generator/
│       ├── agents.py             # Agent definitions
│       ├── generator.py          # Blog post generation workflow
│       ├── model.py              # LLM model (OpenAI, Gemini, Claude, Grok)
│       ├── response_model.py     # Pydantic models for responses
│       └── utils.py              # Utilities
├── pyproject.toml
├── README.md
└── ...
```
## Newsletter
<div style="text-align: left;">
📌 Join 2000+ ML enthusiasts and professionals from 100 countries.<br>
✅ Learn AI for FREE with visuals, easy-to-follow insights.<br>
✅ Get cutting-edge topics like GenAI, RAGs, and LLMs in your inbox every week.
</div>
<br>
<div align="center">

[![Subscribe to AwesomeNeuron Newsletter](https://raw.githubusercontent.com/analyticalrohit/analyticalrohit/5ab83e498b11eefe57c91bc4f4cac10414276920/assets/subscribe_button.svg)](https://awesomeneuron.substack.com/)

</div>
<div style="text-align: left;">
    <a href="https://awesomeneuron.substack.com/">
        <img src="https://raw.githubusercontent.com/analyticalrohit/analyticalrohit/refs/heads/main/assets/awesomeneuron_logo.png" alt="AwesomeNeuron Newsletter">
</div>
<p align="center">
  <a href="https://awesomeneuron.substack.com/">
    <img src="https://raw.githubusercontent.com/analyticalrohit/analyticalrohit/refs/heads/main/assets/awesomeneuron_blog.gif" alt="AwesomeNeuron Newsletter">
  </a>
</p>

## Contributing

We welcome contributions from the community! If you have an addition or improvement to suggest:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a pull request

## License

This project is licensed under [MIT License](LICENSE).

---

⭐️ If you find this repository helpful, please consider giving it a star!

[![Star History Chart](https://api.star-history.com/svg?repos=analyticalrohit/ai-blog-generator&type=Date)](https://www.star-history.com/#analyticalrohit/ai-blog-generator&Date)

Keywords: AI, Machine Learning, Generative AI, LLM, AI Agents, Agentic AI, Agno