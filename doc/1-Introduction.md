# Introduction

## Quelques informations sur Docker

- Création : Docker est une plateforme open source lancée en 2013 par Docker Inc., dont un des fondateurs est Solomon Hykes, ingénieur et entrepreneur français
- Problème adressé : Difficulté à garantir que les applications fonctionnent de manière identique entre les environnements dev, test, et prod.
- Solution apportée : Conteneurs légers et portables qui emballent une application avec toutes ses dépendances dans un environnement isolé.
- Technologie sous-jacente : Utilisation des fonctionnalités Linux (cgroups, namespaces) pour isoler les processus sans la lourdeur d’une machine virtuelle.
- Avantages :
  - Isolation légère et rapide
  - Portabilité entre machines et environnements
  - Reproductibilité garantie du fonctionnement de l’application
  - Accélération du cycle de développement
  - Facilitation du déploiement et de la montée en charge (orchestration)
- Impact : Transformation majeure dans le développement logiciel, adoption massive dans les pratiques DevOps et les architectures microservices.


![Containers vs. VMs](https://blog.stephane-robert.info/_astro/docker-1.CNZLw2-i_Z1z7k4A.webp)

Source : https://blog.stephane-robert.info/_astro/docker-1.CNZLw2-i_Z1z7k4A.webp

## Comparaison entre VM et conteneurs 

| Critère                        | Machines Virtuelles (VM)                           | Docker (Conteneurs)                                      |
| ------------------------------ | -------------------------------------------------- | -------------------------------------------------------- |
| **Isolation**                  | Isolation complète avec un OS invité complet       | Isolation au niveau des processus, partage du noyau hôte |
| **Lourdeur**                   | Plus lourdes : OS complet + applications           | Plus légers : partagent le noyau du système hôte         |
| **Démarrage**                  | Lancement plus lent (minutes)                      | Démarrage très rapide (secondes ou millisecondes)        |
| **Utilisation des ressources** | Plus gourmande en CPU, RAM, stockage               | Plus efficace et optimisée                               |
| **Portabilité**                | Portabilité possible via images VM (VMDK, etc.)    | Très portable grâce aux images Docker                    |
| **Gestion**                    | Gestion via hyperviseur (ex: VMware, Hyper-V, KVM) | Gestion via Docker Engine et outils associés             |
| **Cas d’usage**                | Simuler environnements complets, OS différents     | Déploiement rapide d’applications et microservices       |
| **Sécurité**                   | Isolation forte mais plus complexe                 | Isolation légère, dépendante du noyau hôte               |
| **Taille des images**          | Gigaoctets souvent                                 | Quelques dizaines de Mo à centaines de Mo                |
| **Exemple**                    | VMware, VirtualBox, Hyper-V                        | Docker, Podman, containerd                               |