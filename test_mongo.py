from pymongo import MongoClient
from config import MONGO_URI

try:
    client = MongoClient(MONGO_URI)

    db = client["AIQuizDB"]

    print("MongoDB Connected Successfully ✅")
    print("Database:", db.name)

    print("Collections:")
    print(db.list_collection_names())

except Exception as e:
    print("MongoDB Connection Failed ❌")
    print(e)