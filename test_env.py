from config import GROQ_API_KEY, MONGO_URI

print("Groq Key Loaded:", GROQ_API_KEY is not None)
print("Mongo URI Loaded:", MONGO_URI is not None)