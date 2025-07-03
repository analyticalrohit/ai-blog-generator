def get_default_llm(provider: str) -> str:
    """Get the default LLM name based on the provider"""
    if provider == "OpenAI":
        return "gpt-4o"
    elif provider == "Gemini":
        return "gemini-2.0-flash"
    elif provider == "Claude":
        return "claude-3-5-sonnet-20241022"
    elif provider == "Grok":
        return "grok-beta"
    else:
        raise ValueError(f"Unsupported provider: {provider}")


example_prompts = [
    "How Generative AI is Changing the Way We Work",
    "The Science Behind Why Pizza Tastes Better at 2 AM",
    "How Rubber Ducks Revolutionized Software Development",
    "Why Dogs Think We're Bad at Smelling Things",
    "What Your Browser Tabs Say About You",
]

custom_css = """
.center-text h1, .center-text {
    text-align: center;
    font-size: 36px !important;
    font-weight: bold;
}
"""
