from gpt import ChatGPTClient

def main():
    # Disable logging for this example
    client = ChatGPTClient(log_level=None)
    
    print("ChatGPT Conversation (type 'quit' to exit)")
    print("-" * 50)
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'quit':
            break
            
        # Send message with minimal typing simulation
        success = client.send_message(
            user_input,
            typing_speed=(0.01, 0.03),
            word_pause=(0.05, 0.1),
            mistake_chance=0
        )
        
        if success:
            # Get only the last message (the response)
            messages = client.get_messages()
            if messages:
                print(f"\nChatGPT: {messages[-1].content}")
        else:
            print("\nError: Failed to get response")

if __name__ == "__main__":
    main()
