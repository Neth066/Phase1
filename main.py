from api import QuixoAPI
from quixo import afficher_plateau, verifier_victoire

# Créer une instance de QuixoAPI avec l'idul et le token
idul = "votre_idul"
token = "votre_token"
quixo_api = QuixoAPI(idul, token)

# Initialiser une nouvelle partie
reponse = quixo_api.initialiser_partie()
if "error" in reponse:
    print("Erreur lors de l'initialisation de la partie.")
else:
    game_id = reponse["id"]
    plateau = reponse["plateau"]
    afficher_plateau(plateau)

    # Boucle de jeu principale
    while True:
        position = int(input("Choisissez la position du cube à déplacer (0-24): "))
        direction = input("Choisissez la direction du déplacement (haut, bas, gauche, droite): ")
        
        # Jouer un coup
        reponse = quixo_api.jouer_un_coup(game_id, position, direction)
        if "error" in reponse:
            print("Erreur lors du jeu d'un coup.")
            continue

        plateau = reponse["plateau"]
        afficher_plateau(plateau)

        # Vérifier si un joueur a gagné
        if verifier_victoire(plateau, "X"):
            print("Félicitations, vous avez gagné!")
            break
        elif verifier_victoire(plateau, "O"):
            print("Dommage, l'adversaire a gagné.")
            break