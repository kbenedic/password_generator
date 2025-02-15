Générateur de mots de passe sécurisé

Ce projet est un générateur de mots de passe sécurisé avec une vérification via l'API Pwned Passwords. Il génère un mot de passe aléatoire et vérifie si ce mot de passe a été compromis dans une fuite de données en utilisant l'API de Pwned Passwords.

Fonctionnalités
Génération d'un mot de passe aléatoire
Vérification du mot de passe contre l'API Pwned Passwords pour vérifier s'il a été compromis

Prérequis
Python 3.x
Les bibliothèques suivantes :
requests

Installation
Clonez le repository ou téléchargez les fichiers.

Installez les dépendances nécessaires avec la commande suivante :

bash

pip install requests

Lancez l'application avec la commande :

bash

python app.py

Accédez à l'application à l'adresse suivante dans votre navigateur : http://127.0.0.1:5000/.

Utilisation
Entrez la longueur du mot de passe que vous souhaitez générer (entre 6 et 20 caractères).
Cliquez sur "Générer" pour obtenir un mot de passe sécurisé.
Le mot de passe sera généré et une vérification sera effectuée pour vérifier s'il a été compromis dans une fuite de données.

Licence
Ce projet est sous licence MIT.