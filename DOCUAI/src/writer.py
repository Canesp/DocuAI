import os
import keyring
from openai import OpenAI

class Writer:

    def __init__(self) -> None:
        self.api_key = keyring.get_password("DOCUAI", "api_key")
        self.client = OpenAI(api_key=self.api_key)
        self.assistant_id = "asst_NhtwTnQkISVeqVhzYXHB1Kzh"
        self.assistant = self.client.beta.assistants.retrieve(self.assistant_id)

    def write(self) -> None:
        print(self.assistant.id)
        # files = []

        # for file in self.get_files():
            
        #     files.append(self.client.files.create(file=open(file, "rb"), purpose="assistants").id)

        # thread = self.client.beta.threads.create()

        # message = self.client.beta.threads.messages.create(
        #     thread_id=thread.id,
        #     role="user",
        #     content=f"Project name: {os.path.basename(os.getcwd())}",
        # )
        
        # run = self.client.beta.threads.runs.create(
        #     thread_id=thread.id,
        #     assistant_id=self.assistant_id,
        # )

        # run = self.client.beta.threads.runs.retrieve(
        #     thread_id=thread.id,
        #     run_id=run.id,
        # )

        # messages = self.client.beta.threads.messages.list(
        #     thread_id=thread.id,
        # )

        # for message in reversed(messages.data):
        #     print(message.content[0].text.value)

    def get_files(self) -> list[str]:
        
        current_dir = os.getcwd()

        extensions = [".py", ".c", ".html", ".java", ".js", ".css", ".php", ".rb", ".ts"]
        files = []

        for root, dirs, file_names in os.walk(current_dir):
            for file in file_names:
                if file.endswith(tuple(extensions)) and file != "__init__.py":
                    files.append(os.path.join(root, file))

        return files
    
w = Writer()
f = w.write()
