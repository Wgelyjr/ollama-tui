import asyncio
import ollama
import argparse
import sys

class OllamaInterface:

    def __init__(self, client, model, role, content):
        self.client = client
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
        async for part in await ollama.AsyncClient(host=self.client).chat(model=self.model, messages=[message], stream=True):
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c","--client",default="http://localhost:11434",help="Host of the Ollama instance")
    parser.add_argument("-m", "--model", default="llama3", help="Model to utilize within Ollama")
    parser.add_argument("-r", "--role", default="user", help="Role - I don't know why this would be used")
    parser.add_argument("-w","--content", default=None, help="Message to send - leave blank for interactive mode")

    args = parser.parse_args()

    OllamaInterface(
        client=args.client,
        model=args.model,
        role=args.role,
        content=args.content
    )

if __name__ == "__main__":
    main()