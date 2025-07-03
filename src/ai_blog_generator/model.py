from agno.models.anthropic import Claude
from agno.models.google import Gemini
from agno.models.openai import OpenAIChat
from agno.models.xai import xAI


class Model:
    def __init__(self, provider: str, model_name: str, api_key: str):
        self.provider = provider
        self.api_key = api_key
        if not model_name:
            raise ValueError("Model name must be provided.")
        self.model = self._get_model(model_name)

    def _get_model(self, model_name):
        try:
            if self.provider == "OpenAI":
                return OpenAIChat(api_key=self.api_key, id=model_name)
            elif self.provider == "Gemini":
                return Gemini(api_key=self.api_key, id=model_name)
            elif self.provider == "Claude":
                return Claude(api_key=self.api_key, id=model_name)
            elif self.provider == "Grok":
                return xAI(api_key=self.api_key, id=model_name)
            else:
                raise ValueError(f"Unsupported provider: {self.provider}")
        except Exception as e:
            raise ValueError(e)

    def get(self):
        return self.model
