import pandas as pd


def export_results(results):

    rows = []

    for item in results:

        rows.append({
            "Question": item["question"],
            "Your Answer": item["user_answer"],
            "Correct Answer": item["correct_answer"],
            "Correct": item["correct"]
        })

    return pd.DataFrame(rows)