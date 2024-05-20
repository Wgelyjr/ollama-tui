import asyncio
import ollama
import argparse
import sys

class OllamaInterface:

    def __init__(self, host, model, role, content):
        self.host = host
        self.model = model
        self.role = role
        self.content = content

        if not self.content:
            self.interactive_interface()
        else:
            self.one_shot()
            print("\n")

    async def chat(self):
        message = {'role': self.role, 'content': self.content}
        async for part in await ollama.AsyncClient(host=self.host).chat(model=self.model, messages=[message], stream=True):
            print(part['message']['content'], end='', flush=True)
        
    def one_shot(self):
        asyncio.run(self.chat())

    def content_parser(self):
        if not self.content.startswith('/'):
            return
        self.content = self.content[1::]
        if self.content == "bye":
            print("Bye!")
            sys.exit(0)

    def interactive_interface(self):
        if not self.model:
            self.model = str(input("\nModel:\n>>>"))
        print("Interactive Mode; exit with ctrl+D, or '/bye';")
        while True:
            self.content = str(input("\n\n>>>"))
            self.content_parser()
            self.one_shot()
