Step 1: Create a new GitHub repository

Go to https://github.com/new

Fill in the repository details:

Repository name: ai-qna-bot

Description: “A simple AI-powered Q&A chatbot using Python and an API.”

Choose Public.

Check the box “Add a README file”.

Click Create repository.

Step 2: Clone the repository locally

git clone https://github.com/<piyushrawat12345>/Ai-Q&A-Bot.git
cd Ai-QnA-Bot

Step 3: Create your project files

Example structure:

Ai-QnA-Bot/
│
├── Ai Q&A Bot.py                 
├── requirements.txt       
└── README.md              

Step 4: Write the code (example for a command-line Q&A bot)

import os
from groq import Groq

def main():
    # Initialize Groq client
    api_key = os.environ.get("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 ")
    
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

Step 5: Add dependencies

groq

Step 6: Test it locally

python Ai Q&A Bot.py

Step 6: Commit and push to GitHub

git add .
git commit -m "Initial commit with working AI Q&A bot and documentation"
git push origin main

Step 9: Update README.md

Here’s a ready-to-use README.md template:


