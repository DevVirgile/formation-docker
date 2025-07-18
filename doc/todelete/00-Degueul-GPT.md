# 🐳 Formation Docker – 2 Jours

## 🎯 Objectifs

À l’issue de cette formation, les participants sauront :

- Comprendre l’architecture et les composants de Docker
- Créer, exécuter et gérer des conteneurs Docker
- Construire des images avec `Dockerfile`
- Orchestrer plusieurs conteneurs avec Docker Compose
- Appliquer les bonnes pratiques de conteneurisation
- Réaliser un projet complet conteneurisé

---

## 🧑‍🏫 Public cible

- Développeurs
- Administrateurs système
- DevOps
- Toute personne souhaitant apprendre Docker

## 🧰 Prérequis

- Connaissances de base en ligne de commande
- Notions de développement logiciel (ex. : Python, Node, etc.)

---

## 📅 Jour 1 – Fondamentaux Docker (7h)

### 🕘 9h00 – 9h30 : Introduction à Docker

- Présentation de la formation
- Historique de la conteneurisation
- VM vs conteneurs
- Architecture de Docker (CLI, Daemon, Hub, Registry)

---

### 🕘 9h30 – 10h45 : Premiers pas avec Docker

- Commandes de base : `docker run`, `ps`, `stop`, `rm`, `exec`, `logs`
- Docker Hub
- Démos : conteneurs `alpine`, `nginx`, `ubuntu`

🛠️ **Exercice 1** : Lancer et manipuler des conteneurs simples

---

### ☕ 10h45 – 11h00 : Pause

---

### 🕚 11h00 – 12h30 : Création d’images Docker

- Différence image vs conteneur
- Structure d’un `Dockerfile`
- Instructions clés : `FROM`, `COPY`, `RUN`, `CMD`, `EXPOSE`, `ENV`
- Caching et optimisation

🛠️ **Exercice 2** : Créer une image Docker d’un serveur Flask simple

---

### 🍽️ 12h30 – 13h30 : Pause déjeuner

---

### 🕐 13h30 – 15h00 : Gestion des volumes et réseaux

- Volumes : bind mount, volume nommé
- Réseaux : bridge, host, overlay (vue d'ensemble)
- Communication inter-conteneurs

🛠️ **Exercice 3** : Persistance de données + communication entre 2 conteneurs

---

### ☕ 15h00 – 15h15 : Pause

---

### 🕒 15h15 – 17h00 : Docker Compose

- Introduction à l’orchestration multi-conteneurs
- Structure du fichier `docker-compose.yml`
- Commandes utiles : `up`, `down`, `logs`, `build`, `exec`
- Mise en place d'une stack simple

🛠️ **Exercice 4** : Déploiement d’une stack Flask + PostgreSQL

---

## 📅 Jour 2 – Approfondissement & TP (7h)

### 🕘 9h00 – 10h30 : Gestion avancée et bonnes pratiques

- Inspection (`inspect`, `exec`)
- Nettoyage (`prune`, `rmi`, `volume rm`)
- Optimisation des images (`.dockerignore`, multi-stage build)
- Variables d’environnement et secrets

🛠️ **Mini-TP** : Optimiser une image trop volumineuse

---

### ☕ 10h30 – 10h45 : Pause

---

### 🕥 10h45 – 12h30 : Sécurité, CI/CD & registries

- Utilisateur root vs non-root
- Introduction à la sécurité des images (Trivy, Docker Scout)
- Registres Docker : Docker Hub, GitHub Container Registry, registry local
- Intégration dans une chaîne CI/CD (ex. GitHub Actions, GitLab CI)

💡 **Démonstration** : Build & push vers Docker Hub

---

### 🍽️ 12h30 – 13h30 : Pause déjeuner

---

## 🛠️ 13h30 – 17h00 : TP Final – Projet Docker complet

### 🔧 Objectif :

Construire et déployer une application complète avec Docker Compose, incluant frontend, backend, et base de données.

### 📦 Contenu du projet :

- Application web Flask (ou Node.js) avec API
- Base de données PostgreSQL
- Frontend statique servi via Nginx
- Communication entre services
- Gestion de la persistance via volumes
- Configuration par variables d’environnement

### 🧩 Étapes :

1. Écrire les `Dockerfile`
2. Créer le fichier `docker-compose.yml`
3. Monter les volumes pour la DB
4. Configurer les variables d’environnement (`.env`)
5. Lancer la stack et tester les endpoints
6. (Optionnel) Push des images sur Docker Hub

### 🎯 Objectifs pédagogiques du TP :

- Maîtriser une stack conteneurisée complète
- Appliquer les bonnes pratiques vues en formation
- Être autonome dans l’écriture et le déploiement d’un environnement Docker

---

## 📁 Livrables

- Support de cours PDF ou Markdown
- Fichiers d’exercices + corrigés
- Ressources bonus (cheatsheets, liens utiles)

---

## 🧩 Ressources complémentaires

- [Docker Documentation](https://docs.docker.com/)
- [Play with Docker](https://labs.play-with-docker.com/)
- [Docker Cheatsheet (GitHub)](https://github.com/wsargent/docker-cheat-sheet)
