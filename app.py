import gradio as gr
import markdown

from ai_blog_generator.agents import BlogAgents
from ai_blog_generator.generator import BlogPostGenerator
from ai_blog_generator.model import Model
from ai_blog_generator.utils import custom_css, example_prompts, get_default_llm


def generate_blog(llm_provider, llm_name, api_key, user_topic):
    if not api_key:
        gr.Warning(f"Please enter your {llm_provider} API key.")
    if not llm_name or llm_name.strip() == "":
        gr.Warning("Please enter a model name.")
    url_safe_topic = user_topic.lower().replace(" ", "-")
    llm = Model(llm_provider, llm_name, api_key)
    blog_agents = BlogAgents(llm)
    generate_blog_post = BlogPostGenerator(
        blog_agents=blog_agents,
        session_id=f"generate-blog-post-on-{url_safe_topic}",
        debug_mode=True,
    )
    blog_post = generate_blog_post.run(topic=user_topic)
    final_output = ""
    sources = set()
    for response in blog_post:
        if hasattr(response, "content") and response.content:
            final_output += str(response.content) + "\n"
        if hasattr(response, "sources") and response.sources:
            if isinstance(response.sources, (list, set)):
                sources.update(response.sources)
            else:
                sources.add(str(response.sources))

    # Format sources into HTML
    sources_html = ""
    if sources:
        sources_html = "<h3>Sources:</h3><ul>" + "".join(f"<li>{src}</li>" for src in sources) + "</ul>"
    html_body = markdown.markdown(final_output)
    html_content = f"<div>{html_body}{sources_html}</div>"
    return gr.update(value=html_content, visible=True), ""


with gr.Blocks(title="Blog Generator", css=custom_css) as demo:
    gr.Markdown("# AI Blog Generator", elem_classes="center-text")
    with gr.Row():
        with gr.Column(scale=1):
            llm_provider = gr.Radio(
                label="Select LLM Provider",
                choices=["OpenAI", "Gemini", "Claude", "Grok"],
                value="Gemini",
            )

            # Function to update the textbox when provider changes
            def update_llm_name(provider):
                return get_default_llm(provider)

            llm_name = gr.Textbox(
                label="Enter LLM Name",
                value=get_default_llm(llm_provider.value),
                info="Specify the model name based on the provider.",
            )
            # When provider changes, update the textbox
            llm_provider.change(fn=update_llm_name, inputs=llm_provider, outputs=llm_name)

            api_key = gr.Textbox(label="Enter API Key", type="password")
            selected_prompt = gr.Radio(
                label="Select an example or enter your own topic below:",
                choices=example_prompts,
                value=example_prompts[0],
            )
            user_topic = gr.Textbox(label="Enter your own blog topic", value=example_prompts[0])
            generate_btn = gr.Button("Generate Blog")
        with gr.Column(scale=2):
            output = gr.HTML(
                label="Generated Post",
                visible=True,
            )
            warning = gr.Textbox(label="Warning", visible=False)

    def sync_topic(selected, current):
        return selected

    selected_prompt.change(sync_topic, [selected_prompt, user_topic], user_topic)
    generate_btn.click(
        generate_blog,
        inputs=[llm_provider, llm_name, api_key, user_topic],
        outputs=[output, warning],
    )

demo.launch()
