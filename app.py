import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translation Tool", page_icon="🌐", layout="centered")
st.title("🌐 Language Translation Tool")
st.write("Translate text between supported languages.")

LANGUAGES = {
    "English": "en", "Kannada": "kn", "Tamil": "ta", "Hindi": "hi",
    "Malayalam": "ml", "Telugu": "te", "French": "fr", "Spanish": "es",
    "German": "de", "Japanese": "ja", "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar", "Portuguese": "pt"
}

col1, col2 = st.columns(2)
with col1:
    source_name = st.selectbox("Translate from", list(LANGUAGES), index=0)
with col2:
    target_name = st.selectbox("Translate to", list(LANGUAGES), index=1)

text = st.text_area("Enter text", placeholder="Type or paste text here...", height=150)

if st.button("Translate", type="primary", use_container_width=True):
    if not text.strip():
        st.warning("Please enter text to translate.")
    elif source_name == target_name:
        st.info("Choose two different languages.")
    else:
        try:
            translated = GoogleTranslator(source=LANGUAGES[source_name],
                                      target=LANGUAGES[target_name]).translate(text)
            st.subheader("Translation")
            st.text_area("Translated text", value=translated, height=150)
        except Exception as error:
            st.error("Translation could not be completed. Check your internet connection and try again.")
            st.caption(f"Technical detail: {error}")

st.caption("Translations are provided by an online translation service and may need review.")
