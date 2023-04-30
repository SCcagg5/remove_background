FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier des exigences et installer les dépendances
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier le script de l'API dans le répertoire de travail
COPY api.py .

# Exposer le port 8080 pour l'API
EXPOSE 8080

# Lancer l'application Flask sans Gunicorn
CMD ["python", "api.py"]
