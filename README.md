# 🤖 AutoChatgpt

![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Automation](https://img.shields.io/badge/automation-enabled-green)
![Stars](https://img.shields.io/github/stars/vibheksoni/AutoChatgpt?style=social)

Your AI assistant on autopilot - A powerful automation framework for ChatGPT that simulates human-like interaction patterns. No API required!

## ✨ Why AutoChatgpt?

- 🎯 **Full Automation**: Create autonomous ChatGPT workflows
- 🤖 **Task Scheduling**: Run conversations on your schedule
- 🔄 **Workflow Chains**: Connect multiple ChatGPT interactions
- 🎮 **Smart Controls**: Fine-tune behavior and responses
- 🚀 **Human Simulation**: Natural typing and interaction patterns
- 📊 **Result Export**: Save conversations and analytics

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/vibheksoni/AutoChatgpt.git

# Install dependencies
pip install -r requirements.txt
```

## 🎯 Quick Start

```python
from gpt import ChatGPTClient

# Initialize the client
client = ChatGPTClient()

# Send a message with human-like typing
client.send_message("What is Python?")

# Get the conversation history
messages = client.get_messages()
for msg in messages:
    print(f"{msg.role}: {msg.content}")
```

## 🎨 Features

### Human-Like Typing Simulation
```python
client.send_message(
    "Hello, how are you?",
    typing_speed=(0.05, 0.15),    # Typing speed variation
    word_pause=(0.2, 0.5),        # Natural pauses between words
    mistake_chance=0.05,          # Occasional typos
    human_correct=True            # Natural correction behavior
)
```

### Configurable Logging
```python
import logging

# Debug mode with custom log file
client = ChatGPTClient(
    log_level=logging.DEBUG,
    log_file="chatgpt_debug.log"
)

# Disable logging
client = ChatGPTClient(log_level=None)
```

### Interactive Conversations
```python
# From examples/conversation_loop.py
client = ChatGPTClient()
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    client.send_message(user_input)
```

## 📚 Examples

The [examples](examples/) directory contains automation scenarios:
- `basic_chat.py`: Simple automated interactions
- `custom_typing.py`: Advanced human-like behavior
- `conversation_loop.py`: Continuous chat automation
- `code_generation.py`: Automated code generation

## 🛡️ Error Handling

The framework includes comprehensive error handling for:
- Network issues
- Authentication challenges
- Message parsing errors
- Session management
- Response timeouts

## 🤝 Contributing

Contributions are what make the open source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⭐ Show Your Support

If you find this project useful, please consider giving it a star! It helps others discover this tool and motivates continued development.

[![GitHub Star](https://img.shields.io/github/stars/vibheksoni/AutoChatgpt?style=social)](https://github.com/vibheksoni/AutoChatgpt)

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👨‍💻 Author

**Vibhek Soni** - [@vibheksoni](https://github.com/vibheksoni)

If you like this project, please consider:
- ⭐ Starring the repository
- 🐦 Following me on GitHub
- 🍴 Forking the project

## 🙏 Acknowledgments

- Thanks to all contributors who help improve this project
- Special thanks to the open-source community
- Inspired by the need for human-like ChatGPT automation

---

<p align="center">Made with ❤️ by <a href="https://github.com/vibheksoni">Vibhek Soni</a></p>
