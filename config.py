import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
