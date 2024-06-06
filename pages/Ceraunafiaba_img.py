from openai import OpenAI
import json
import streamlit as st
import time
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.img_prompt import img_prompt
from config.pdf_generator_api1 import pdf_generator_api


st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/Ceraunafiaba_img.py", label="Fiaba doc generator", icon="1️⃣")

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

MODEL="gpt-4o"

api_key=st.secrets['OPENAI_API_KEY']
print(api_key)
client=OpenAI(api_key=api_key)


delimiter = "####"

example = {
        "titolopagina1": "text",
        "pagina1": "text",
        "pagina2": "text",
        "pagina3": "text",
        "pagina4": "text",
        "pagina5": "text",
        "pagina6": "text",
        "pagina7": "text",
        "pagina8": "text",
        "pagina9": "text",
        "pagina10": "text"
}

example_json = json.dumps(example) 


system_message = f"""
sei un aiutante che crea storie affascinanti per bambini. 
ti verranno forniti dei parametri divisi da la scritta {delimiter}: Nome, Eta, Colore pelle, Colore occchi, Colore capelli, Informazioni generali, Ambientazione della storia, Morale della storia. 
il colore della pelle e la morale della storia non devono essere espliciti nel testo
devi scrive una storia di 10 pagine, ogni pagina deve avere un testo di 500 caratteri. La prima pagina deve contenere un titolo di massimo 15 caratteri.
obbiettivo: far capire in modo semplice la morale della storia al bambino
il linguaggio deve essere semplice
output: una lista di oggetti JSON divisa per pagine tipo così: {example_json}
"""

Nome = st.text_input(label='Nome')
Eta = st.text_input(label='Eta')
Pelle = st.text_input(label='Colore pelle')
Occhi = st.text_input(label='Colore occchi')
Capelli = st.text_input(label='Colore capelli')
Info = st.text_input(label='Informazioni generali')
Ambientazione = st.text_input(label='Ambientazione della storia')
Morale = st.text_input(label='Morale della storia')



user_message=f"{Nome}{delimiter}{Eta}{delimiter}{Pelle}{delimiter}{Occhi}{delimiter}{Capelli}{delimiter}{Info}{delimiter}{Ambientazione}{delimiter}{Morale}"







if st.button('Genera la storia'):
    with st.spinner('Generando la storia...'):
        
        
        while True:
            try:
                progress_bar = st.progress(10)

                completition = client.chat.completions.create(
                model=MODEL,
                temperature=0.5,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": f"{delimiter}{user_message}{delimiter}"},
                ], 
                max_tokens=4000 
                )
                content = json.loads(completition.choices[0].message.content)
                
                progress_bar.progress(15)

                titolopagina1=content["titolopagina1"]
                pagina1=content["pagina1"]
                pagina2=content["pagina2"]
                pagina3=content["pagina3"]
                pagina4=content["pagina4"]
                pagina5=content["pagina5"]
                pagina6=content["pagina6"]
                pagina7=content["pagina7"]
                pagina8=content["pagina8"]
                pagina9=content["pagina9"]
                pagina10=content["pagina10"]

                gpt_output = [
                    titolopagina1,
                    pagina1,
                    pagina2,
                    pagina3,
                    pagina4,
                    pagina5,
                    pagina6,
                    pagina7,
                    pagina8,
                    pagina9,
                    pagina10
                ]
                
                st.write('testo generato!')
                progress_bar.progress(30)
                

                with open(pdf_generator_api(testo=gpt_output, immagini=img_prompt(gpt_output=gpt_output)), "rb") as file:
                    btn = st.download_button(
                            label="Scarica il PDF!",
                            data=file,
                            file_name="Storia.pdf",
                            mime="Ceraunafiaba-webapp/config/data"
                        )
                progress_bar.progress(100)
                break

            except Exception as e:
                st.error(f"Error: {e}"),
                st.write("Trying again...")
                time.sleep(1)

        
else:
    st.write('Per favore clicca qui per generare la storia.')

