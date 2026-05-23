import ollama
from datetime import datetime

messages = []

print("=" * 40)
print("🤖 Local AI Assistant")
print("Type 'exit' to quit")
print("=" * 40)

while True:
    user = input("\nYou: ")

    if user.lower() in ["exit", "quit", "bye"]:
        print("\n👋 Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user
    })

    try:
        response = ollama.chat(
            model="phi3:mini",
            messages=messages
        )

        ai_response = response["message"]["content"]

        print(f"\n🤖 AI: {ai_response}")

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
        print("\n⚠️ Error:", e)