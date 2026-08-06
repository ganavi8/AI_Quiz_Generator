import streamlit as st

from quiz_generator import generate_quiz
from evaluator import evaluate_quiz
from file_reader import read_pdf, read_txt
from charts import create_pie_chart, create_bar_chart

from database import quiz_collection

from datetime import datetime



# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Quiz Generator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)



# ---------------- LOAD CSS ---------------- #

def load_css():

    try:

        with open("assets/style.css") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except:

        pass



load_css()



# ---------------- SESSION STATE ---------------- #

if "quiz" not in st.session_state:

    st.session_state.quiz = None


if "current_question" not in st.session_state:

    st.session_state.current_question = 0


if "answers" not in st.session_state:

    st.session_state.answers = {}


if "submitted" not in st.session_state:

    st.session_state.submitted = False




# ---------------- SIDEBAR ---------------- #

with st.sidebar:


    st.markdown(
    """
    <h1 style='text-align:center'>
    ⚙️ Quiz AI
    </h1>
    """,
    unsafe_allow_html=True
    )


    difficulty = st.selectbox(

        "🎯 Difficulty",

        [
            "Easy",
            "Medium",
            "Hard"
        ]

    )



    quiz_type = st.selectbox(

        "📝 Quiz Type",

        [
            "Multiple Choice"
        ]

    )



    num_questions = st.slider(

        "🔢 Number of Questions",

        5,

        30,

        10

    )



    st.divider()



    st.markdown(
    """
    ### 🧠 AI Quiz Generator

    ✨ Features:

    🚀 AI Question Generation

    📄 PDF Quiz Creation

    📝 Notes Based Quiz

    📊 Performance Analytics

    🏆 Learning Progress

    """
    )




# ---------------- PREMIUM HEADER ---------------- #

st.markdown(

"""
<div style="
text-align:center;
padding:25px;
">


<h1>
🧠 AI Quiz Generator
</h1>


<h3>
🚀 Transform Learning With Artificial Intelligence
</h3>


<p>
Create smart quizzes from topics, notes and documents
</p>


</div>

""",

unsafe_allow_html=True

)




# ---------------- FEATURE CARDS ---------------- #

c1,c2,c3 = st.columns(3)



with c1:

    st.info(
    """
    📚 Smart Questions

    AI creates meaningful
    questions from your content.
    """
    )



with c2:

    st.info(
    """
    🤖 AI Powered

    Powered by Groq
    Llama AI model.
    """
    )



with c3:

    st.info(
    """
    📊 Analytics

    Track score and
    learning improvement.
    """
    )



st.divider()




# ---------------- INPUT SECTION ---------------- #

st.subheader(
    "✨ Create Your Quiz"
)



tab1,tab2 = st.tabs(

[
    "📚 Topic",
    "📝 Notes"
]

)




with tab1:


    topic = st.text_input(

        "Enter Topic",

        placeholder="Example: Deep Learning"

    )




with tab2:


    notes = st.text_area(

        "Paste Notes",

        height=220

    )





uploaded_file = st.file_uploader(

    "📄 Upload PDF or TXT",

    type=[

        "pdf",

        "txt"

    ]

)



st.divider()




# ---------------- BUTTONS ---------------- #

col1,col2,col3 = st.columns(3)



with col1:


    generate = st.button(

        "🚀 Generate Quiz",

        use_container_width=True

    )



with col2:


    clear = st.button(

        "🗑 Clear",

        use_container_width=True

    )



with col3:


    new_quiz = st.button(

        "🔄 New Quiz",

        use_container_width=True

    )





# ---------------- CLEAR ---------------- #

if clear:


    st.session_state.quiz = None

    st.session_state.answers = {}

    st.session_state.current_question = 0

    st.session_state.submitted = False


    st.rerun()





# ---------------- NEW QUIZ ---------------- #

if new_quiz:


    st.session_state.quiz = None

    st.session_state.answers = {}

    st.session_state.current_question = 0

    st.session_state.submitted = False


    st.rerun()





# ---------------- GENERATE QUIZ ---------------- #

if generate:


    if topic == "" and notes == "" and uploaded_file is None:


        st.warning(
            "Please enter topic, notes or upload file"
        )

        st.stop()



    if topic:


        content = topic



    elif notes:


        content = notes



    else:


        if uploaded_file.name.endswith(".pdf"):


            content = read_pdf(uploaded_file)


        else:


            content = read_txt(uploaded_file)





    with st.spinner(

        "🤖 AI is creating your quiz..."

    ):


        try:


            quiz = generate_quiz(

                topic=content,

                difficulty=difficulty,

                num_questions=num_questions,

                quiz_type=quiz_type

            )



            st.session_state.quiz = quiz

            st.session_state.current_question = 0

            st.session_state.answers = {}

            st.session_state.submitted = False




            quiz_collection.insert_one(

                {

                "type":"quiz",

                "topic":content,

                "difficulty":difficulty,

                "questions":quiz,

                "created_at":datetime.now()

                }

            )



            st.success(
                "✅ Quiz Generated Successfully!"
            )



        except Exception as e:


            st.error(
                str(e)
            )
            # ---------------- INTERACTIVE QUIZ ---------------- #

