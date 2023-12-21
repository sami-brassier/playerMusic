import hashlib

def check_password(password):
    requirements = [
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(c in "!@#$%^&*" for c in password),
        len(password) >= 8
    ]

    return all(requirements)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password = input("Choisir un mot de passe : ")

while not check_password(password):
    print("Le mot de passe ne respecte pas les exigences de sécurité.")
    password = input("Choisir un nouveau mot de passe : ")

hashed_password = hash_password(password)

print("Mot de passe valide ! Crypté :", hashed_password)