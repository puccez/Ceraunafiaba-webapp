from openai import OpenAI
from config.img_gen import img_gen
import streamlit as st

def img_prompt(gpt_output):
    MODEL='gpt-4o'
    client=OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

    example = """
        "pagina1": "img prompt",
        "pagina2": "img prompt",
        "pagina3": "img prompt",
        "pagina4": "img prompt",
        "pagina5": "img prompt",
        "pagina6": "img prompt",
        "pagina7": "img prompt",
        "pagina8": "img prompt",
        "pagina9": "img prompt",
        "pagina10": "img prompt"
    """

    type_prompt = """
    Generate images using this exact template:
    Digital painting of a distinctly feminine green-eyed, white-furred tabaxi monk (with fluffy cheeks and a tuft on her head) with gradient shading, clean linework, vibrant palette, and stylized proportions. Wearing a simple green monk tunic and carrying a pack, [scenario]
    The scenario should always:
    1. be in a setting
    2. doing a thing (use dynamic verbs, not passive things like "waiting" or "watching")
    3. showing a strong emotion
    Make sure to use the exact template given.
    """

    completition = client.chat.completions.create(
        model=MODEL,
        temperature=0.5,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": f""" 
             genera promp per dalle usando questo template: 
             {type_prompt},
             le immagini devono essere verticali

             L'output deve essere una lista json di questo tipo: 
             {example}
            """},
            {"role": "user", "content": f"{gpt_output}"},
        ], 
        )
    


    img_prompt_out = completition.choices[0].message.content
    print('prompt immagini generato!')
    st.progress(40)
    return img_gen(prompt=img_prompt_out)
    

# gpt_output = ['Giorgio e la Musica', "C'era una volta un bambino di nome Giorgio. Aveva tre anni, occhi celesti e capelli biondi. Giorgio abitava in una grande città piena di suoni e rumori. Ogni giorno, mentre camminava con la mamma, sentiva la musica delle strade: il cinguettio degli uccelli, il rumore delle auto e il suono delle campane. Giorgio amava la musica e spesso si fermava ad ascoltare ogni suono con grande attenzione.", "Un giorno, mentre passeggiava nel parco con la mamma, Giorgio sentì un suono dolce e melodioso. Seguì il suono e trovò un musicista che suonava il violino. Giorgio rimase incantato e si sedette sull'erba ad ascoltare. Il musicista notò Giorgio e gli sorrise. Finito il pezzo, il musicista chiese a Giorgio se gli piacesse la musica. Giorgio annuì con entusiasmo e il musicista gli raccontò una storia speciale sulla musica.", '"La musica è dappertutto," spiegò il musicista. "Basta saper ascoltare. Ogni suono può diventare una melodia se lo ascolti con il cuore." Giorgio era affascinato da quelle parole. Tornato a casa, iniziò a prestare ancora più attenzione ai suoni intorno a lui. Scoprì che il ticchettio dell\'orologio, il fruscio delle foglie e persino il ronzio del frigorifero avevano una loro musica.', "Una sera, mentre era a letto, Giorgio sentì un suono strano provenire dalla finestra. Si alzò e guardò fuori. Era il vento che faceva danzare le foglie degli alberi. Giorgio chiuse gli occhi e immaginò di essere un direttore d'orchestra, dirigendo il vento e le foglie in una sinfonia magica. Sentì una grande gioia nel cuore e capì che la musica era davvero dappertutto, proprio come aveva detto il musicista.", "Il giorno dopo, Giorgio decise di creare la sua musica. Prese delle pentole dalla cucina e iniziò a battere con i cucchiai. Ogni colpo produceva un suono diverso e Giorgio si divertiva un mondo. La mamma, sentendo il rumore, entrò in cucina e sorrise vedendo il suo piccolo musicista all'opera. Prese una pentola e iniziò a suonare insieme a lui. La cucina si trasformò in una sala concerti piena di allegria.", 'Nel pomeriggio, Giorgio e la mamma andarono al mercato. Qui, Giorgio ascoltò i venditori che chiamavano i clienti, il tintinnio delle monete e il chiacchiericcio delle persone. Ogni suono era una nota nella sua mente. Quando tornarono a casa, Giorgio prese dei fogli e iniziò a disegnare la sua giornata, trasformando ogni suono in una nota musicale. La mamma lo guardava con orgoglio e ammirazione.', 'Un giorno, al parco, Giorgio incontrò di nuovo il musicista del violino. Lo salutò con entusiasmo e gli raccontò di tutte le musiche che aveva scoperto nella città. Il musicista sorrise e disse: "Vedi, Giorgio, la musica è come un amico. È sempre con noi, basta solo cercarla e ascoltarla con il cuore." Giorgio annuì felice, sentendosi un piccolo esploratore del mondo dei suoni.', 'Da quel giorno, Giorgio continuò a scoprire nuove musiche ogni giorno. A scuola, ascoltava il suono delle matite che scrivevano sui fogli, il ronzio del ventilatore e le risate dei suoi amici. Ogni suono diventava una melodia nella sua mente. Giorgio capì che la musica non era solo nelle canzoni, ma in ogni piccolo suono intorno a lui. E questo lo rendeva felice e sereno.', "Una sera, mentre ascoltava una ninna nanna cantata dalla mamma, Giorgio chiuse gli occhi e sognò di essere un grande musicista. Nel sogno, dirigeva un'orchestra fatta di uccelli, foglie, vento e stelle. Ogni suono si univa in una sinfonia perfetta e Giorgio si sentiva al settimo cielo. Quando si svegliò, capì che il sogno era un regalo della musica che aveva nel cuore.", 'Giorgio continuò a crescere con la musica nel cuore. Ogni giorno, scopriva nuove melodie e suoni che lo ispiravano. La città era il suo grande palcoscenico e ogni suono era una nota della sua sinfonia personale. Giorgio imparò che la musica non è solo nelle canzoni, ma in ogni piccolo suono intorno a noi. E così, ogni giorno, viveva con gioia e meraviglia, ascoltando il mondo con il cuore aperto.']

# img_prompt(gpt_output)
