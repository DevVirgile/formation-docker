# 💪 Exercices & TP Final – Formation Docker 2 Jours

---

## 🔧 Exercice 1 – Découverte de Docker

**Objectif :** Manipuler des conteneurs simples

1. Lancer un conteneur Alpine :

   ```bash
   docker run -it alpine sh
   ```
2. Tester quelques commandes : `ls`, `ping`, `apk add curl`
3. Quitter, relister les conteneurs : `docker ps -a`
4. Supprimer le conteneur : `docker rm <id>`

---

## 🔧 Exercice 2 – Créer une image personnalisée

**Objectif :** Créer une image à partir d’un `Dockerfile`

Structure :

* `app.py`
* `requirements.txt`
* `Dockerfile`
* `.dockerignore`

Contenu `app.py` :

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Docker!"

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

Contenu `requirements.txt` :

```
flask==2.3.3
```

Contenu `Dockerfile` :

```dockerfile
FROM python:3.10-slim
WORKDIR /app

# Copie ciblée des fichiers nécessaires
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./

ENTRYPOINT ["python"]
CMD ["app.py"]
```

Contenu `.dockerignore` :

```
__pycache__/
*.pyc
*.pyo
*.pyd
venv/
.env
.git/
.dockerignore
Dockerfile
```

Build + run :

```bash
docker build -t mon-serveur .
docker run -p 5000:5000 mon-serveur
```

---

## 🔧 Exercice 3 – Volumes et données

**Objectif :** Utiliser les volumes Docker

1. Créer un volume :

```bash
docker volume create pgdata
```

2. Lancer un conteneur PostgreSQL avec le volume :

```bash
docker run -d \
  --name mon-postgres \
  -e POSTGRES_PASSWORD=secret \
  -v pgdata:/var/lib/postgresql/data \
  postgres
```

3. Arrêter puis redémarrer le conteneur, vérifier la persistance

---

## 🔧 Exercice 4 – Réseaux Docker

**Objectif :** Créer un réseau et faire dialoguer deux conteneurs

1. Créer un réseau :

```bash
docker network create mon-reseau
```

2. Lancer PostgreSQL sur ce réseau
3. Lancer un conteneur `alpine` ou `pgadmin` dans le même réseau
4. Tester la connexion

---

## 🔧 Exercice 5 – Stack Docker Compose

**Objectif :** Créer une stack `web` + `db`

Contenu `docker-compose.yml` :

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: secret
```

Commandes :

```bash
docker compose up
docker compose down
```

---

## 🔧 Exercice 6 – Optimisation d’image

**Objectif :** Comparer les tailles d’image, améliorer le `Dockerfile`

1. Comparer les images `python:3.10`, `slim`, `alpine`
2. Ajouter un fichier `.dockerignore`
3. Utiliser un multi-stage build (optionnel)

---

# 🛠️ TP Final – Application Full Stack Dockerisée

## 📃 Cahier des charges

* Backend : API Flask avec PostgreSQL
* Frontend : HTML statique
* Proxy : Nginx
* Orchestration via Docker Compose
* Persistance des données
* Variables via fichier `.env`

## 📁 Structure attendue

```
$1│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
```

Contenu `backend/Dockerfile` :

```dockerfile
FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./

ENTRYPOINT ["python"]
CMD ["app.py"]
```

Contenu `backend/requirements.txt` :

```
flask==2.3.3
psycopg2-binary==2.9.9
```

Contenu `frontend/index.html` :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>TP Docker</title>
</head>
<body>
    <h1>Bienvenue sur mon application Dockerisée</h1>
    <p id="message">Chargement...</p>

    <script>
        fetch('/api/messages')
            .then(response => response.json())
            .then(data => {
                document.getElementById('message').textContent = data.message || data.error;
            })
            .catch(error => {
                document.getElementById('message').textContent = "Erreur : " + error;
            });
    </script>
</body>
</html>
```

Contenu `backend/.dockerignore` :

```
__pycache__/
*.pyc
*.pyo
*.pyd
venv/
.env
.git/
.dockerignore
```

## 📄 Étapes

Contenu `nginx/default.conf` :

```nginx
server {
    listen 80;

    location /api/ {
        proxy_pass http://backend:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
}
```

Contenu `backend/app.py` :

```python
from flask import Flask, jsonify
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

@app.route('/api/messages')
def get_messages():
    try:
        db_url = os.environ.get('DATABASE_URL')
        conn = psycopg2.connect(db_url, cursor_factory=RealDictCursor)
        cur = conn.cursor()
        cur.execute("SELECT 'Hello from PostgreSQL!' AS message;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

1. Implémenter l’API Flask connectée à PostgreSQL
2. Servir une page HTML avec Nginx
3. Router `/api` vers Flask et `/` vers le HTML
4. Configurer `docker-compose.yml` avec les 3 services
5. Lancer la stack, vérifier le bon fonctionnement

Contenu `.env` :

```
POSTGRES_DB=messagesdb
POSTGRES_USER=user
POSTGRES_PASSWORD=password
DATABASE_URL=postgresql://user:password@db:5432/messagesdb
FLASK_PORT=5000
```

## ✅ Critères de validation

* Accès via `http://localhost`
* API fonctionnelle avec PostgreSQL
* Frontend servi via Nginx
* Stack démarrable avec une seule commande
* Utilisation de volumes et variables d’environnement

## 🧠 Annexe – Différences entre ENTRYPOINT et CMD

| Élément       | ENTRYPOINT                                | CMD                                   |
| ------------- | ----------------------------------------- | ------------------------------------- |
| Rôle          | Définit la commande principale            | Fournit les **arguments par défaut**  |
| Priorité      | Prioritaire sur CMD                       | S'efface si des arguments sont passés |
| Remplaçable ? | ✅ Oui, via `--entrypoint`                 | ✅ Oui, via arguments `docker run`     |
| Combine ?     | ✅ Oui, ENTRYPOINT + CMD = commande + args | ❌ CMD seul est toute la commande      |
| Cas d’usage   | Image avec un script ou binaire principal | Fournir des paramètres modifiables    |

### 🔍 Exemple combiné

```dockerfile
ENTRYPOINT ["echo"]
CMD ["Bonjour"]
```

* `docker run mon-image` ➞ `echo Bonjour`
* `docker run mon-image Salut !` ➞ `echo Salut !`
* `docker run --entrypoint ls mon-image /` ➞ `ls /`

## 📦 Exemple – Dockerfile avec `ARG` et `--name`

Contenu `Dockerfile` :

```dockerfile
FROM alpine:3.20

# Déclaration d'une variable de build
ARG NOM_FICHIER=default.txt

# Utilisation de cette variable dans une commande
RUN echo "Bonjour depuis Dockerfile avec ARG !" > /$NOM_FICHIER

CMD ["cat", "/default.txt"]
```

### 🛠️ Build et run

```bash
docker build -t fichier-custom --build-arg NOM_FICHIER=bonjour.txt .
docker run --name mon-conteneur fichier-custom
```

* `ARG` permet de passer des variables **au moment du build**.
* `--name` permet de nommer le conteneur au moment du **`docker run`**.

## 🏑 Bonus (optionnel)

* Interface JS connectée à l’API
* CI/CD (GitHub Actions)
