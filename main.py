from fileinput import filename
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
from dotenv import load_dotenv
from threading import Thread
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from settings import BOT_TOKEN
from utils import transcript_voice_message
from ask_llm import ask_llm
from gtts import gTTS
from pydub import AudioSegment
import re
load_dotenv()


app = FastAPI()


@app.get(
    '/', 
    include_in_schema=False,
    summary="Point d'entrée de l'API",
    description="Renvoie un message de bienvenue pour confirmer que l'API fonctionne correctement.",
    response_description="Message de bienvenue"
)

@app.head(
    '/', 
    include_in_schema=False,
    summary="Point d'entrée de l'API",
    description="Renvoie un message de bienvenue pour confirmer que l'API fonctionne correctement.",
    response_description="Message de bienvenue"
)
async def root():
    return JSONResponse({"message": "Hello World"})

def run_app():
    port = int(os.environ.get('PORT', 8080))
    uvicorn.run(app, host='0.0.0.0', port=port)
    
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut comment puis-je t'aider?")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_Id = str(update.effective_user.id)
    message = update.message.text
    response = ask_llm(message, user_Id)
    
    await update.message.reply_text(response)

async def handle_voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_Id = str(update.effective_user.id)
        messageVoice = update.message.voice
        file = await context.bot.get_file(messageVoice.file_id)
        ogg_path = f'media/audios/{messageVoice.file_id}.ogg'
        wav_path = f'media/audios/{messageVoice.file_id}.wav'
        
        await file.download_to_drive(ogg_path)
        transcript = transcript_voice_message(ogg_path, wav_path, update)
        
        response = ask_llm(transcript, user_Id)

        await update.message.reply_text(response)
        response = re.sub(r'[\*\_`]', '', response.replace('\n', ' '))
        tts = gTTS(text=response, lang='fr')
        tts.save(f'media/bot/mp3/{messageVoice.file_id}.mp3')
        sound = AudioSegment.from_mp3(f'media/bot/mp3/{messageVoice.file_id}.mp3')
        sound.export(f'media/bot/ogg/{messageVoice.file_id}.ogg', format="ogg")

        await context.bot.send_voice(chat_id=update.effective_chat.id, voice=open(f'media/bot/ogg/{messageVoice.file_id}.ogg', 'rb'))

        os.remove(f'media/bot/mp3/{messageVoice.file_id}.mp3')
        os.remove(f'media/bot/ogg/{messageVoice.file_id}.ogg')
        os.remove(ogg_path)
        os.remove(wav_path)
    except Exception as e:
        print(e)

  
def main():
    print("Bot en cours...")
    appTelegram = ApplicationBuilder().token(BOT_TOKEN).build()
    appTelegram.add_handler(CommandHandler("start", start))
    appTelegram.add_handler(MessageHandler(filters.TEXT, handle_message))
    appTelegram.add_handler(MessageHandler(filters.VOICE, handle_voice_message))
    appTelegram.run_polling()
    
if __name__ == '__main__':
    fastapi_thread = Thread(target=run_app, daemon=True)
    fastapi_thread.start()
    main()