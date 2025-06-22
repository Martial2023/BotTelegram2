import speech_recognition as sr
from telegram import Update
from pydub import AudioSegment
from groq import Groq
import os
import json
from settings import HISTORY_FILE, MODEL_NAME

client = Groq()
recognizer = sr.Recognizer()

def transcript_voice_message(ogg_path: str, wav_path: str, update: Update):
    """Transcribe a voice message from a .wav file."""
    audio = AudioSegment.from_file(ogg_path, format='ogg')
    audio = audio.set_channels(1).set_frame_rate(16000)  # nécessaire pour Google Speech
    audio.export(wav_path, format='wav')
    
    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio, language='fr-FR')
            return text
        except sr.UnknownValueError:
            update.message.reply_text("Je n'ai pas pu comprendre le message vocal.")
        except sr.RequestError as e:
            update.message.reply_text(f"Erreur avec le service de reconnaissance vocale : {e}")


def load_histories():
    if not os.path.exists(HISTORY_FILE):
        return {}
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_histories(histories):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(histories, f, ensure_ascii=False, indent=2)
        


def ask_llama(messages):
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=messages,
        temperature=0.7,
        max_completion_tokens=1024,
        
        top_p=1,
        stream=False,  # Pour l'intégration Telegram, mieux vaut éviter stream=True
    )
    return completion.choices[0].message.content