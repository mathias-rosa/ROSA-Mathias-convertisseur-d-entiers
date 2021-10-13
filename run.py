# -*- coding: utf-8

"""
ROSA Mathias
Devoir maison d'informatique
Convertisseur d’entiers : Octobre 2021

Lancement du programme
"""

# Import de l'interface graphique
from fonctions import convertir_vers_b10, convertir_dp_b10, verifier
from interface_graphique import (fenetre, bouton_convertir, texte_entree,
                                 base_deux, base_cinq, base_dix, base_seize,
                                 var_bases, frame_err)


def convertir():
    """
    Ne prend rien en argument.
    Ne retourne rien si l'utilisateur a bien rentré un nombre contenant des
    chiffres de la base qu'il a choisi dans l'interface graphique et un messege
    d'erreur sinon.

    Permet de gérer l'interaction de l'utilisateur sur l'interface graphique.
    """

    # On enlève un eventuel ancien message d'erreur
    frame_err.pack_forget()
    # On récupère l'entier depuis l'entrée utilisateur
    entier = texte_entree.get()

    # Les deux derniers caractères de var_bases.get() correspondent au numéro
    # de la base
    base = int(var_bases.get()[-2:])

    if not verifier(entier, base):
        #  On enlève le bouton convertir afin de faire de la place pour le
        # message d'erreur.
        bouton_convertir.pack_forget()
        # On ajoute le message d'erreur.
        frame_err.pack(fill="x")
        # On remet le bouton convertir.
        bouton_convertir.pack(side="right")
        return "Erreur : chiffre interdit"

    if base == 2:

        entier_b10 = convertir_vers_b10(entier, 2)

        base_deux.set(entier)
        base_cinq.set(convertir_dp_b10(entier_b10, 5))
        base_dix.set(entier_b10)
        base_seize.set(convertir_dp_b10(entier_b10, 16))

    elif base == 5:

        entier_b10 = convertir_vers_b10(entier, 5)

        base_deux.set(convertir_dp_b10(entier_b10, 2))
        base_cinq.set(entier)
        base_dix.set(entier_b10)
        base_seize.set(convertir_dp_b10(entier_b10, 16))

    elif base == 10:

        base_deux.set(convertir_dp_b10(int(entier), 2))
        base_cinq.set(convertir_dp_b10(int(entier), 5))
        base_dix.set(entier)
        base_seize.set(convertir_dp_b10(int(entier), 16))

    elif base == 16:

        entier_b10 = convertir_vers_b10(entier, 16)

        base_deux.set(convertir_dp_b10(entier_b10, 2))
        base_cinq.set(convertir_dp_b10(entier_b10, 5))
        base_dix.set(entier_b10)
        base_seize.set(entier)


# On lie la fonction convertir au bouton "convertir" de l'interface graphique
bouton_convertir.configure(command=convertir)

# =============================================================================
# Lancement de la fenetre
# =============================================================================

fenetre.mainloop()
