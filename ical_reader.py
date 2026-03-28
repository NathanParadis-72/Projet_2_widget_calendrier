"""
programme pour extraire de l'information pertinente d'un fichier .ical afin de pouvoir l'utiliser dans le widget calendrier

"""





import sys





#fonction pour mieux trier les listes et les rendre plus propres
def trieur_liste(liste_evenement):
    """
    Fonction pour séparer la date de l'heure de début et de fin en deux items dans une liste. crée deux listes de deux items
    a partir des items 1 et 3 de la liste a l'entrée.
    Entrées: liste d'un evenement ical avec la date et heure de début a la position 1, et la date et heure de fin a la position 3
    Sorties: Aucun return, modifie seulement la liste qui entre afin qu'elle formatée comme ceci: une liste
    a la position 1 contenant la date de début et l'heure de fin dans deux items séparés, et une autre liste a la position 3 qui 
    contient la date et l'heure de fin de l'evenement.
    
    """
    for i in range(4):
        if i == 0 or i == 2 or i == 4:
            continue
        else:
            liste_evenement[i] = liste_evenement[i].replace("T", ":")
            liste_evenement[i] = liste_evenement[i].replace("Z", "")
            liste_evenement[i] = liste_evenement[i].split(":")
    



#fonction pour formater les heures en format plus lisible
def formateur_heure(liste_evenement):
    """
    Fonction pour formater des heures de format "HHMMSS" en heures de format "HHhMM"
    Entrées: Liste d'evenement triée par la fonction "trieur liste", afin que les heures soient séparées des dates
    Sorties: Pas de return, modifie seulement la liste afin d'avoir des heures de format HHhMM (13h30 par exemple) pour pouvoir les
    envoyer au code du widget calendrier sans avoir à les traduire plus tard.
    """
    for i in range(4):
        if i == 0 or i == 2 or i == 4:
            continue
        else:
            stringheure = liste_evenement[i][1]
            heure = stringheure[:-2]
            heureformatee = heure[:2] + "h" + heure[2:]
    
            liste_evenement[i][1] = heureformatee




#fonction pour sauvegarder le path du ical entre les utilisations du programme
def sauvegarde_path():
    """
    Fonction pour voir si une sauvegarde du path du fichier ical/ics existe, et si non, elle en crée un fichier de sauvegarde contenant 
    le path du fichier ical/.ics pour les utilisations futures du programme.
    Entrées: Aucune, demande un input de l'utilisateur qu'il placera ensuite dans le fichier de sauvegarde.
    Sorties: Variable contenant le path du fichier ical/ics, et un fichier .txt contenant ce même path.
    """
    validation = False

    while validation == False:
        try: 
            sauvegarde_calendrier = open('sauvegarde_calendrier', "x+")
            
        
            try:
                #input du path directement ou trouver une facon de trouver le fichier a partir du nom?
                pathfichiercal = input("Quel est le path de votre fichier icalendar? (vous pouvez le trouver en faisant 'right-click' sur le" \
                " fichier et en cliquant sur 'copy path') \n\npath: ")

                testpath = open(pathfichiercal, "r")
                testpath.close()
                
                sauvegarde_calendrier.write(pathfichiercal)
                sauvegarde_calendrier.close()
                validation = True

            except FileNotFoundError:
                print("path invalide")

        except FileExistsError:
            sauvegarde_calendrier = open('sauvegarde_calendrier', "r")
            pathfichiercal = sauvegarde_calendrier.read()
            sauvegarde_calendrier.close()

            try:
                testpath = open(pathfichiercal, "r")
                testpath.close()
                validation = True

            except FileNotFoundError:
                print("\npath invalide\n")
                pathfichiercal = input("Quel est le path de votre fichier icalendar? (vous pouvez le trouver en faisant 'right-click' sur le" \
                " fichier et en cliquant sur 'copy path') \n\npath: ")
        
    #fonction test de path ici?

    return pathfichiercal




#mettre les deuxieme try except dans une fonction et les standardiser, mettre le input a la meme place, pareil pour le close(), etc etc










pathfichiercal = sauvegarde_path()


#(pour override le save si jamais tu veux rentrer ton propre path)
# pathfichiercal = r"C:\users\parad\Desktop\test2.ics" 



calendrier = open(pathfichiercal, "r") #open('nomdufichier', 'parametre') le parametre 'r' (litteral) fait que le open peut juste lire le fichier
lirecal = calendrier.read()
calendrier.close() #pas oublier de close le fichier apres l'avoir lu
calpropre = lirecal.replace("\n", ",") #enleve les newlines et les remplace avec des virgules pour pouvoir separer les composantes plus tard
calproprefinal = calpropre.replace(",END:VCALENDAR", "")
listecal = calproprefinal.split("BEGIN:VEVENT") # crée une liste et sépare les items par toutes les fois ou c'est écrit "begin:vevent"

listecal.remove(listecal[0])





#création de la liste mere du calendrier, sert a plus qu'une semaine, changer le nom au besoin! ! !
listesemaine = []





for evenement in listecal:
    #creer une liste a partir des evennements dans la liste du calendrier
    infos_evenement = str(evenement).split(",")
    
    
    #rendre la liste plus propre, enlever les trucs innutiles, seulement garder la date et heures, plus le nom
    infos_evenement.remove(infos_evenement[0]) 
    for i in range(3): infos_evenement.remove(infos_evenement[-1])
    for i in range(6): infos_evenement.remove(infos_evenement[2])
    
    infos_evenement_propre = str(infos_evenement).replace("[", "").replace("]", "").replace("'", "").replace(",", ":")

    #refaire la liste mais en la splittant a des endroits differents pour préparer les clés pour chaque evenement
    liste_evenement = str(infos_evenement_propre).split(":")
    
    


    #fonction pour faire des listes plus propres et mieux triées
    trieur_liste(liste_evenement)

    

    #fonction pour formater les heures pour les rendre plus facile a lire sur le calendrier
    formateur_heure(liste_evenement)
    



    #on crée une nouvelle liste et on rentre les informations de l'evenement dedans
    nouvel_evenement = {"nom" : liste_evenement[5], "debut" : liste_evenement[1], "fin" : liste_evenement[3]}
    
    #et on rajoute la liste de l'événement dans le prochain item de la liste calendrier mere
    listesemaine.append(nouvel_evenement)

    















print(listesemaine)
#print(listesemaine[0]["debut"]) #premier item de la liste d'evenements, clé pour output la liste de date+heure de début, pour seulement avoir l'heure, rajouter [1], pour la date, rajouter [0]












#OU JE SUIS RENDU: je devrais voir si on save comme ca on a pas a refaire tous les calculs a chaque fois qu'on ouvre
#le code, ou et si oui, rajoute un output a un txt file ou un json pour avoir les differents evenements sauvegardés en quelque part



"""
[{'nom': 'TEST2', 'debut': ['20260314', '16h00'], 'fin': ['20260314', '17h00']}, {'nom': 'TESTTESTTEST', 'debut': ['20260312', '13h30'], 'fin': ['20260312', '15h30']}]
= listesemaine
"""







#dictionaire.clear() ou list.clear() ca delete tout dans le dict ou la liste, on va se servir de ca