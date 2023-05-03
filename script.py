# Bibliothèques utilisées
import random
import re
import os

#-------------------- Fonctions ----------------

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

def set_color(pstr, pcolor):
    num1 = str(pcolor)
    if pcolor % 16 == 0:
        return(f"\033[38;5;{num1}m{pstr}\033[0;0m")
    else:
        return(f"\033[38;5;{num1}m{pstr}\033[0;0m")

def get_lst_cards_value(lst_cards_with_color):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    lst_cards_value = []
    for card in lst_cards_with_color:
        value = ansi_escape.sub('', card).strip()
        # if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
        #     value = int(value)
        lst_cards_value.append(value)
    return lst_cards_value

def init_game():
     # tuple contenant la liste des cartes alliances du paquet
    alliances = (+2, +2, +2, +2, +3, +3, +4)
    # tuple contenant la liste des cartes trahison du paquet
    treasons = (-1, -1, -1, -2, -2, -2, -2, -3, -3, -3)
    # tuple content la liste des villes
    city = ('Docks','Commissariat','Mairie')
    # dictionnaire permettant de connaitre le code couleur de la carte en fonction de sa valeur
    code_color_cards = {5: 32, 
                        6: 208, 
                        7: 206, 
                        8: 196}
    lst_cards = []

    # Ajout des cartes 5, 6, 7 et 8
    for i in range(5, 9):
        for j in range(i):
            lst_cards.append(set_color(str(i), code_color_cards[i]))
            
    # Ajout des cartes "ville"
    for i in city:
        lst_cards.append(i)
    # Ajout de cartes "alliance"
    for i in alliances:
        lst_cards.append(i)
    # Ajout de cartes "trahison"
    for i in treasons:
        lst_cards.append(i)

    # Mélangez les 45 cartes
    def melanger_cartes():
        random.shuffle(lst_cards)
        return lst_cards
    melanger_cartes()

    # Retirer 3 cartes
    def retirer_cartes_pioche():
        for i in range(3):
            lst_cards.remove(lst_cards[-1])
        return lst_cards
    print(f"Pioche du jeu après les 3 cartes retirées : {retirer_cartes_pioche()}")
    
    # Une fois la génération du paquet de cartes terminé, on le retourne
    return lst_cards, random.randint(1,2)
# lst_cards = init_game()

def to_deal(round):
    lst_cards, starting_player = init_game()
    lst_game = []
    lst_player_1 = []
    lst_player_2 = []
    
    for i in range(5):
        lst_player_1.append(lst_cards.pop())
        lst_player_2.append(lst_cards.pop())
        
    if round == 1:
        for i in range(2):
            lst_game.append(lst_cards.pop())

    return lst_game, lst_player_1, lst_player_2
# lst_game, lst_player_1, lst_player_2 = to_deal(1)
# print("Main du joueur 1 : ", lst_player_1)
# print("Main du joueur 2 : ", lst_player_2)

def display_game(round, lst_game, lst_collecting_cards_1, lst_collecting_cards_2, num_player = 0, lst_player = []):
    # Efface la console
    os.system('cls')
    
    # Séparateur pour une meilleur visibilité
    print(f'--------- Manche {round} ----------')

    # Afficher les cartes sur la table
    print("Tapis : ", lst_game)

    # Afficher les cartes ramassées par le joueur 1
    print("Joueur 1 a ramassé : ", lst_collecting_cards_1)

    # Afficher les cartes ramassées par le joueur 2
    print("Joueur 2 a ramassé :", lst_collecting_cards_2)

    # Séparateur pour une meilleur visibilité
    print('\n------------------------------')

    # Afficher la main du joueur qui doit jouer
    print(f"C'est au tour du joueur {num_player}")
    print(f"Vos cartes {lst_player}")
# print(display_game(1,lst_game,7,7,1,lst_player_1))

