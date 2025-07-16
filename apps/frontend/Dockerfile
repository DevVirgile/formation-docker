FROM alpine:3.18.4
RUN apk update && \
    apk upgrade
# Installer Nginx
RUN apk add --no-cache nginx
# Exposer le port 80 pour permettre l'accès HTTP
EXPOSE 80
# Démarrer Nginx
CMD ["nginx", "-g", "daemon off;"]