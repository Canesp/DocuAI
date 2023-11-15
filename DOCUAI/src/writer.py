import os
from openai import OpenAI

class Writer:

    def __init__(self) -> None:
        self.api_key = os.getenv("api_key")
        self.client = OpenAI(self.api_key)
        self.assistant_id = "asst_NhtwTnQkISVeqVhzYXHB1Kzh"
        self.assistant = self.client.beta.assistants.retrieve(self.assistant_id)

    def write(self, files: list[str]) -> None:
        pass