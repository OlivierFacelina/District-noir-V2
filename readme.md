# FONCTION SET_COLOR :

"""Concaténer une chaine à un code couleur.
Cette fonction sert à retourner une chaine en lui appliquant une couleur en fonction d'un code 
Codes Couleur utile pour l'exercice
Blue : 32 | Orange : 208 | Pink : 206 | Yellow : 220 | Green : 28 | Red : 196

Parameters
----------
pstr : string
    Chaine à colorer
pcolor : int
    code couleur (cf. chiffre ci-dessus)

Returns
-------
string
    la chaine en entrée concaténé avec la couleur, de type : 
        Code couleur : "\x1b[38;5;33m" + {valeur} + Code permettant de remttre la couleur intiale "\x1b[0;0m"
"""

# FONCTION GET_LST_CARDS_VALUE

"""Retire tous les codes couleur.
Permetter de retirer tous les codes couleur des valeurs d'une liste passé en paramètre

Parameters
----------
lst_cards_with_color : list
    liste des cartes du jeux avec les codes couleur

Returns
-------
list
    retourne la liste des cartes du jeux sans les codes couleur
"""

# FONCTION INIT_GAME

"""Initialisation de la partie.
Cette fonction aura pour but de générer le paquets de cartes en fonction de sa composition dans le jeu :
- Cartes "SOUTIEN" : carte 5 * 5, carte 6 * 6, carte 7 * 7, carte 8 * 8 (ces cartes pourront être générés à l'aide d'une double boucle)
- Cartes "ALLIANCE" : carte 2 * 4, carte 3 * 2, carte 4 * 1 (cf. tuple alliances)
- Cartes "TRAHISON" : carte -1 * 3, carte -2 * 4, carte -3 * 2 (cf. tuple treasons)

Parameters
----------
Aucun

Returns
-------
lst_cards : list
    Retourne la liste des cartes qui constitue le paquet. Le code couleur sera appliqué sur les cartes (cf. dict code_color_cards)
beginner: int
    Retourne le numéro du joueur qui commence à la manche 1. Le chiffre sera soit 1 soit 2 et sera choisi aléatoirement
"""

# FONCTION TO_DEAL

"""Distribue les cartes pour chaque joueur et en mets 2 sur la table à la manche 1.
Cette fonction aura pour but de distribuer 5 cartes à chaque joueur
Au round 1, 2 cartes 

Parameters
----------
round : int
    numéro de la manche en cours

Returns
-------
lst_game, lst_player_1, lst_player_2
    Retourne 3 listes :
        - lst_game : liste contenant 2 cartes pour la 1ère manche et vide pour les autres manches
        - lst_player_1 : contenant les 5 cartes du joueur 1
        - lst_player_2 : contenant les 5 cartes du joueur 2
"""