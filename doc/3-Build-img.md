# Construire une image

## Notions de Layers

Pour construire une image, on part d'une image préexistente, et lui ajoute des couches (layers) par dessus.
Pour se faire, 

Exemple de Dockerfile :

```Dockerfile
FROM alpine:3.20.0

ARG NAME_MAINTENER=Manuel
LABEL maintener=${NAME_MAINTENER}

RUN mkdir -p /data/in /data/out

WORKDIR /app

ENV NAME_TO_GREET=Dorian

COPY scripts/ .

ENTRYPOINT ["sh", "greetings.sh", "ENTRYPOINT", "$NAME_TO_GREET"]
CMD ["sh", "greetings.sh", "CMD", "$NAME_TO_GREET"]
```

## Les différentes instructions pour le Dockerfile

[Lien vers article sur les différentes instructions (Blog Stephane Robert)](https://blog.stephane-robert.info/docs/conteneurs/images-conteneurs/ecrire-dockerfile/#linstruction-copy)

### ENTRYPOINT vs CMD

| Aspect                   | `ENTRYPOINT`                                  | `CMD`                                        |
| ------------------------ | --------------------------------------------- | -------------------------------------------- |
| **But**                  | Définir la **commande principale** de l'image | Fournir des **arguments par défaut**         |
| **Peut être surchargé**  | ✅ Oui (avec `--entrypoint`)                  | ✅ Oui (avec `docker run ... <nouvelle cmd>`) |
| **Combinaison possible** | ✅ Oui (ENTRYPOINT + CMD = commande + args)   | ❌ Seul, CMD est toute la commande            |
| **Utilisation typique**  | Script ou binaire principal à exécuter        | Paramètres par défaut ou shell à exécuter    |

### Pour créer son image

```bash
docker build -t monapp:local .
```