from googletrans import Translator
import streamlit as st

st.set_page_config(
    page_title="code.py Tradutor",
    page_icon='codepy.jpeg'
)

st.image('email.png')

translator = Translator()

st.title('Tradutor Inglês <> Português')

texto = st.text_area('Digite aqui o texto:')

idioma = st.selectbox('Selecione o idioma da tradução:', ['pt', 'en'])

if st.button('Traduzir'):
    lista = [texto]
    translations = translator.translate(lista, dest=idioma)
    for translation in translations:
        traducao = translation.text
    st.markdown(traducao)