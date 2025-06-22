# 🤖 ProlinkeetAI — Assistant Vocal Telegram avec LLaMA et FastAPI

**ProlinkeetAI** est un assistant intelligent disponible via un **bot Telegram** capable de comprendre et de répondre aux **messages texte et vocaux**, en s’appuyant sur le modèle **LLaMA 4 de Meta** via l’API **Groq**. Il utilise **FastAPI** pour exposer un endpoint HTTP (ping/keep-alive), est **déployé sur Render**, et est maintenu en éveil grâce à **UptimeRobot**.

---

## 🚀 Fonctionnalités

- 💬 Réponses instantanées aux messages texte envoyés sur Telegram.
- 🎙️ Transcription de messages vocaux (en français) grâce à Google Speech Recognition.
- 🧠 Génération de réponses contextuelles avec le modèle **LLaMA 4** (Groq API).
- 🔊 Réponses vocales synthétisées avec `pyttsx3` et converties en `.ogg` pour Telegram.
- 🌐 Interface HTTP via **FastAPI** (endpoint `/`) pour vérification de santé.
- ☁️ Déploiement cloud sur **Render.com**, avec maintien actif via **UptimeRobot**.

---

## 📂 Architecture du projet