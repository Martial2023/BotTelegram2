FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    ffmpeg \
    espeak-ng \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de l'application dans le conteneur
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Vérifier l'installation de espeak-ng
RUN if ! command -v espeak-ng &> /dev/null; then \
    echo "eSpeak-ng n'est pas installé correctement."; \
    exit 1; \
fi

# Exposer le port utilisé par FastAPI
EXPOSE 8080

# Commande par défaut pour exécuter l'application
CMD ["python", "main.py"]
