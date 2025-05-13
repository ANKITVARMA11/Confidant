from openai import OpenAI

client = OpenAI()

# Initializing conversation history
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant. Only use the content provided. Do not use any outside knowledge."}
]

def reply(user_input: str):
    # Appending the new user input to the old one
    conversation_history.append({"role": "user", "content": user_input})

    # Sending the full conversation to the API
    response = client.chat.completions.create(
        model="gpt-4",
        messages=conversation_history,
        temperature=0.3
    )

    # Extracting the assistant's reply
    reply = response.choices[0].message.content.strip()

    # Appending the assistant's reply to history
    conversation_history.append({"role": "assistant", "content": reply})

    return reply
