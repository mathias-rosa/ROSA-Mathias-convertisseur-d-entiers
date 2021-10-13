
"""
Module de gestion de piles python
Mathias ROSA
"""


def Créer_Pile():
    """
    Ne prend rien en argument, renvoie une liste vide (type list)
    """
    return []


def Empiler(pile, element):
    """
    Prend en argument une pile (type list) et un element à empiler
    (tous types)
    Ajoute l'element à la pile et ne renvoie rien
    """
    pile.append(element)


def Dépiler(pile):
    """
    Prend en argument une pile (type list)
    Si la pile est non vide, retire et renvoie l'element au sommet de la pile
    (tous types) sinon, renvoie un message d'erreur (type str)
    """
    return pile.pop() if pile else "Erreur : impossible de dépiler une pile vide"


def Pile_Vide(pile):
    """
    Prend en argument une pile (type list)
    Renvoie True si la pile est vide et False sinon (type bool)
    """
    return pile == []


def Longueur(pile):
    """
    Prend en argument une pile (type list)
    Renvoie la longueur de la pile (type int)
    """
    return len(pile)


def Premier(pile):
    """
    Prend en argument une pile (type list)
    Si la pile est non vide, renvoie la valeur du sommet de la pile
    (type du sommet de la pile) et sinon un message d'erreur
    """
    if pile:
        premier = pile.pop()
        pile.append(premier)
        return premier
    return "Erreur : Pile vide"


def Inverser(pile):
    """"
    Prend en argument une pile (type list)
    Renvoie la pile qui contient les mêmes éléments, mais dont l’ordre a
    été inversé. (type list)
    """
    return [pile.pop() for elem in range(len(pile))]