def to_play(lst_game, num_player, lst_player, lst_collecting_cards, player_take):
    lst_collecting_cards = []
    # On converti la liste des cartes de la main du joueur en liste extrayant que la valeur des cartes
    
    # Tant que la saisie diffère d'une carte de la main ou qu'elle est différente de 0, on refait saisir le joueur
    while True:
        # Demander au joueur de saisir la valeur d'une carte de sa main ou de saisir la chaine "take" s'il souhaite prendre et qu'il n'a pas encore pris durant cette manche
        action = input("Veux-tu poser une carte (Poser) ou prendre les 5 dernières cartes (Prendre) ?")
        # Si le joueur décide de joueur une carte de sa main
        if action == "Poser":
            # on retire la carte de sa main et on l'ajouter aux cartes de la table
            card = int(input("Quelle carte veux-tu poser ?"))
            if card in lst_player:
                lst_game.append(card)
                lst_player.remove(card)
            break
        # Sinon si le joueur décide de prendre les cartes de la table s'il n'a pas déjà pris durant cette manche et qu'il y a au moins 1 carte sur la table
        elif action == "Prendre" and len(lst_game) > 0 and player_take == False:
            
            # Si le jeu contient moins de 5 cartes, le joueur ramasse toutes les cartes de la table
            if len(lst_game) < 5:
                card = lst_game
                lst_collecting_cards.append(card)
                lst_game = []
            else:
                # Sinon, le joueur ne peut prendre que les 5 dernières cartes de la table
                last_cards = len(lst_game) - 1
                for i in range(5):
                    card = lst_game[last_cards]
                    lst_game.remove(card)
                    lst_collecting_cards.append(card)
                    last_cards -= 1

            # On vérifie si le joueur possède 3 carte citées
            if "Commissariat" in lst_collecting_cards and "Docks" in lst_collecting_cards and "Mairie" in lst_collecting_cards:
                check_three_cities(num_player,lst_collecting_cards)
            
            # Ne pas oublier de passer le drapeau permettant de savoir s'il a pris durant cette manche à True
            player_take = True
            break

    return lst_game, lst_player, lst_collecting_cards, player_take
# lst_param_collectings_cards = []
# lst_game, lst_player, lst_collecting_cards, player_take = to_play(lst_game,1,lst_player_1,lst_param_collectings_cards,False)
# print(lst_game,lst_player,lst_collecting_cards,player_take)

def check_three_cities(num_player, lst_collecting_cards):
    nb_cities = 0
    # On boucle sur les cartes ramassées du joueur
    for card in lst_collecting_cards:
        # Si la carte a pour valeur (inutile de retirer le code couleur car les cartes cités n'en possède pas) le nom d'une des 3 cités
        if card in ['Commissariat','Docks','Mairie']:
            # si c'est le cas on incrémente un compteur
            nb_cities += 1
    # Si 3 cartes cités sont comptés on appelle la fonction end_game
    if nb_cities == 3:
        end_game(num_player)
# print(check_three_cities(1,lst_collecting_cards))

"""Regroupe et Compte les cartes ramassées par un joueur.
Cette fonction aura pour but de regrouper les cartes de même valeur et de les compter. Ce qui simplifira le comptage des points.
Elle exclura également les cartes cités car elle ne sont pas nécessaire au comptage des points

Parameters
----------
lst_collecting_cards : list
    Liste des cartes ramassées du joueur pour laquelle on souhaite vérifier qu'il n'y a pas 3 cartes cités

Returns
-------
lst_group_cards : dictionnaire
    Dictionnaire avec comme clés, les valeurs des cartes et en valeur pour chaque clé le nombre de cartes
"""    
def get_group_cards(lst_collecting_cards):
    lst_group_cards = {}
    # Avant de compter les cartes, on retire le code couleur des cartes
    
    # On boucle sur toutes les cartes
    for i in range(len(lst_collecting_cards)):
        # Si les cartes sont différentes des cartes cités on les ajoute au dictionnaire
        if lst_collecting_cards[i] != "Docks" or lst_collecting_cards[i] != "Commissariat" or lst_collecting_cards[i] != "Mairie":
            # Si la valeur de la carte a déjà été inséré dans le dictionnaire, on incrémente sa quantité
            if lst_group_cards.__contains__(lst_collecting_cards[i]):
                lst_group_cards[lst_collecting_cards[i]] += 1
            # Sinon on l'ajoute dans le dictionnaire
            else:
                # lst_group_cards.append(lst_collecting_cards[i])
                lst_group_cards[lst_collecting_cards[i]] = 1
    return lst_group_cards

# get_group_cards(lst_collecting_cards = [5,8,5,5,5,8,"+2","+2", "-1"])

