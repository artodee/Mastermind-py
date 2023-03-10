from random import randint

## Le jeu se lance en tapant joue() dans l'invité de commande

NOMBRE_DE_PIONS = 4


def resultat(proposition, bonne_reponse):
    '''
  fonction qui compare la proposition avec la bonne_reponse
  :parameter: proposition (liste)
  :parameter: bonne_reponse (liste)
  :returns: une liste contenant "X" si bien placé, "o" si mal placé, "." sinon
  '''
    # un caractère bien placé sera marqué d'un X
    # un présent mais mal placé d'un o
    # ni l'un ni l'autre d'un .

    # on commence par créer la liste "bilan" à partir d'une liste par compréhension
    bilan = ["." for n in range(NOMBRE_DE_PIONS)]

    # pour éviter les effets de bord, on copie la bonne_reponse dans une autre variable avec
    # laquelle on va pouvoir travailler. Même chose pour la proposition du joueur
    prop = [e for e in proposition]
    bonne_rep = [e for e in bonne_reponse]

    # Voici le premier passage pour rechercher les éléments bien placés:

    for i in range(4):
        if prop[i] == bonne_rep[i]:
            bilan[i] = 'X'
            prop[i] = '*'
            bonne_rep[i] = '*'

    # Ici on retrouve le deuxième passage pour rechercher les éléments mal placés:

    for i in range(4):
        n = prop[i]
        if n != '*' and n in bonne_rep:
            bilan[i] = 'o'
            idx = bonne_rep.index(n)
            bonne_rep[idx] = '*'

    return bilan  # ne pas oublier return


COULEURS = {'.': '\033[0;37m', "o": '\033[0;31m', "X": '\033[0;32m'}


def affiche_resultat(liste):
    """
  affiche en couleur une liste
  """
    print("> ", end="")
    for c in liste:
        print(COULEURS[c], c, end="", sep="")
    print(COULEURS["."])


def joue():
    # on tire une combinaison au hasard
    print("--------------")
    print("| MasterMind |")
    print("--------------")
    print("La combinaison contient 4 chiffres entre 0 et 5 (inclus)")
    print("qui peuvent être présents plusieurs fois.")
    print("bonne chance !\n\n")

    combinaison_a_deviner = []  # on crée la variable combinaison_a_deviner

    # maintenant on remplit cette liste avec NOMBRE_DE_PIONS nombres, compris entre 0 et 5
    for i in range(NOMBRE_DE_PIONS):
        combinaison_a_deviner.append(str(randint(0, 5)))

    nombre_de_coups = 0  # pour le moment le nombre de coups joués vaut 0
    proposition_joueur = []  #   on fabrique la variable proposition_joueur
    while (proposition_joueur != combinaison_a_deviner
           and nombre_de_coups <= 12):
        proposition_joueur = list(input("? "))
        nombre_de_coups += 1
        affiche_resultat(resultat(proposition_joueur, combinaison_a_deviner))

    # si on arrive ici, c'est que l'on a quitté la boucle while... soit
    # parce qu'on a gagné...
    if proposition_joueur == combinaison_a_deviner:
        print(f"gagné en {nombre_de_coups} coups !")
    else:  # soit parceque le nombre de tentatives est supérieur à 12
        print("perdu !")
