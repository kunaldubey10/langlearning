import streamlit as st
from utils.db import fetchone

st.title("Word of the Day")
lang = st.selectbox("Choose Language", ["Spanish", "French", "Japanese"])

word = fetchone(
    "SELECT * FROM vocabulary WHERE language = %s ORDER BY date_added DESC LIMIT 1",
    (lang,)
)

if word:
    st.metric("Word", word["word"])
    st.write(word["meaning"])
    if word["audio_url"]:
        st.audio(word["audio_url"])
else:
    st.warning(f"No word found for {lang}. Please add some entries.")
