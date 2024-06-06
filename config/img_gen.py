from openai import OpenAI
import json
import streamlit as st


def img_gen(prompt):
  st.write('inizio generazione immagini (ci vorrà un po)')
  client=OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

  img = json.loads(prompt)
  image_urls = []
  
  for i in range(1,4):
    pagine = img[f'pagina{i}']
    response = client.images.generate(
      model="dall-e-3",
      prompt=f"{pagine}. Lo stile deve essere cartoon astratto e l'orientazione orizzontale. L'immagin non deve assolutamente contenere scritte",
      n=1,
      size="1024x1792",
      response_format='b64_json'
    )

    url = response.data[0].b64_json
    st.write(f'generata immagine {i}')
    image_urls.append(url)

  st.write('immagini generate!')
  st.progress(70)
  return image_urls
  



