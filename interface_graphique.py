# -*- coding: utf-8

"""
ROSA Mathias
Devoir maison d'informatique
Convertisseur d’entiers : Octobre 2021

Interface Graphique
"""

# Import de la bibliothèque Tkinter
from tkinter import *
from tkinter import ttk


# =============================================================================
# Variables Globales
# =============================================================================

COULEUR_FOND = "#F3F4F5"
COULEUR_TEXTE = "#191C1F"
COULEUR_ACCENTUATION = "#EB5CAB"
COULEUR_BLEU = "#0666EB"


# =============================================================================
# Création de la fentre et frame principale
# =============================================================================

fenetre = Tk()

frame_principale = Frame(fenetre, bg=COULEUR_FOND)
frame_principale.pack(fill="both", expand=True, padx=10)

# =============================================================================
# Titre
# =============================================================================

label_titre = Label(frame_principale, text="Convertisseur\nd'entiers",
                    font="Abadi 20 bold", fg=COULEUR_TEXTE, bg=COULEUR_FOND,
                    justify="left", anchor="w")
label_titre.pack(fill="x", pady=10)

# =============================================================================
# Choix de la base
# =============================================================================

label_base = Label(frame_principale, text="Base de départ",
                   font="Abadi 12 bold", fg=COULEUR_ACCENTUATION,
                   bg=COULEUR_FOND, justify="left", anchor="w")
label_base.pack(fill="x")

var_bases = StringVar()
var_bases.set("Base 10")

bases_menu = ttk.Combobox(frame_principale, textvariable=var_bases,
                          values=("Base 2", "Base 5", "Base 10", "Base 16"),
                          state="readonly", font="Abadi 12 bold")


bases_menu.pack(fill="x", ipady=5)

# =============================================================================
# Zone d'entrée
# =============================================================================

label_entree = Label(frame_principale, text="Quel entier souhaitez vous"
                     " convertir ?",
                     font="Abadi 12 bold", fg=COULEUR_ACCENTUATION,
                     bg=COULEUR_FOND, justify="left", anchor="w")
label_entree.pack(fill="x", pady=5)

texte_entree = StringVar()
texte_entree.set("0")

entry_entree = Entry(frame_principale, font="Abadi 14 bold",
                     fg=COULEUR_TEXTE, bg="white", relief=FLAT, cursor="xterm",
                     textvariable=texte_entree)
entry_entree.pack(fill="x", pady=5, ipady=5)

# =============================================================================
# Affichage des Résultats
# =============================================================================

label_resultats = Label(frame_principale, text="Résultats",
                     font="Abadi 12 bold", fg=COULEUR_ACCENTUATION,
                     bg=COULEUR_FOND, justify="left", anchor="w")
label_resultats.pack(fill="x", pady=5)

frame_resultats = Frame(frame_principale, bg="white")
frame_resultats.pack(fill="x", pady=5, ipadx=10, ipady=5)

# =============================================================================
# Tableau
# =============================================================================

frame_base_titre = Frame(frame_resultats, bg="white")
frame_base_titre.pack(fill="x", pady=5, padx=5, ipadx=5)

frame_base_titre.columnconfigure(0, weight=3)
frame_base_titre.columnconfigure(1, weight=1)

# =============================================================================
# Entete du tableau
# =============================================================================

Label(frame_base_titre, text="Entier Converti", font="Abadi 15 bold",
      bg="white", fg=COULEUR_BLEU).grid(column=0, row=1, sticky="W")

Label(frame_base_titre, text="Base", font="Abadi 15 bold",
      bg="white", fg=COULEUR_BLEU).grid(column=1, row=1)

# =============================================================================
# Base 2
# =============================================================================

base_deux = StringVar()
base_deux.set("0")

entry_base_deux = Entry(frame_base_titre, textvariable=base_deux,
                        font="Abadi 12 bold", bg="white", fg=COULEUR_TEXTE,
                        relief=FLAT, cursor="xterm")
entry_base_deux.grid(column=0, row=2, sticky="W", padx=10)

Label(frame_base_titre, text="2", font="Abadi 15",
      bg="white", fg=COULEUR_TEXTE).grid(column=1, row=2)

# =============================================================================
# Base 5
# =============================================================================

base_cinq = StringVar()
base_cinq.set("0")

entry_base_cinq = Entry(frame_base_titre, textvariable=base_cinq,
                        font="Abadi 12 bold", bg="white", fg=COULEUR_TEXTE,
                        relief=FLAT, cursor="xterm")
entry_base_cinq.grid(column=0, row=3, sticky="W", padx=10)

Label(frame_base_titre, text="5", font="Abadi 15",
      bg="white", fg=COULEUR_TEXTE).grid(column=1, row=3)

# =============================================================================
# Base 10
# =============================================================================

base_dix = StringVar()
base_dix.set("0")

entry_base_dix = Entry(frame_base_titre, textvariable=base_dix,
                       font="Abadi 12 bold", bg="white", fg=COULEUR_TEXTE,
                        relief=FLAT, cursor="xterm")
entry_base_dix.grid(column=0, row=4, sticky="W", padx=10)

Label(frame_base_titre, text="10", font="Abadi 15",
      bg="white", fg=COULEUR_TEXTE).grid(column=1, row=4)

# =============================================================================
# Base 16
# =============================================================================

base_seize = StringVar()
base_seize.set("0")

entry_base_seize = Entry(frame_base_titre, textvariable=base_seize,
                         font="Abadi 12 bold", bg="white", fg=COULEUR_TEXTE,
                        relief=FLAT, cursor="xterm")
entry_base_seize.grid(column=0, row=5, sticky="W", padx=10)

Label(frame_base_titre, text="16", font="Abadi 15",
      bg="white", fg=COULEUR_TEXTE).grid(column=1, row=5)


# =============================================================================
# Message d'erreur
# =============================================================================

frame_err = Frame(frame_principale, bg=COULEUR_FOND)

Label(frame_err, text="⚠️", font="Abadi 15 bold", fg="#dc3545",
                     bg=COULEUR_FOND, justify="left",
                     anchor="w").pack(side="left")
label_erreur = Label(frame_err, text="L'entier entré n'est pas dans la"
                     "\nbonne base", font="Abadi 12 bold", fg="#dc3545",
                     bg=COULEUR_FOND, justify="left", anchor="w")
label_erreur.pack(fill="x", pady=5)


# =============================================================================
# Bouton convertir
# =============================================================================

bouton_convertir = Button(frame_principale, text="Convertir", font="Abadi 12 bold",
                   bg=COULEUR_BLEU, fg="white", relief=FLAT, cursor="hand2")
bouton_convertir.pack(side="right")


# =============================================================================
# Paramètres supplémentaires de la fenêtre
# =============================================================================

fenetre.geometry("320x550")
fenetre.title("Convertiseur d'entiers")


if __name__ == "__main__":

    # Permet de lancer l'interface graphique seule si on exécute le fichier
    # interface_graphique.py. L'interface graphique n'est pas connectée
    # aux fonctions, le programme se lance depuis le fichier run.py
    fenetre.mainloop()
