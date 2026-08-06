from pymongo import MongoClient

uri = "mongodb+srv://ganavi:bF0uL1Ju2UcD9art@cluster0.h9imcey.mongodb.net/AIQuizDB?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(uri)

    # Test the connection
    client.admin.command("ping")

    print("✅ MongoDB Connected Successfully!")

    db = client["AIQuizDB"]

    collection = db["quiz_history"]

    result = collection.insert_one(
        {
            "test": "Connection Successful"
        }
    )

    print("✅ Data Inserted Successfully")
    print("Inserted ID:", result.inserted_id)

except Exception as e:
    print("❌ Connection Failed")
    print(e)