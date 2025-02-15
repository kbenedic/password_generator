import random
import string

#fonction pour générer un mot de passe sécurisé
def generate_password(length=12):
    # Définir les caractères possible
    characters = string.ascii_letters + string.digits +string.punctuation
    #Générer le mot de passe aléatoirement
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Test de génération d'un mot de passe
if __name__== "__main__":
    password = generate_password(16) # Générer un mdp en 16 carac.
    print(f"mot de passe généré : {password}")