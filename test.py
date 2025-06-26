from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='fr')
    tts.save(filename)
    os.system(f"start {filename}")  # Sur Windows, utilise 'start' pour lire le fichier
    # Sur Linux, remplace par 'xdg-open' ou 'mpg123'

text_to_speech("Bonjour, ceci est un test.")