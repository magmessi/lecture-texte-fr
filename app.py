import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64

st.set_page_config(page_title="Lecture à voix haute", page_icon="🔊")
st.title("📖 Lecture à voix haute en français")
st.write("Tape un texte en français et écoute-le en audio. Idéal pour ceux qui comprennent mais ne savent pas bien lire.")

# Zone de texte
texte = st.text_area("📝 Écris ici le texte à lire", height=200)

if st.button("🎧 Lecture à voix haute") and texte.strip():
    # Création de l'audio
    tts = gTTS(text=texte, lang="fr")
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)

    # Affichage du lecteur audio
    st.audio(audio_fp, format='audio/mp3')

    # Lien de téléchargement
    b64 = base64.b64encode(audio_fp.read()).decode()
    href = f'<a href="data:audio/mp3;base64,{b64}" download="lecture.mp3">📥 Télécharger l\'audio</a>'
    st.markdown(href, unsafe_allow_html=True)

elif st.button("❌ Effacer"):
    st.experimental_rerun()