if st.session_state.quiz and not st.session_state.submitted:


    quiz = st.session_state.quiz

    total = len(quiz)

    current = st.session_state.current_question

    question = quiz[current]



    st.progress(
        (current + 1) / total
    )



    st.markdown(
    f"""
    <h2>
    📝 Question {current+1} / {total}
    </h2>
    """,
    unsafe_allow_html=True
    )



    st.write(
        question["question"]
    )



    selected = st.radio(

        "Choose your answer",

        question["options"],

        index=None,

        key=f"answer_{current}"

    )



    if selected:


        st.session_state.answers[current] = selected



    st.divider()



    c1,c2,c3 = st.columns(3)



    with c1:


        if current > 0:


            if st.button(
                "⬅ Previous",
                use_container_width=True
            ):


                st.session_state.current_question -= 1

                st.rerun()




    with c2:


        st.write(
            f"Question {current+1}/{total}"
        )




    with c3:


        if current < total-1:


            if st.button(
                "Next ➡",
                use_container_width=True
            ):


                st.session_state.current_question += 1

                st.rerun()



        else:


            if st.button(
                "Submit Quiz ✅",
                use_container_width=True
            ):


                if len(st.session_state.answers) != total:


                    st.warning(
                        "Answer all questions before submitting"
                    )


                else:


                    st.session_state.submitted = True

                    st.rerun()





# ---------------- RESULTS ---------------- #

if st.session_state.submitted:


    score, percentage, results = evaluate_quiz(

        st.session_state.quiz,

        st.session_state.answers

    )



    quiz_collection.insert_one(

        {

        "type":"result",

        "score":score,

        "percentage":percentage,

        "total_questions":
            len(st.session_state.quiz),

        "results":results,

        "completed_at":
            datetime.now()

        }

    )



    st.balloons()



    st.markdown(

    """

    <h1 style="text-align:center">

    🎉 Quiz Completed

    </h1>

    """,

    unsafe_allow_html=True

    )



    c1,c2,c3 = st.columns(3)



    with c1:


        st.metric(

            "🏆 Score",

            f"{score}/{len(st.session_state.quiz)}"

        )



    with c2:


        st.metric(

            "📈 Percentage",

            f"{percentage:.2f}%"

        )



    with c3:


        if percentage >= 90:

            level="🔥 Expert"


        elif percentage >=75:

            level="⭐ Advanced"


        elif percentage >=50:

            level="👍 Intermediate"


        else:

            level="📚 Beginner"



        st.metric(

            "Level",

            level

        )





    st.divider()



    # ---------------- ANALYTICS ---------------- #


    st.header(
        "📊 AI Performance Analytics"
    )



    pie = create_pie_chart(

        score,

        len(st.session_state.quiz)

    )


    st.plotly_chart(

        pie,

        use_container_width=True

    )




    bar = create_bar_chart(

        results

    )


    st.plotly_chart(

        bar,

        use_container_width=True

    )





    # ---------------- REVIEW ---------------- #

    st.header(
        "📝 Answer Review"
    )



    for i,result in enumerate(results):


        with st.expander(
            f"Question {i+1}"
        ):


            st.write(

                result["question"]

            )


            st.write(

                "Your Answer:",

                result["user_answer"]

            )


            st.write(

                "Correct Answer:",

                result["correct_answer"]

            )



            if result["correct"]:


                st.success(
                    "✅ Correct"
                )


            else:


                st.error(
                    "❌ Incorrect"
                )


            st.info(

                result["explanation"]

            )







# ---------------- QUIZ HISTORY ---------------- #

st.sidebar.divider()



st.sidebar.subheader(
    "📚 Previous Attempts"
)



if st.sidebar.button(
    "View History"
):


    history = list(

        quiz_collection.find()

        .sort(

            "completed_at",

            -1

        )

        .limit(10)

    )



    if history:


        for item in history:


            if item.get("type")=="result":


                st.sidebar.success(

                    f"""
🏆 Score:
{item['score']}/{item['total_questions']}

📈 Percentage:
{item['percentage']:.2f}%

"""
                )


    else:


        st.sidebar.info(
            "No quiz history available"
        )







# ---------------- RESET ---------------- #

if st.session_state.submitted:


    if st.button(
        "🔄 Create New Quiz",
        use_container_width=True
    ):


        st.session_state.quiz=None

        st.session_state.answers={}

        st.session_state.current_question=0

        st.session_state.submitted=False


        st.rerun()






# ---------------- FOOTER ---------------- #

st.markdown("---")


st.markdown(

"""
<div style="
text-align:center;
">


<h3>
🧠 AI Quiz Generator
</h3>


<p>
Built with Python • Streamlit • Groq AI • MongoDB
</p>


<p>
❤️ Smart Learning Powered by AI
</p>


</div>
""",

unsafe_allow_html=True

)