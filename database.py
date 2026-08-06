from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["AIQuizDB"]

quiz_collection = db["quiz_history"]