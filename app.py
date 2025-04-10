import streamlit as st
from streamlit_option_menu import option_menu
import os

st.set_page_config(page_title="Language Learning Portal", layout="wide")
with open("static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Login", "Courses", "Quizzes", "Vocabulary", "Translate"],
        icons=["house", "person", "book", "patch-question", "lightbulb", "globe"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    import pages.Home
elif selected == "Login":
    import pages. Login
elif selected == "Courses":
    import pages.Courses
elif selected == "Quizzes":
    import pages.Quizzes
elif selected == "Vocabulary":
    import pages.Vocabulary
elif selected == "Translate":
    import pages.Translate
