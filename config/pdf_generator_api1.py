def pdf_generator_api(testo, immagini):
    import http.client
    import jwt
    import datetime
    import json
    import os
    import streamlit as st

    def create_bearer_token(secret, algorithm='HS256'):
        # Header
        header = {
            "alg": algorithm,
            "typ": "JWT"
        }
        
        # Payload
        payload = {
            "iss": "62a9980822e387a5d88557458d6811f826b9db3d12f91b9b8dd5643663e245ac",
            "sub": "emanuele.puccetti@icloud.com",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        }
        
        # Encode JWT
        token = jwt.encode(payload, secret, algorithm=algorithm, headers=header)
        
        return token

    # Secret key
    secret = st.secrets['PDF_GEN_SECRET']
    

    # Create token
    token = create_bearer_token(secret)
    token_str = token
    st.write('token pdf api generato!')

    conn = http.client.HTTPSConnection("us1.pdfgeneratorapi.com")

    immagini = ["data:image/png;base64," + img for img in immagini]

    # payload = "{\"template\":{\"id\":\"1074008\",\"data\":{\"titolopagina1\":\"" + testo[0] + "\",\"pagina1\":\"" + testo[1] + "\",\"pagina2\":\"" + testo[2] + "\",\"pagina3\":\"" + testo[3] + "\",\"img1\":\"" + immagini[0] + "\",\"img2\":\"" + immagini[1] + "\",\"img3\":\"" + immagini[2] + "\"}},\"format\":\"pdf\",\"output\":\"url\",\"name\":\"output\"}"

    import json

    data_dict = {
        "template": {
            "id": "1074008",
            "data": {
                "titolopagina1": testo[0],
                "pagina1": testo[1],
                "pagina2": testo[2],
                "pagina3": testo[3],
                "pagina4": testo[4],
                "pagina5": testo[5],
                "img1": immagini[0],
                "img2": immagini[1],
                "img3": immagini[2],
                "img4": immagini[3],
                "img5": immagini[4]
            }
        },
        "format": "pdf",
        "output": "file",
        "name": "output"
    }

    payload = json.dumps(data_dict)

    # print(payload)

    headers = {
        'content-type': "application/json",
        'Authorization': f"Bearer {token_str}"
        }

    conn.request("POST", "/api/v4/documents/generate", payload, headers)

    res = conn.getresponse()
    data = res.read()

    if res.status != 200:
        st.write(f"Error: {res.status} - {res.reason}")
        st.write(data.decode('utf-8'))
        return None

    pdf_dir = 'data'
    pdf_path = os.path.join(pdf_dir, 'output.pdf')

    # Ensure the directory exists
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    try:
        with open(pdf_path, 'wb') as f:
            f.write(data)
        st.write('PDF created successfully!')
    except Exception as e:
        st.write(f"Failed to write PDF file: {e}")
        return None
    
    return pdf_path