from gpt import ChatGPTClient
import re

def extract_code_blocks(content: str) -> list[str]:
    """Extract code blocks from markdown formatted text."""
    pattern = r"```[\w]*\n(.*?)```"
    return re.findall(pattern, content, re.DOTALL)

def main():
    client = ChatGPTClient()
    
    # Ask for multiple code examples
    prompts = [
        "Write a Python function to calculate factorial",
        "Write a Python class for a simple bank account",
        "Write a Python decorator to measure execution time"
    ]
    
    for prompt in prompts:
        print(f"\nPrompt: {prompt}")
        print("-" * 50)
        
        success = client.send_message(prompt)
        if success:
            messages = client.get_messages()
            if messages:
                response = messages[-1].content
                code_blocks = extract_code_blocks(response)
                
                print("\nGenerated Code:")
                for i, code in enumerate(code_blocks, 1):
                    print(f"\nCode Block {i}:")
                    print(code.strip())
        
        print("-" * 50)

if __name__ == "__main__":
    main()
