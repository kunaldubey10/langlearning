import streamlit as st
from utils.db import fetchone, fetchall

lang = st.selectbox("Choose Language", ["Spanish", "French", "Japanese"])
q = fetchone("SELECT * FROM questions WHERE language = %s ORDER BY RAND() LIMIT 1", (lang,))
options = fetchall("SELECT * FROM options WHERE question_id = %s", (q['id'],))

st.subheader(q["question_text"])
ans = st.radio("Options", [o["option_text"] for o in options])
if st.button("Next"):
    correct = [o for o in options if o["is_correct"] == 1][0]
    if ans == correct["option_text"]:
        st.success("Correct!")
    else:
        st.error(f"Wrong! Correct answer: {correct['option_text']}")