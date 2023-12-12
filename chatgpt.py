import openai

openai.api_key = "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"

while True:

    prompt = input("\nIntroduce una pregunta: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="text-davinci-003", # Modelo entrenado
                            prompt=prompt,
                            n=1, # Numero de respuestas
                            max_tokens=2048) # Lonfitud de la respuesta

    print(completion.choices[0].text)
