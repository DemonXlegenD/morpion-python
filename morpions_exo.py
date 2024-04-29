#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------<<<Morpion>>>-------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------------------------------------------------------------------#
"""------------------------------------------------------------DEBUT DES FONCTIONS--------------------------------------------------------------------"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------#


#Verifie si le joueur a gagné la partie, renvoie False pour arreter la partie en cours lorsqu'il a gagné et renvoie True lorsque ce n'est pas terminé
def verifie(m,joueur):

    #gagné par une ligne
    if(m[0]==[joueur,joueur,joueur] or m[1]==[joueur,joueur,joueur] or m[2]==[joueur,joueur,joueur]):
        
        print("Le joueur " + ("1" if (joueur=="X") else "2") + f" a gagné par une ligne de {joueur}")
        return False

    #gagné par une colonne
    elif((m[0][0]==joueur and m[1][0]==joueur and m[2][0]==joueur)
        or (m[0][1]==joueur and m[1][1]==joueur and m[2][1]==joueur)
        or (m[0][2]==joueur and m[1][2]==joueur and m[2][2]==joueur)):

        print("Le joueur " + ("1" if (joueur=="X") else "2") + f" a gagné par une colonne de {joueur}")
        return False

    #gagné par une diagonale
    elif((m[0][0]==joueur and m[1][1]==joueur and m[2][2]==joueur)
        or (m[0][2]==joueur and m[1][1]==joueur and m[2][0]==joueur)):

        print("Le joueur " + ("1" if (joueur=="X") else "2") + f" a gagné par une diagonale de {joueur}")
        return False
    
    #pas gagné
    else:
        return True

#affiche les cases encore disponibles
def affiche_case(liste):
    string = ""
    string = string.join(str(elem)+", " if elem!=liste[-1] else str(elem) for elem in liste)
    return string

#affiche le jeu de morpion
def affiche_morpion(m):
    
    print("-------")
    for i in range(len(m)):
        ligne= "|"
        for j in range(len(m[i])):
            if(m[i][j]==-1):
                ligne += " "
            else:
                ligne += str(m[i][j])
            ligne += "|"
        print(ligne)
        print("-------")
    
#calcul le reste d'un nombre
def calcul_reste(nombre):
    #%: modulo
    return nombre%3

#calcul la division entière d'un nombre
def calcul_div_ent(nombre):
    #// pour division entière, on aurait pu aussi faire int(nombre/3)
    return nombre//3

#ajoute un X ou un O (selon le joueur) dans le morpion
def ajoute_dans_morpion(joueur,num_case,cases,m):

    #si le numéro rentré est dans la liste des cases disponibles
    if(num_case in cases):
        #on insert "X" ou "O" dans la case choisie
        m[calcul_div_ent(case)][calcul_reste(case)] = joueur
        #retire de la liste la case remplie
        cases.remove(num_case)
        return False

    #si le numéro est déjà emprunté
    else:
        print("La case choisie est déjà remplie.\nChoissisez-en une vide!\n")
        return True


#-------------------------------------------------------------------------------------------------------------------------------------------------------#
"""-------------------------------------------------------------FIN DES FONCTIONS---------------------------------------------------------------------"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------------------------------------------------------------------#
"""-------------------------------------------------------------DEBUT DU PROGRAMME--------------------------------------------------------------------"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------#


print("Bonjour et bienvenue sur le jeu morpions.")

#Variable qui démare la partie
running = False
lancer = True

#Le joueur choisit de lancer ou non la partie
while lancer:
    try:
        answer=input("Souhaitez-vous lancer une partie? [Y/N] ").upper()
    except:
        print("\nVeuillez choisir Y ou N")

    #si le joueur ne veut pas lancer de partie
    if (answer == "Y" or answer== "YES"):
        lancer = False
        running = True  

    #si le joueur décide de lancer une partie
    elif (answer == "N" or answer == "NO"):
        lancer = False
        print("Au revoir...")

    #si un autre nombre 
    else:
        print("\nVeuillez choisir Y ou N")

#lancement de la partie
while running:
    
    jouer = True
    #morpion de départ (-1 car 0 correspondra au numéro d'une case: pour ne pas avoir d'ambiguïté dans des fonctions)
    morpion = [[-1,-1,-1]
              ,[-1,-1,-1]
              ,[-1,-1,-1]]
    """caractèristiques du joueur 1"""      
    #symbole du joueur 1
    joueur_1 = "X"
    #le joueur 1 commencera la partie en premier
    joueur_1_is_playing = True
    #symbole du joueur 2
    joueur_2 = "O"
    #le joueur 1 commencera la partie après que le joueur 1 ait joué
    joueur_2_is_playing = False

    #cases du morpions
    cases = [0,1,2,3,4,5,6,7,8]

    #quelles cases à quelle numéro
    morpion_description = [[0,1,2]
                            ,[3,4,5]
                            ,[6,7,8]]

    print("Voici comment sont numérotées les cases:\n")

    affiche_morpion(morpion_description)

    print("\nLorsque vous rentrerez un numéro entre 0 et 8, cela remplira la case de ce numéro-là automatiquement.\nA vous de jouer et bonne chance!\n")

    #lancement des tours par tours
    while jouer and running:

        #Tour du joueur 1
        while joueur_1_is_playing:
            print("Tour du joueur 1\n")

            try:
                case = int(input(f"Choississez une case ({affiche_case(cases)}) : "))

                #la case est bien comprise entre 0 et 8
                if(case>=0 and case<=8):
                    joueur_1_is_playing = ajoute_dans_morpion(joueur_1, case, cases, morpion)

                    #si la case n'est pas prise
                    if not(joueur_1_is_playing):
                        affiche_morpion(morpion)
                        joueur_2_is_playing = verifie(morpion,joueur_1)
                        jouer = joueur_2_is_playing

                #la case est un autre nombre
                else:
                    print("\nVeuillez choisir un nombre valide\n")
            except:
                print("\nVeuillez choisir un nombre valide\n")

        #Lorsque toutes les cases sont remplises, on arrête la partie (il est placé ici dans l'algorithme car le joueur 1 est le premier à commencer et à finir dans le pire des cas)
        if(cases==[] and joueur_2_is_playing):
            joueur_2_is_playing = False
            jouer = joueur_2_is_playing
            print("\nAucun des deux joueurs n'a gagné la partie...")

        #Tour du joueur 2
        while joueur_2_is_playing:
            print("Tour du joueur 2\n")

            try:

                case = int(input(f"Choississez une case ({affiche_case(cases)}) : "))

                if(case>=0 and case<=8):

                    joueur_2_is_playing = ajoute_dans_morpion(joueur_2, case, cases, morpion)

                    if not(joueur_2_is_playing):

                        affiche_morpion(morpion)
                        joueur_1_is_playing = verifie(morpion, joueur_2)
                        jouer = joueur_1_is_playing

                #la case est un autre nombre
                else:
                    print("\nVeuillez choisir un nombre valide\n")

            except:
                print("\nVeuillez choisir un nombre valide")

            
        
        
    
    
    print("\nMerci à vous d'avoir jouer!\n")
    question= True

    #demande au joueur s'il veut rejouer
    while question:
        try:
            continuer = (input("Voulez-vous rejouer? [Y/N]")).upper()
            #le joueur veut continuer
            if(continuer=="Y" or continuer == "YES"):
                question = False
                running= True
                print("\nEt c'est repartit pour un tour!!!")
            
            #le joueur veut arrêter
            elif(continuer=="N" or continuer == "NO"):
                question = False
                running = False
                print("\nAu plaisir de vous revoir!")
            
            #il a rentrer autre chose que Y ou N
            else:
                print("\nRentrez Y ou N")
        except:
            print("\nVeuillez rentrer une valeur valide")

        
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
"""--------------------------------------------------------------FIN DU PROGRAMME---------------------------------------------------------------------"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------#



