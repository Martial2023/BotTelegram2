# 🤖 ProlinkeetAI — Assistant Personnel Telegram avec LLaMA et FastAPI

**ProlinkeetAI** est un assistant personnel numérique conçu pour offrir une expérience utilisateur fluide et intelligente via un **bot Telegram**. Ce projet exploite des technologies avancées telles que le modèle **LLaMA 4** de Meta, l’API **Groq**, et **FastAPI** pour fournir des réponses contextuelles précises et des interactions vocales naturelles. Le code est hébergé sur **Render**, garantissant une disponibilité continue grâce à **UptimeRobot**.

---

## 🚀 Fonctionnalités

- **💬 Réponses instantanées** : Répond aux messages texte envoyés sur Telegram avec des réponses contextuelles et pertinentes.
- **🎙️ Transcription vocale** : Convertit les messages vocaux en texte (en français) grâce à Google Speech Recognition.
- **🧠 Intelligence contextuelle** : Génère des réponses basées sur le modèle **LLaMA 4** via l’API Groq.
- **🔊 Synthèse vocale** : Produit des réponses vocales synthétisées avec `gTTS`, converties en `.mp3` pour une compatibilité avec Telegram.
- **🌐 Endpoint HTTP** : Fournit une interface HTTP via **FastAPI** pour vérifier la santé de l’application.
- **☁️ Déploiement cloud** : Hébergé sur **Render.com**, avec maintien actif via **UptimeRobot** qui effectue un `HEAD` sur l’API toutes les 5 minutes pour éviter l’endormissement.

---

## 📂 Architecture du Projet

### Structure des Dossiers

- **`main.py`** : Point d’entrée principal du bot Telegram et du serveur FastAPI.
- **`ask_llm.py`** : Gestion des interactions avec le modèle LLaMA et historique des conversations.
- **`utils.py`** : Fonctions utilitaires pour la transcription vocale et la gestion des fichiers.
- **`settings.py`** : Configuration des variables d’environnement et des paramètres système.
- **`build.sh`** : Script d’installation des dépendances et des outils nécessaires.
- **`media/`** : Répertoire pour les fichiers audio (ogg et mp3).
- **`data/`** : Contient les historiques des conversations.

---

## 🛠️ Installation et Déploiement

### Prérequis

- **Python 3.10+**
- **Render.com** pour l’hébergement
- **UptimeRobot** pour la surveillance

### Étapes d’Installation

1. Clonez le dépôt :
   ```bash
   git clone <URL_du_dépôt>
   cd TelegramChatLLM
   ```

2. Installez les dépendances :
   ```bash
   bash build.sh
   ```

3. Configurez les variables d’environnement :
   - Créez un fichier `.env` à la racine.
   - Ajoutez les clés nécessaires :
     ```env
     BOT_TOKEN=<Votre_Token_Telegram>
     GROQ_API_KEY=<Votre_API_Key_Groq>
     ```

4. Lancez l’application localement :
   ```bash
   python main.py
   ```

5. Déployez sur Render.com en suivant les instructions de leur documentation.

---

## 📖 Fonctionnement

### Interaction avec Telegram

- **Commandes** :
  - `/start` : Démarre une conversation avec le bot.
  - Messages texte : Réponses instantanées basées sur le contexte.
  - Messages vocaux : Transcription et réponse vocale.

### Endpoint HTTP

- **`GET /`** : Vérifie la santé de l’application.
- **UptimeRobot** : Effectue un `HEAD` toutes les 5 minutes pour maintenir l’API active.

---

## 🧑‍💻 Contributions

Les contributions sont les bienvenues ! Veuillez soumettre vos pull requests ou ouvrir des issues pour signaler des bugs ou proposer des améliorations.

---

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.