import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")

# Use Streamlit secrets if .env is not available
if not GROQ_API_KEY:
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", None)

if not MONGO_URI:
    MONGO_URI = st.secrets.get("MONGO_URI", None)