# Ollama-TUI

A simple terminal interface for interacting with an external Ollama server. Linux only, requires Python 3.8+.

## Installation & Usage:

```
git clone git@github.com:Wgelyjr/ollama-tui.git
cd ollama-tui
pip install .
```

Pip will install it to your system PATH.

From there, you can:

Export environment variables with your preferred defaults:
- OLLAMATUI_HOST="http://locahost:11434"
- OLLAMATUI_MODEL="llama3"
- OLLAMATUI_ROLE="user"
- OLLAMATUI_MESSAGE="When was beethoven born?"

Pass your preferred defaults into the application:

`ollama-tui -h localhost:11434`

Command-line switches will override entries from environment variables.

Message-less calls will result in the application being opened in interactive mode. Interactive mode can be exited by saying `/bye`.