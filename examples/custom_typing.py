import logging
from gpt import ChatGPTClient

def main():
    # Initialize with custom logging
    client = ChatGPTClient(log_level=logging.DEBUG, log_file="chat_debug.log")
    
    # Send message with custom typing behavior
    client.send_message(
        "Explain what is Python?",
        typing_speed=(0.05, 0.15),      # Slower typing
        word_pause=(0.3, 0.7),          # Longer pauses between words
        mistake_chance=0.1,             # 10% chance of typos
        human_correct=True              # Correct typos like a human
    )
    
    messages = client.get_messages()
    for msg in messages:
        print(f"{msg.role}: {msg.content}")

if __name__ == "__main__":
    main()
