import openai

openai.api_key = "api_key"

while True:

    prompt = input("\nIntroduce una pregunta: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="text-davinci-003", # Modelo entrenado
                            prompt=prompt,
                            n=1, # Numero de respuestas
                            max_tokens=2048) # Lonfitud de la respuesta

    print(completion.choices[0].text)
