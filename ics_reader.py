"""
Programme pour extraire de l'information pertinente d'un fichier .ics afin de pouvoir l'utiliser dans le code du 
widget calendrier
Par: Nathan Paradis et Arnaud Baril
Version de remise
"""

import os
import urllib.request





### Définition des fonctions ###


def trieur_liste(liste_evenement):
    """
    Fonction pour séparer la date de l'heure de début et de fin en deux items dans une liste. crée deux listes de
    deux items à partir des items 1 et 3 de la liste à l'entrée.
    Entrées: liste d'un événement .ics avec la date et heure de début à la position 1, et la date et heure de fin 
    à la position 3
    Sorties: Aucun return, modifie seulement la liste qui entre afin qu'elle formatée comme ceci: une liste
    à la position 1 contenant la date de début et l'heure de fin dans deux items séparés, et une autre liste à la
    position 3 qui contient la date et l'heure de fin de l'événement.
    """
    for i in range(4):
        if i % 2 == 0:
            continue
        else:
            liste_evenement[i] = liste_evenement[i].replace("T", ":").replace("Z", "").split(":")



def formateur_heure(liste_evenement):
    """
    Fonction pour formater des heures de format "HHMMSS" en heures de format "HHhMM"
    Entrées: Liste d'événement triée par la fonction "trieur liste", afin que les heures soient séparées 
    des dates
    Sorties: Pas de return, modifie seulement la liste afin d'avoir des heures de format HHhMM (13h30 par exemple)
    pour pouvoir les envoyer au code du widget calendrier sans avoir à les traduire plus tard.
    """
    for i in range(4):
        if i % 2 == 0: 
            continue
        else:
            stringheure = liste_evenement[i][1]
            heure = stringheure[:-2]
            heureformatee = heure[:2] + "h" + heure[2:]
    
            liste_evenement[i][1] = heureformatee



def mise_a_jour_cal(url_cal):
    """
    Fonction pour mettre à jour le fichier .ics dans le repertoire du code
    Entrées: Le url du fichier .ics
    Sorties: Le fichier de sauvegarde de calendrier mis à jour
    """
    #trouve le path du repertoire courant du code
    repertoire_code = os.path.dirname(os.path.abspath(__file__))

    #nommer le fichier de sauvegarde du calendrier
    filename = "sauvegarde_calendrier.ics"

    #crée le path pour le fichier de sauvegarde
    path_sauvegarde_cal = os.path.join(repertoire_code, filename)
    
    #entre les données du calendrier dans un nouveau fichier dans le répertoire du code
    urllib.request.urlretrieve(url_cal, path_sauvegarde_cal)



def extracteur_donnees_cal():
    """
    Fonction pour créer une liste contenant les infos du fichier .ics du calendrier
    Entrées: Aucune
    Sorties: Liste contenant les événements du calendrier
    """
    
    calendrier_ics = open('sauvegarde_calendrier.ics', "r")
    donnees_cal = calendrier_ics.read() #sort les données du fichier .ics
    calendrier_ics.close()
    
    #on enlève les caractères dont on a pas besoin et on prépare la création de liste
    calpropre = donnees_cal.replace("\n", ",").replace(",END:VCALENDAR", "")
    
    #crée une liste et sépare les items par toutes les fois ou c'est écrit "begin:vevent"
    listecal = calpropre.split("BEGIN:VEVENT")
    
    #on enlève l'item 0 puisqu'il ne contient aucun info d'événement
    listecal.remove(listecal[0])


    return listecal



