import requests
import hashlib
import random
import string

def check_password_pwned(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chars = sha1_hash[:5]
    rest_of_hash = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{first5_chars}"
    response = requests.get(url)

    if response.status_code == 200:
        if rest_of_hash in response.text:
            print(f"Le mot de passe {password} a été compromis !")
            print("Il est fortement conseillé de changer ce mot de passe.")
        else:
            print(f"Le mot de passe {password} est sécurisé.")
    else:
        print("Erreur de connexion à l'API Pwned Passwords.")

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        print("\nGénérateur de mot de passe sécurisé et vérification contre les mots de passe compromis.")
        length = input("Entrez la longueur du mot de passe (par défaut 12): ")
        length = int(length) if length else 12

        password = generate_password(length)
        print(f"Mot de passe généré: {password}")

        check_password_pwned(password)

        repeat = input("\nSouhaitez-vous générer un autre mot de passe ? (o/n): ")
        if repeat.lower() != 'o':
            print("Merci d'avoir utilisé le générateur de mot de passe !")
            break

if __name__ == "__main__":
    main()
