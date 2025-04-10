import streamlit as st
from utils.db import fetchall

st.title("Courses")

# Fetch all lessons from the database
courses = fetchall("SELECT * FROM lessons")

# Display them
for course in courses:
    st.subheader(course['lesson_title'])       # ✅ use valid column name
    st.video(course['youtube_url'])            # ✅ display the video
