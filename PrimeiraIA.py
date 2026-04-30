from google import genai


arquivo = open("D:/cursos/MinhaPrimeiraIA/MinhaPrimeiraIa/api.txt","r")
conteudo = arquivo.read()
print(conteudo)
client = genai.Client(api_key=conteudo)

chat = client.chats.create(model="gemini-3-flash-preview")
pergunta = input("digite sua pergunta: ").upper()

while pergunta != "FIM":
    resposta = chat.send_message(pergunta)
    print(resposta.text)
    pergunta = input("digite sua pergunta: ").upper()