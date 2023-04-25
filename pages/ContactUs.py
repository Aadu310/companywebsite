import streamlit as st
import pandas
from sendemail import sendemail


st.header("Contact Us")

with st.form(key="send_email forms"):
    user_email = st.text_input("Your email address")
    df = pandas.read_csv("topics.csv")
    topics = st.selectbox('What do you want to discuss?',df["topic"])
    user_message = st.text_area("Enter your Text")
    message = f'''\
Subject: New email received from {user_email}

From: {user_email}
Topic: {topics}
{user_message}
'''
    button = st.form_submit_button("Submit")
    if button:
        sendemail(message)
        st.info("Email is sent successfully")
