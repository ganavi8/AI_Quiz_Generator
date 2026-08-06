import json
from datetime import datetime


def save_history(topic, score, percentage):

    history = {
        "topic": topic,
        "score": score,
        "percentage": percentage,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    with open("history/history.json", "a") as file:
        file.write(json.dumps(history) + "\n")