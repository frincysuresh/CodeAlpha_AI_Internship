import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍"
)

st.title("🌍 Language Translation Tool")
st.write("Translate text from one language to another.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

source = st.selectbox("Translate from", list(languages.keys()))
target = st.selectbox(
    "Translate to",
    list(languages.keys()),
    index=1
)

text = st.text_area("Enter text to translate")

if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text.")
    elif source == target:
        st.warning("Please select two different languages.")
    else:
        try:
            result = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.subheader("Translation")
            st.success(result)

        except Exception as e:
            st.error("Translation failed. Please try again.")

st.caption("Powered by Google Translate through deep-translator.")