def sauvegarde_calendrier():
    """
    Fonction pour voir si un fichier de sauvegarde avec l'url du calendrier existe, et si oui, mettre son contenu
    dans une varible. Si le fichier n'existe pas, la fonction demande à l'utilisateur d'input l'url de son calendrier
    afin de créer une sauvegarde.
    Entrées: Aucune, demande l'input de l'utilisateur au besoin.
    Sorties: Un fichier .txt contenant le url du calendrier, et une variable contenant le contenu du fichier .ics
    """
    try:
        
        try: 
            sauvegarde_url = open('sauvegarde_url.txt', 'r')
            url_cal = sauvegarde_url.read()
            sauvegarde_url.close()

            mise_a_jour_cal(url_cal)

            listecal = extracteur_donnees_cal()

        except FileNotFoundError:
            #si il ne trouve pas le fichier, il le crée. Premièrement il demande un input
            url_cal = input("Entrez le url secret de votre calendrier google (il se trouve dans 'settings and sharing' > 'integrate " \
            "calendar' > 'secret adress in ical format')\n\nURL: ")
            
            #sauvegarde le url dans un fichier .txt
            sauvegarde_url = open('sauvegarde_url.txt', 'w+')
            sauvegarde_url.write(url_cal)
            sauvegarde_url.close()

            mise_a_jour_cal(url_cal)
            
            listecal = extracteur_donnees_cal()

    except urllib.error.URLError:
        print("Pas de connexion internet, le calendrier se mettra à jour la prochaine fois que vous y aurez acces")
        sauvegarde = open('sauvegarde_calendrier.ics', 'r')
        listecal = sauvegarde.read()
        sauvegarde.close()


    return listecal







### requis pour le projet, cette fonction ne sert pas en dehors du cadre du projet scolaire ###
def output_listemere(listemere): 
    """
    Fonction pour output la liste mère du calendrier dans un fichier text afin d'aller gratouiller tous les points possibles
    sur ce projet
    Entrées: Liste formattée qui sort de la fonction: "formatage_listemere"
    Sorties: fichier text contenant la liste
    """
    fichier_output = open('fichier_liste-mere.txt', 'w+')
    fichier_output.write(str(listemere))
    fichier_output.close()







##### Fonction contenant tout le code necessaire pour widget.py #####

#fonction finale
def formatage_listemere():
    """
    Fonction pour créer une liste mere contenant des dictionnaires d'événements formattées de maniere à pouvoir
    être lue par le code widget.py pour afficher des informations sur des événements dans un calendrier
    Entrées: Aucune
    Sorties: Liste complétée et formattée contenant des dictionnaires qui contiennent les information des 
    événements dans le calendrier
    """
    #création de la liste mere du calendrier
    listemere = []

    #création de la liste d'événements qu'on va utiliser pour le reste du code
    listecal = sauvegarde_calendrier()

    for evenement in listecal:
        #créer une liste à partir des événements dans la liste du calendrier
        infos_evenement = str(evenement).split(",")
        
        
        #rendre la liste plus propre, enlever les trucs innutiles, seulement garder la date et heures, et le nom
        infos_evenement.remove(infos_evenement[0]) 
        for i in range(3): infos_evenement.remove(infos_evenement[-1])
        for i in range(6): infos_evenement.remove(infos_evenement[2])
        
        infos_evenement_propre = str(infos_evenement).replace("[", "").replace("]", "").replace("'", "").replace(",", ":")

        #refaire la liste mais en la séparant à des endroits differents pour préparer les clés pour chaque événement
        liste_evenement = str(infos_evenement_propre).split(":")
        
        

        #fonction pour faire des listes plus propres et mieux triées
        trieur_liste(liste_evenement)


        #fonction pour formater les heures pour les rendre plus facile à lire sur le calendrier
        formateur_heure(liste_evenement)
        


        #on crée un nouveau dictionnaire et on entre les informations de l'événement dedans
        nouvel_evenement = {"nom" : liste_evenement[5], "debut" : liste_evenement[1], "fin" : liste_evenement[3]}
        
        #on rajoute la liste de l'événement dans le prochain item de la liste calendrier mère
        listemere.append(nouvel_evenement)



    #fonction requise pour le projet scolaire, peut être enlevée pour sauver quelques bytes
    output_listemere(listemere)



    return listemere