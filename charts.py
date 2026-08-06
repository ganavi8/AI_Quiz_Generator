import plotly.graph_objects as go



# ---------------- PIE CHART ---------------- #

def create_pie_chart(score, total):


    wrong = total - score


    fig = go.Figure(

        data=[

            go.Pie(

                labels=[
                    "Correct Answers",
                    "Wrong Answers"
                ],


                values=[
                    score,
                    wrong
                ],


                hole=0.4

            )

        ]

    )


    fig.update_layout(

        title="Quiz Accuracy"

    )


    return fig





# ---------------- BAR CHART ---------------- #

def create_bar_chart(results):


    questions = []

    scores = []



    for index, result in enumerate(results):


        questions.append(
            f"Q{index+1}"
        )


        if result["correct"]:

            scores.append(1)

        else:

            scores.append(0)



    fig = go.Figure(

        data=[

            go.Bar(

                x=questions,

                y=scores

            )

        ]

    )


    fig.update_layout(

        title="Question Performance",

        xaxis_title="Questions",

        yaxis_title="Score (1=Correct)"

    )


    return fig