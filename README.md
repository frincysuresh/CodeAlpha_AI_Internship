# CodeAlpha FAQ Chatbot

A lightweight FAQ chatbot for Python basics. It compares the user's question with prepared FAQs using TF-IDF and cosine similarity, then returns the closest answer.

## Features
- Chat-style interface
- FAQ dataset
- Text vectorization (TF-IDF)
- Similarity matching (cosine similarity)
- Unknown-question fallback
- Clear chat button

## Setup
1. Install Python 3.10+.
2. Open terminal in this folder.
3. Create environment (optional): `python -m venv .venv`
4. Activate it:
   - Windows: `.venv\\Scripts\\activate`
   - macOS/Linux: `source .venv/bin/activate`
5. Install packages: `pip install -r requirements.txt`
6. Run: `streamlit run app.py`

## Test checklist
- Ask: "What is Python?"
- Ask: "Explain loops"
- Ask an unrelated question and check fallback
- Clear conversation and confirm messages reset

## Internship repository name
`CodeAlpha_FAQChatbot`
