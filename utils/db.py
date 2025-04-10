import mysql.connector
import streamlit as st

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="kunaldubeysql@10",
        database="language_portal"
    )

def fetchone(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.close()
    return result

def fetchall(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

def execute_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()