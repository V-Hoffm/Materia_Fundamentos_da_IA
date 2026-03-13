import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("Api_Key")

chat = ChatGroq(model='llama-3.3-70b-versatile')

def resposta_bot(mensagens):
  # contexto do modelo definido abaixo
  mensagens_modelo = [('system', 'Você é um professor com experiência em engenharia de dados da Univille IA ')]
  mensagens_modelo += mensagens
  template = ChatPromptTemplate.from_messages(mensagens_modelo)
  chain = template | chat
  return chain.invoke({}).content

print('Bem-vindo ao Univille AI')

mensagens = []
while True:
  pergunta = input('Usuario: ')
  if pergunta.lower() == 'x':
    break
  mensagens.append(('user', pergunta))
  resposta = resposta_bot(mensagens)
  mensagens.append(('assistant', resposta))
  print(f'Bot: {resposta}')

print('Muito obrigado por usar o Univille AI')
print(mensagens)