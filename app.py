import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="FAQ Chatbot", page_icon="💬", layout="centered")
st.title("💬 FAQ Chatbot")
st.write("Ask a question about Python basics. The bot matches your question with its FAQ list.")

FAQS = [
    ("What is Python?", "Python is a beginner-friendly, high-level programming language known for readable syntax."),
    ("What is a variable?", "A variable is a named place used to store a value in a program."),
    ("What is a list?", "A list is an ordered collection that can store multiple items and can be changed."),
    ("What is a function?", "A function is a reusable block of code that performs a specific task"),
    ("What is a loop?", "A loop repeats a set of instructions while a condition is met or for each item in a sequence"),
    ("What is a dictionary?", "A dictionary stores data as key-value pairs"),
    ("What is an if statement?", "An if statement runs code only when its condition is true"),
    ("How do I print in Python?", "Use print(), for example: print('Hello')"),
    ("What is a string?", "A string is text enclosed in quotation marks"),
    ("What is an integer?", "An integer is a whole number, such as 5 or -2"),
    ("How do I install Python?", "Download Python from python.org and follow the installation steps for your operating system"),
    ("What is AI?", "Artificial Intelligence is a field that develops computer systems able to perform tasks that usually require human-like intelligence")
]

questions = [q for q, a in FAQS]
answers = [a for q, a in FAQS]
vectorizer = TfidfVectorizer()
faq_matrix = vectorizer.fit_transform(questions)

if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_question = st.chat_input("Ask a question...")
if user_question:
    st.session_state.history.append({"role": "user", "content": user_question})
    question_vector = vectorizer.transform([user_question])
    scores = cosine_similarity(question_vector, faq_matrix)[0]
    best_index = scores.argmax()
    confidence = float(scores[best_index])

    if confidence < 0.50:
        response = "Sorry, I don't have a close FAQ match. Try asking about Python basics."
    else:
        response = answers[best_index]

    st.session_state.history.append({"role": "assistant", "content": response})
    st.rerun()

if st.button("Clear conversation"):
    st.session_state.history = []
    st.rerun()

st.caption("This demo uses TF-IDF and cosine similarity to match questions. It is not a generative AI model.")
