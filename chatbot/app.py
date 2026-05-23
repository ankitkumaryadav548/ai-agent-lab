import ollama
from datetime import datetime
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

messages = []

# Header UI
print(Fore.CYAN + "=" * 45)
print(Fore.GREEN + "🤖 Local AI Assistant")
print(Fore.YELLOW + "Type 'exit' to quit")
print(Fore.CYAN + "=" * 45)

while True:
    # User input
    user = input(Fore.BLUE + "\nYou: ")

    # Exit condition
    if user.lower() in ["exit", "quit", "bye"]:
        print(Fore.MAGENTA + "\n👋 Goodbye!")
        break

    # Save user message
    messages.append({
        "role": "user",
        "content": user
    })

    try:
        # Streaming AI response
        print(Fore.GREEN + "\n🤖 AI: ", end="")

        response = ollama.chat(
            model="phi3:mini",
            messages=messages,
            stream=True
        )

        ai_response = ""

        for chunk in response:
            content = chunk["message"]["content"]
            ai_response += content
            print(content, end="", flush=True)

        print()

        # Save AI response
        messages.append({
            "role": "assistant",
            "content": ai_response
        })

        # Save chat history
        with open("history.txt", "a", encoding="utf-8") as file:
            file.write(f"\n[{datetime.now()}]\n")
            file.write(f"You: {user}\n")
            file.write(f"AI: {ai_response}\n")

    except Exception as e:
        print(Fore.RED + f"\n⚠️ Error: {e}")