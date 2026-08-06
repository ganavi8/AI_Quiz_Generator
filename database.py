import streamlit as st
from pymongo import MongoClient

client = MongoClient(st.secrets["MONGO_URI"])

db = client["AIQuizDB"]

quiz_collection = db["quiz_history"]