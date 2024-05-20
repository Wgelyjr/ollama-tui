from .ollamatui import OllamaInterface
import argparse
import os

def main():
    host = os.environ.get('OLLAMATUI_HOST') if os.environ.get('OLLAMATUI_HOST') else "http://localhost:11434"
    model = os.environ.get('OLLAMATUI_MODEL') if os.environ.get('OLLAMATUI_MODEL') else None
    role = os.environ.get('OLLAMATUI_ROLE') if os.environ.get('OLLAMATUI_ROLE') else "user"
    message = os.environ.get('OLLAMATUI_MESSAGE') if os.environ.get('OLLAMATUI_MESSAGE') else None

    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--host", default=host,help="Host of the Ollama instance")
    parser.add_argument("-m", "--model", default=model, help="Model to utilize within Ollama")
    parser.add_argument("-r", "--role", default=role, help="Role - I don't know why this would be used")
    parser.add_argument("-w","--content", default=message, help="Message to send - leave blank for interactive mode")

    args = parser.parse_args()

    OllamaInterface(
        host=args.host,
        model=args.model,
        role=args.role,
        content=args.content
    )
