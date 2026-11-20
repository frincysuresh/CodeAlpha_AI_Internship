# CodeAlpha Language Translation Tool

A simple Streamlit translation app with language selection and text translation.

## Features
- Text input
- Source and target language dropdowns
- Translate button
- Result display
- Error handling

## Setup
1. Install Python 3.10+.
2. Open terminal in this project folder.
3. Create an environment (optional but recommended): `python -m venv .venv`
4. Activate it:
   - Windows: `.venv\\Scripts\\activate`
   - macOS/Linux: `source .venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run: `streamlit run app.py`

Internet connection is required for the translation service. This project uses `deep-translator` with Google Translate service; it is not an official Google Cloud API integration.

## Test checklist
- Translate a short English sentence to Kannada.
- Change source/target languages.
- Try empty input and confirm validation.
- Confirm the app handles network/service errors.

## Internship repository name
`CodeAlpha_LanguageTranslationTool`
