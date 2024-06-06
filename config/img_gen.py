from openai import OpenAI
import json


def img_gen(prompt):
  print('inizio generazione immagini (ci vorrà un po)')
  client = OpenAI()

  img = json.loads(prompt)
  image_urls = []
  
  for i in range(1,4):
    response = client.images.generate(
      model="dall-e-3",
      prompt=f"{img[f"pagina{i}"]}. Lo stile deve essere cartoon astratto e l'orientazione orizzontale. L'immagin non deve assolutamente contenere scritte",
      n=1,
      size="1024x1792",
      response_format='b64_json'
    )

    url = response.data[0].b64_json
    print(f'generata immagine {i}')
    image_urls.append(url)

  print('immagini generate!')
  return image_urls
  



