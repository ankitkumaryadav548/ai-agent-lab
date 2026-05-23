import ollama

messages = []

while True:
    user = input("You: ")

    messages.append({
        "role": "user",
        "content": user
    })

    response = ollama.chat(
        model='phi3:mini',
        messages=messages
    )

    ai = response['message']['content']

    print("AI:", ai)

    messages.append({
        "role": "assistant",
        "content": ai
    })