#TEST des possibilités avec chaque joueur (ne pas oublier de passer lancer en False avant de tester)

""""            
joueur_1 = "X"
joueur_2 = "O"

#j1 gagne
morpion1 = [["X",-1,-1]
              ,["X",-1,-1]
              ,["X",-1,-1]]

verifie(morpion1,joueur_1)


morpion3 = [[-1,"X",-1]
              ,[-1,"X",-1]
              ,[-1,"X",-1]]

verifie(morpion3,joueur_1)

morpion5 = [[-1,"X",-1]
              ,[-1,"X",-1]
              ,[-1,"X",-1]]

verifie(morpion5,joueur_1)

morpion7 = [["X","X","X"]
              ,[-1,-1,-1]
              ,[-1,-1,-1]]

verifie(morpion7,joueur_1)

morpion9 = [[-1,-1,-1]
              ,["X","X","X"]
              ,[-1,-1,-1]]

verifie(morpion9,joueur_1)

morpion11 = [[-1,-1,-1]
              ,[-1,-1,-1]
              ,["X","X","X"]]

verifie(morpion11,joueur_1)

morpion13 = [[-1,-1,"X"]
              ,[-1,"X",-1]
              ,["X",-1,-1]]

verifie(morpion13,joueur_1)

morpion15 = [["X",-1,-1]
              ,[-1,"X",-1]
              ,[-1,-1,"X"]]

verifie(morpion15,joueur_1)

#j2 gagne
morpion2 = [["O",-1,-1]
              ,["O",-1,-1]
              ,["O",-1,-1]]

verifie(morpion2,joueur_2)

morpion4 = [[-1,"O",-1]
              ,[-1,"O",-1]
              ,[-1,"O",-1]]

verifie(morpion4,joueur_2)



morpion6 = [[-1,-1,"O"]
              ,[-1,-1,"O"]
              ,[-1,-1,"O"]]

verifie(morpion6,joueur_2)

morpion8 = [["O","O","O"]
              ,[-1,-1,-1]
              ,[-1,-1,-1]]

verifie(morpion8,joueur_2)

morpion10 = [[-1,-1,-1]
              ,["O","O","O"]
              ,[-1,-1,-1]]

verifie(morpion10,joueur_2)

morpion12 = [[-1,-1,-1]
              ,[-1,-1,-1]
              ,["O","O","O"]]

verifie(morpion12,joueur_2)

morpion14 = [[-1,-1,"O"]
              ,[-1,"O",-1]
              ,["O",-1,-1]]

verifie(morpion14,joueur_2)

morpion16 = [["O",-1,-1]
              ,[-1,"O",-1]
              ,[-1,-1,"O"]]

verifie(morpion16,joueur_2)

"""