"""Calcule les points
Cette fonction aura pour but de calculer les points à partir du dictionnaire regroupant les cartes. Le comptage se fera selon les règles suivantes :
    - cartes SOUTIEN identiques : la majorité marque le nombre de points égal au chiffre du SOUTIEN, en cas d'égalité aucun joueur ne remporte les points
    - 4 cartes SOUTIEN différentes : 5 points par série de 5-6-7-8
    - cartes ALLIANCE et TRAHISON : ajouter et retirer les points figurant sur les cartes
En cas d'égalité : le joueur ayant le plus de cartes SOUTIEN 8 remporte la partie, si égalité même chose pour les cartes SOUTIEN 7 etc...

Parameters
----------
group_cards_1 : collection
    Dictionnaire avec comme clés, les valeurs des cartes et en valeur pour chaque clé le nombre de cartes du joueur 1
group_cards_2 : collection
    Dictionnaire avec comme clés, les valeurs des cartes et en valeur pour chaque clé le nombre de cartes du joueur 2

Returns
-------
score_player_1 : int
    Score du joueur 1
score_player_2 : int
    Score du joueur 2
"""
def get_scoring(group_cards_1, group_cards_2):
    score_player_1 = 0
    score_player_2 = 0

    # SOUTIEN (cartes de 5 à 8) : La majorité marque un nombre de points égal au chiffre représenté sur la carte SOUTIEN
    for i in range(5,9):
        # Si le joueur ne possède pas une des 4 cartes SOUTIEN
        if group_cards_1.__contains__(i) == False:
            if group_cards_2.__contains__(i) == True:
                score_player_2 += i
        elif group_cards_2.__contains__(i) == False:
            if group_cards_1.__contains__(i) == True:
                score_player_1 += i
        # En cas d'égalité aucun joueur ne remporte les points
        elif group_cards_1[i] == group_cards_2[i]:
            print("Egalité")
        # Si le joueur à une plus grande quantité de carte SOUTIEN
        elif group_cards_1[i] > group_cards_2[i]:
            score_player_1 += i
        else:
            score_player_2 += i


    # SOUTIEN (cartes de 5 à 8) : 4 SOUTIENS différents remporte 5 points

    # Calcul pour le Joueur 1
    if group_cards_1.__contains__(5) and group_cards_1.__contains__(6) and group_cards_1.__contains__(7) and group_cards_1.__contains__(8):
        min_value = 10
        for i in range(5,9):
            if group_cards_1[i] < min_value:
                min_value = group_cards_1[i]
        score_player_1 += 5 * min_value
    # Calcul pour le Joueur 2
    if group_cards_2.__contains__(5) and group_cards_2.__contains__(6) and group_cards_2.__contains__(7) and group_cards_2.__contains__(8):
        min_value = 10
        for i in range(5,9):
            if group_cards_2[i] < min_value:
                min_value = group_cards_2[i]
        score_player_2 += 5 * min_value

    # ALLIANCE et TRAHISON : Additionner et soustraire leur valeur
    alliance_cards = ["+2", "+3", "+4"]
    treason_cards = ["-1", "-2", "-3"]
    for i in alliance_cards:
        # ALLIANCE Joueur 1
        if group_cards_1.__contains__(i):
            i = int(i) 
            score_player_1 += i
        # ALLIANCE Joueur 2
        if group_cards_2.__contains__(i):
            i = int(i)
            score_player_2 += i

    for i in treason_cards:
        # TRAHISON Joueur 1
        if group_cards_1.__contains__(i):
            i = int(i)
            score_player_1 += i
        # TRAHISON Joueur 2
        if group_cards_2.__contains__(i):
            i = int(i)
            score_player_2 += i

    return score_player_1, score_player_2

lst_player_1 = {5:4, 6:1, 8:3, "-2":1, "+4":2, "+5":1}
lst_player_2 = {5:3, 6:2, 7:1, 8:3}
# get_scoring(lst_player_1,lst_player_2)

