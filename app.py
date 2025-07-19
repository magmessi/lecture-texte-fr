import streamlit as st
from gtts import gTTS

def lire_texte_francais(texte, nom_fichier="audio.mp3"):
    tts = gTTS(text=texte, lang='fr')
    tts.save(nom_fichier)
    return nom_fichier

st.title("📖 Lecture vocale en français")
st.write("Entrez un texte en français pour qu'il soit lu à voix haute.")

texte = st.text_area("Texte à lire", height=200)

if st.button("Lire à voix haute"):
    if texte.strip() == "":
        st.warning("Veuillez entrer un texte.")
    else:
        nom_fichier = lire_texte_francais(texte)
        audio_file = open(nom_fichier, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
