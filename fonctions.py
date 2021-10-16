# -*- coding: utf-8

"""
ROSA Mathias
Devoir maison d'informatique
Convertisseur d’entiers : Octobre 2021

Fonctions
"""

from Piles import Créer_Pile, Empiler, Dépiler, Pile_Vide, Longueur


def chiffre_vers_b10(chiffre):
    """
    Prend en argument :
        - un entier dans une base parmi (2, 5, 10, 16) : str

    Retourne :
        - un chiffre de la base 10 : int

    Permet de convertir un nombre en chiffre de la base 10
    """

    table = ["A", "B", "C", "D", "E", "F"]
    if chiffre in table:
        return 10 + table.index(chiffre)
    return int(chiffre)


def convertir_vers_b10(entier, base):
    """"
    Prend en argument :
        - un entier à convertir : str
        - la base depuis laquelle on souhaite effectuer la conversion : int

    Retourne :
        - le nombre converti en base 10 : int

    Cette fonction sert à convertir un nombre en base 2 à un nombre en une
    autre base parmi (2, 5, 10, 16)
    """
    pile_entier = Créer_Pile()

    # On ajoute tous les chiffres de l'entier dans une pile
    for chiffre in entier:
        Empiler(pile_entier, chiffre)

    nombre_converti = 0

    # Pour chaque chiffre de la pile, on multiplie le chiffre par la base à la
    # puissance de la position du nombre dans la pile
    for i in range(Longueur(pile_entier)):

        # On convertit le chiffre de la base d'entrée en chiffre de la base 10
        chiffre = chiffre_vers_b10(Dépiler(pile_entier))
        nombre_converti += chiffre * base**i

    return nombre_converti


def convertir_dp_b10(entier, base):
    """"
    Prend en argument :
        - un entier à convertir : int
        - la base vers laquelle on souhaite effectuer la conversion : int

    Retourne :
        - le nombre converti : str

    Cette fonction sert à convertir un nombre en base 10 à un nombre en une
    autre base parmi (2, 5, 10, 16)
    """
    # On traite en premier le cas ou l'entier est 0.
    if entier == 0:
        return "0"

    pile_reste = Créer_Pile()
    while entier != 0:  # On effectue les divisions euclidiennes successives.
        reste = entier % base

        # Si la base est la base 16, il faut convertir les entiers > 9
        # en chiffres de la base 16 (lettres)
        if base == 16 and reste > 9:
            table = ["A", "B", "C", "D", "E", "F"]
            reste = table[reste - 10]

        Empiler(pile_reste, str(reste))
        entier = entier // base

    nombre_converti = ""
    while not Pile_Vide(pile_reste):
        nombre_converti += Dépiler(pile_reste)

    return nombre_converti


def verifier(entier, base):
    """
    Prend en argument :
        - un entier : str
        - la base dans laquelle il est censé être écrit : int

    Retourne :
        - True si l'entier peut être écrit dans la base et False sinon

    Cette fonction sert à vérifier qu'un nombre est bien écrit dans une
    certaine base parmi (2, 5, 10, 16)

    """
    liste_chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                      "A", "B", "C", "D", "E", "F"]

    for chiffre in entier:
        # On vérifie si chaque chiffre est bien un chiffre de la base passée en
        # argument
        if chiffre not in liste_chiffres[:base]:
            # Le chiffre n'est pas un chiffre de la base passée en argument.
            return False

    # Tous les chiffres sont des chiffres de la base passée en argument.
    return True
