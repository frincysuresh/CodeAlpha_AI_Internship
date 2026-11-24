import streamlit as st
import requests

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
            url = "https://api.mymemory.translated.net/get"

            response = requests.get(
                url,
                params={
                    "q": text,
                    "langpair": f"{languages[source]}|{languages[target]}"
                },
                timeout=20
            )

            response.raise_for_status()
            data = response.json()

            if data.get("responseStatus") == 200:
                st.subheader("Translation")
                st.success(data["responseData"]["translatedText"])
            else:
                st.error("Translation service is temporarily unavailable.")

        except requests.exceptions.RequestException:
            st.error("Unable to connect to the translation server. Please try again.")

        except (KeyError, ValueError):
            st.error("Unable to process the translation. Please try again.")

st.caption("Powered by MyMemory Translation API.")