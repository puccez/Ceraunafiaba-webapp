import streamlit as st
from openai import OpenAI
import os
import time


client=OpenAI(api_key=st.secrets('OPENAI_API_KEY'))
MODEL='gpt-4o'

st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/Ceraunafiaba_img.py", label="Fiaba doc generator", icon="1️⃣")

st.title("C'era una fiaba 🧌")


Nome=st.text_input(label='Nome')
Eta=st.text_input(label='Età')
Info=st.text_input(label='Info')
Ambientazione=st.text_input(label='Ambientazione')
Morale=st.text_input(label='Morale')

delimiter = "####"
user_message=f"{Nome}{delimiter}{Eta}{delimiter}{Info}{delimiter}{Ambientazione}{delimiter}{Morale}"
system_message = f"""
sei un aiutante che crea storie affascinanti per bambini. 
ti verranno forniti dei parametri divisi da la scritta {delimiter}: Nome, Eta, Colore pelle, Colore occchi, Colore capelli, Informazioni generali, Ambientazione della storia, Morale della storia. 
il colore della pelle e la morale della storia non devono essere espliciti nel testo
devi scrive una storia di 10 pagine, ogni pagina deve avere un testo di 500 caratteri. La prima pagina deve contenere un titolo di massimo 15 caratteri.
obbiettivo: far capire in modo semplice la morale della storia al bambino
il linguaggio deve essere semplice
"""

if st.button('Genera una storia'):
    with st.spinner('Generando la storia...'):
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.007)
        
        with st.chat_message('ai'):
            message_placeholder=st.empty()
            completition = client.chat.completions.create(
                model=MODEL,
                temperature=0.5,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": f"{delimiter}{user_message}{delimiter}"},
                ], 
                max_tokens=4000 
                )
            output = completition.choices[0].message.content
            message_placeholder.markdown(output)
        
else:
    st.write('Clicca il bottone per generare la storia.')
