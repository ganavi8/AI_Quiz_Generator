from pymongo import MongoClient


client = MongoClient(
    "mongodb://localhost:27017/"
)


db = client["AIQuizDB"]


quiz_collection = db["quiz_history"]