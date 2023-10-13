import openai

openai.api_key = ""  # don't worry, I deleted this already


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "thanks"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