"""Retourne le vainqueur
Compare le score du joueur 1 et du joueur 2 et retourne le vainqueur.
En cas d'égalité, compte quel joueur possède le plus de cartes SOUTIEN 8 et le retorune en vainqueur, si égalité même chose pour les cartes SOUTIEN 7 etc...

Parameters
----------
score_player_1 : int
    Score du joueur 1
score_player_2 : int
    Score du joueur 2
group_cards_1 : collection
    Dictionnaire avec comme clés, les valeurs des cartes et en valeur pour chaque clé le nombre de cartes du joueur 1
group_cards_2 : collection
    Dictionnaire avec comme clés, les valeurs des cartes et en valeur pour chaque clé le nombre de cartes du joueur 2

Returns
-------
[1-2]: int
    Retourn 1 si le joueur 1 remporte la partie et 2 si le joueur 2 remporte la partie
"""
def get_winner(score_player_1, score_player_2, group_cards_1, group_cards_2):
    # Le score du joueur 1 est supérieur au score du joueur 2 => le joueur 1 gagne
    if score_player_1 > score_player_2 :
        print("Le joueur 1 a gagné !")
    # Le score du joueur 1 est inférieur au score du joueur 2 => le joueur 2 gagne
    elif score_player_2 > score_player_1:
        print("Le joueur 2 a gagné !")
    # Sinon égalité
    else : 
        # En cas d'égalité, le joueur ayant le plus de soutien de valeur 8 l'emporte, puis en cas de nouvelle égalité le joueur ayant le plus de soutien de valeur 7 l'emporte etc.
        if group_cards_1._contains_(8) < group_cards_2._contains_(8):
            print("Bien joué, le joueur 1 a plus de 8 !")

        elif group_cards_2._contains_(8) < group_cards_1._contains_(8):
                print("Bien joué, le joueur 2 a plus de 8 !")
        
        elif group_cards_1._contains_(8) == group_cards_2._contains_(8):
            print("Encore une égalité !")
        
        elif group_cards_1._contains_(7) < group_cards_2._contains_(7) :
                print("Bien joué, le joueur 1 a plus de 7 !")
        
        elif group_cards_2._contains_(7) < group_cards_1._contains_(7):
                print("Bien joué, le joueur 2 a plus de 7 !")
        
        elif group_cards_1._contains_(7) == group_cards_2._contains_(7):
            print("Encore une égalité !")
        
        elif group_cards_1._contains_(6) < group_cards_2._contains_(6) :
                print("Bien joué, le joueur 1 a plus de 6 !")
        
        elif group_cards_2._contains_(6) < group_cards_1._contains_(6):
                print("Bien joué, le joueur 2 a plus de 6 !")
        
        elif group_cards_1._contains_(6) == group_cards_2._contains_(6):
            print("Encore une égalité !")

        elif group_cards_1._contains_(5) < group_cards_2._contains_(5) :
                print("Bien joué, le joueur 1 a plus de 5 !")
        
        elif group_cards_2._contains_(5) < group_cards_1._contains_(5):
                print("Bien joué, le joueur 2 a plus de 5 !")
        
        else:
                print("Vous avez fait égalité !")

    exit()

"""Affiche le vainqueur
Concatène "Vainqueur : Joueur"  et le numéro du joueur vainqueur pour l'afficher et quitte le jeu

Parameters
----------
num_player : int
    numéro du joueur vainqueur

Returns
-------
Aucun
"""
def end_game(num_player):
    print(f"-----------Vainqueur : Joueur {num_player}------------")
    exit()

#-------------------- Initialisation de mon dictionnaire players ----------------
# players = {"lst_player_1" : [], "lst_player_2" : [], "lst_collecting_cards_1" : [], "lst_collecting_cards_2" : [], "take_player_1": False, "take_player_2": False}

# #-------------------- Script principal ----------------
# # Initilisation d'une partie
# init_game()

# # Boucler pour lancer 4 manches
# for i in range(4):
    
#     # Distribution des cartes pour chaque manche
#     to_deal(1)
    
#     # Boucler tant que les joueurs possèdent encore des cartes en main et qu'ils n'ont pas tous les 2 pris de cartes sur la table
#     while len(players["lst_player_1"]) > 0 or len(players["lst_player_2"]) > 0 or players["take_player_1"] == False or players["take_player_2"] == False:

#         # Ordre des tours de jeu en fonction du joueur qui coommence la manche
#         # player_order = get_player_order()

#         # Boucler pour les 2 joueurs
#         for player in players:
#             # Afficher le jeu
#             display_game()

#             # Faire jouer un joueur
#             to_play()

# # Remettre la drapeau take des players False
# players["take_player_1"] = False
# players["take_player_2"] = False


# #-------------------- Fin de partie ----------------
# # regrouper les cartes des joueurs pour simplifier le calcul des points
# get_group_cards()

# # Calcul des points pour les 2 joueurs
# player_1_points = get_scoring(players["player_1"])
# player_2_points = get_scoring(players["player_2"])

# # en fonction du nombre de points des joueurs on renvoie le vainqueur ou on départage en cas d'égalité
# if group_cards_1 > player_2_points:
#     print("Le joueur 1 a gagné !")
# elif player_2_points > player_1_points:
#     print("Le joueur 2 a gagné !")
# else:
#     print("Match nul !")