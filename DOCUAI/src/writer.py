import os
import keyring
from openai import OpenAI

class Writer:

    def __init__(self) -> None:
        self.api_key = keyring.get_password("DOCUAI", "api_key")
        self.client = OpenAI(api_key=self.api_key)
        self.assistant_id = "asst_NhtwTnQkISVeqVhzYXHB1Kzh"
        self.assistant = self.client.beta.assistants.retrieve(self.assistant_id)

    def write(self, notes: str) -> bool:
        
        files = []

        for file in self.get_files():
            
            files.append(self.client.files.create(file=open(file, "rb"), purpose="assistants").id)

        print(files)

        thread = self.client.beta.threads.create()

        message = self.client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=f"Project name: {os.path.basename(os.getcwd())}, Notes: {notes if notes else ''}.",
            file_ids=files,
        )
        
        run = self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=self.assistant.id,
            instructions="",
        )

        while run.status in ["queued", "in_progress"]:
            run = self.client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id,
            )

        for file in files:
            self.client.files.delete(file)

        messages = self.client.beta.threads.messages.list(
            thread_id=thread.id,
        )

        message = messages.data[0]

        if message.file_ids != []:
            download_file_id = message.file_ids[0]
            dowloaded_file = self.client.files.content(download_file_id)
            dowloaded_file = dowloaded_file.read()

            with open("README.md", "wb") as f:
                f.write(dowloaded_file)

            return True
        else:
            return False

        

    def get_files(self) -> list[str]:
        
        current_dir = os.getcwd()

        extensions = [".py", ".c", ".html", ".java", ".js", ".css", ".php", ".rb", ".ts"]
        files = []

        for root, dirs, file_names in os.walk(current_dir):
            for file in file_names:
                if file.endswith(tuple(extensions)) and file != "__init__.py":
                    files.append(os.path.join(root, file))

        return files
    
