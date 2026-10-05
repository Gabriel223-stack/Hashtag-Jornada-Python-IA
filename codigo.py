# titulo
# campo de mensagem (input)
# quando o usuário enviar uma mensagem
    # mostrar a mensagem na conversa
    # mandar mensagem para IA responder
    # mostrar a resposta da IA
    
# pip install streamlit openai
# streamlit run codigo.py

import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="...",
                   base_url="https://generativelanguage.googleapis.com/v1beta/openai")

st.write("## ChatBot de IA")

# criar o historico de mensagens
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

mensagem_usuario = st.chat_input("Digite sua mensagem aqui...")

for mensagem in st.session_state["lista_mensagens"]:
    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"]
    st.chat_message(quem_enviou).write(texto_mensagem)

if mensagem_usuario:
    # exibir a mensagem do usuário na tela
    # user -> usuario
    # assistant -> inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    mensagem1 = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem1)
    
    # pegar a resposta da IA
    resposta_modelo = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gemini-flash-lite-latest"
    )
    
    print(resposta_modelo)
    
    resposta_ia = resposta_modelo.choices[0].message.content
    
    # enviar a mensagem da IA no chat
    st.chat_message("assistant").write(resposta_ia)
    mensagem2 = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem2)

    
# tornar as respostas inteligentes
