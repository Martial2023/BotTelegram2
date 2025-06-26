#!/usr/bin/env bash

# Mettre à jour les paquets et installer les dépendances nécessaires
apt-get update && apt-get install -y ffmpeg espeak-ng

# Installer les dépendances Python
pip install -r requirements.txt

# Vérifier l'installation de eSpeak-ng
if ! command -v espeak-ng &> /dev/null
then
    echo "eSpeak-ng n'est pas installé correctement. Veuillez vérifier les dépendances."
    exit 1
fi

# Vérification des modules Python
python -c "import pyttsx3; print('pyttsx3 installé correctement.')" || {
    echo "Erreur avec pyttsx3. Veuillez vérifier les dépendances Python."
    exit 1
}