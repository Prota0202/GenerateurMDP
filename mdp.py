import random
import string

# Définition des caractères possibles pour le mot de passe
CARACTERES = string.ascii_letters + string.digits + string.punctuation

# Fonction pour créer un seul mot de passe
def creer_mot_de_passe(taille: int) -> str:
    mdp = random.sample(CARACTERES, k=taille)
    return ''.join(mdp)

# Fonction pour générer un ensemble de mots de passe et les enregistrer dans un fichier
def creer_mots_de_passe(quantite: int, nom_fichier: str) -> None:
    if not 1 <= quantite <= 100:
        raise ValueError("Nombre de mots de passe invalide")
    ensemble_mdp = set()
    while len(ensemble_mdp) < quantite:
        taille_mdp = random.randint(6, 16)
        mdp = creer_mot_de_passe(taille_mdp)
        ensemble_mdp.add(mdp)
    with open(f"{nom_fichier}.txt", "a") as fichier:
        for mdp in ensemble_mdp:
            fichier.write(f"\nMot de passe: {mdp}\n---------")
            print(f"Mot de passe: {mdp}\n---------")
    print(f"Mots de passe générés et enregistrés dans {nom_fichier}")

# Interactions avec l'utilisateur pour générer les mots de passe
nb_mdp = int(input("Combien de mots de passe voulez-vous générer ? : "))
nom_fichier = input("Entrez le nom du fichier où sauvegarder : ")
try:
    creer_mots_de_passe(nb_mdp, nom_fichier)
except ValueError as erreur:
    print(erreur)
input("Appuyez sur Entrée pour continuer..")
