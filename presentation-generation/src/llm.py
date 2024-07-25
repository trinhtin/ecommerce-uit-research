# src/llm.py
from some_llm_library import LLMClient

class LLM:
    def __init__(self, config):
        self.client = LLMClient(config)

    def generate_response(self, context):
        return self.client.generate(context)
