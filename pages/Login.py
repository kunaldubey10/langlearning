import streamlit as st
from utils.auth import login_user, signup_user

st.title("Login / Signup")
option = st.radio("Select Option", ["Login", "Sign Up"])

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button(option):
    if option == "Login":
        user = login_user(username, password)
        if user:
            st.session_state["user"] = user["username"]
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials")
    else:
        signup_user(username, password)
        st.success("Account created successfully!")
