import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64

st.set_page_config(page_title="Lecture à voix haute", page_icon="🔊")
st.title("📖 Lecture à voix haute en français")
st.write("Écris un texte en français pour l'écouter en audio. Idéal pour ceux qui comprennent mais ne savent pas lire.")

# Zone de texte
texte = st.text_area("📝 Ton texte ici", height=200)

if st.button("🎧 Lecture à voix haute") and texte.strip():
    # Création de l'audio avec gTTS
    tts = gTTS(text=texte, lang="fr")

    # Création d'un buffer audio pour la lecture
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)

    # Pour la lecture
    st.audio(audio_buffer, format='audio/mp3')

    # On crée une deuxième copie du buffer pour le téléchargement
    download_buffer = BytesIO()
    tts.write_to_fp(download_buffer)
    download_buffer.seek(0)
    b64 = base64.b64encode(download_buffer.read()).decode()
    href = f'<a href="data:audio/mp3;base64,{b64}" download="lecture.mp3">📥 Télécharger l\'audio</a>'
    st.markdown(href, unsafe_allow_html=True)

elif st.button("❌ Effacer"):
    st.experimental_rerun()


