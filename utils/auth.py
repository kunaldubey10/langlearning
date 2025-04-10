import hashlib
import streamlit as st
from utils.db import fetchone, execute_query

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_user(username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    return fetchone(query, (username, hash_password(password)))

def signup_user(username, password):
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    execute_query(query, (username, hash_password(password)))