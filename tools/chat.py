# Third party
import openai


openai.api_key = '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'


def chat_with_gpt(prompt) -> str:
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=256,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip()


print('Welcome to the ChatGPT console!')

while True:
    user_input: str = input('You: ')
    if user_input.lower() in ['quit', 'exit']:
        break

    # Send user input as a prompt to ChatGPT
    response = chat_with_gpt(user_input)

    print('ChatGPT:', response)
