import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔐Password Strength Checker")
st.markdown("""
## welcome to the ultimate password strength checker!👋
use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
            we will give you helpful tips to create a **Strong Password** 🔒""")

password = st.text_input("Enter your password:", type="password")

feedback = []

score = 0

if password:
    # Check password length
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("Password should be at least 8 characters long.")