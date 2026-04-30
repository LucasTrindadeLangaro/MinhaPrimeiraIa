from google import genai

client = genai.Client(api_key="AIzaSyCytOooxBb9JZXwQOdA026X9bMAvPJoQSc")

chat = client.chats.create(model="gemini-3-flash-preview")
pergunta = input("digite sua pergunta: ").upper()

while pergunta != "FIM":
    resposta = chat.send_message(pergunta)
    print(resposta.text)
    pergunta = input("digite sua pergunta: ").upper()