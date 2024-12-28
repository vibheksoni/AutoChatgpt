import logging
from gpt import ChatGPTClient

def main():
    # Initialize with default settings
    client = ChatGPTClient()
    
    # Send a message and wait for response
    client.send_message("Write a hello world program in Python")
    
    # Get conversation history
    messages = client.get_messages()
    for msg in messages:
        print(f"{msg.role}: {msg.content}")

if __name__ == "__main__":
    main()
