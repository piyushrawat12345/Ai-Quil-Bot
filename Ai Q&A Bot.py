import os
from groq import Groq

def main():
    # Initialize Groq client
    api_key = os.environ.get("GROQ_API_KEY")
    
    if not api_key:
        print("Error: GROQ_API_KEY environment variable not set")
        print("Please set it using: export GROQ_API_KEY='your-api-key-here'")
        return
    
    client = Groq(api_key=api_key)
    
    print("=" * 50)
    print("AI Q&A Bot - Powered by Groq")
    print("=" * 50)
    print("Type your questions below (type 'quit' or 'exit' to stop)\n")
    
    while True:
        # Get user input
        question = input("You: ").strip()
        
        # Exit condition
        if question.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye! 👋")
            break
        
        if not question:
            continue
        
        try:
            # Call Groq API
            print("\nBot: ", end="", flush=True)
            
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": question,
                    }
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=1024,
            )
            
            # Print response
            answer = chat_completion.choices[0].message.content
            print(answer)
            print()
            
        except Exception as e:
            print(f"\nError: {str(e)}\n")

if __name__ == "__main__":
    main()
