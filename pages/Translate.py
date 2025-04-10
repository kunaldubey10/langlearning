import streamlit as st
from googletrans import Translator

st.title("Translation Tool")
translator = Translator()
text = st.text_input("Enter text")
target = st.selectbox("Translate to", ["es", "fr", "de", "ja"])

if text:
    translated = translator.translate(text, dest=target)
    st.success(translated.text)
