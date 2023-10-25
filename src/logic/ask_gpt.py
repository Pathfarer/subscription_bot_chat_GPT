import openai


async def ask_gpt(question: str) -> (str, bool):
    completion = await openai.ChatCompletion.acreate(model="gpt-4",
                                                     messages=[{"role": "user", "content": question}])

    return completion.choices[0].message.content
