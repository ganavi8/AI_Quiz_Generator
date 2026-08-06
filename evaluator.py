def evaluate_quiz(quiz, answers):

    score = 0

    results = []


    for index, question in enumerate(quiz):


        correct_answer = question["answer"]


        user_answer = answers.get(
            index,
            "Not Answered"
        )


        is_correct = (
            user_answer == correct_answer
        )


        if is_correct:

            score += 1



        results.append(

            {
                "question":
                    question["question"],


                "user_answer":
                    user_answer,


                "correct_answer":
                    correct_answer,


                "correct":
                    is_correct,


                "explanation":
                    question.get(
                        "explanation",
                        "No explanation available"
                    )
            }

        )



    percentage = (
        score / len(quiz)
    ) * 100



    return (
        score,
        percentage,
        results
    )