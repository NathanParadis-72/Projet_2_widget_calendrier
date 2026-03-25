"""
programme pour extraire de l'information pertinente d'un fichier .ical, afin de pouvoir l'utiliser dans le widget

"""



#test de lecture de fichier

fichiercal = r"C:\users\parad\Desktop\test2.ics" #path du fichier (pour mon ordi, va falloir le modifier pour le final)

calendrier = open(fichiercal, "r") #open('nomdufichier', 'parametre') le parametre 'r' fait que le open peut juste lire le fichier
lirecal = calendrier.read()
calpropre = lirecal.replace("\n", ",") #enleve les newlines et les remplace avec des virgules pour pouvoir separer les composantes plus tard
calproprefinal = calpropre.replace(",END:VCALENDAR", "")
listecal = calproprefinal.split("BEGIN:VEVENT") # crée une liste et sépare les items par toutes les fois ou c'est écrit "begin:vevent"


# print(listecal)

listecal.remove(listecal[0])

lundi = [{
    "event1" : "dictionnaire_event"
}]

#remove list item 0 a la place d'ecrire une variable nombre avec une fonction "reverse append"

listelundi = []

for evenement in listecal:
    infos_evenement = str(evenement).split(",")
    
    list(infos_evenement)
    
    #rendre la liste plus propre, enlever les trucs innutiles, seulement garder la date et heures, plus le nom
    infos_evenement.remove(infos_evenement[0]) 
    for i in range(3): infos_evenement.remove(infos_evenement[-1])
    for i in range(6): infos_evenement.remove(infos_evenement[2])
    
    infos_evenement_cleaned = str(infos_evenement).replace("[", "").replace("]", "").replace("'", "").replace(",", ":")

    #refaire la liste mais en la splittant a des endroits differents pour préparer les clés pour chaque evenement
    cles_evenement = str(infos_evenement_cleaned).split(":")
    
    
    #on crée une nouvelle liste et on rentre les informations de l'evenement dedans
    nouvel_evenement = [{"nom de l'evenement" : cles_evenement[5]}, {"temps de debut" : cles_evenement[1]}, {"temps de fin" : cles_evenement[3]}]
    
    #et on la rajoute a la liste de LUNDI (DATE A CHANGER) ! ! ! ! ! ! !
    listelundi.append(nouvel_evenement)





#OU JE SUIS RENDU: jai toutes les données dans des dictionnaires dans des listes, je vais pouvoir commencer a faire une fonction pour calculer les dates
#et les autres fonctions qu'Arnaud a besoin pour son widget, plus je devrais voir si on save comme ca on a pas a refaire tous les calculs a chaque fois qu'on ouvre
#le code, ou et si oui, rajoute un output a un txt file ou un json pour avoir les differents evenements sauvegardés en quelque part




    

print(listelundi)
#print(listelundi[0][0]["tempsdebut"])      #va chercher dans la liste cles evenements, le premier item, et a partir de la on peut prendre la donnée qu'on veut













import datetime #pour avoir des fonctions de date?







#fonction pour mettre des donnés spécifiques de ficher ical dans des variables

def info_evenement(fichier_ical):
    
    for text in fichier_ical:
        """sortir ces infos entre BEGIN:VEVENT et END:VEVENT et les mettre dans variable "text"?"""

        date = "date trouvée dans le ical"
        heuredebut = "heure début trouvée dans ical"
        heurefin = "heure fin trouvée dans ical"
        nom_evenement = "nom d'evenement trouvé dans le ical (summary)"
    return (date, nom_evenement, heuredebut, heurefin)

















#dictionaire.clear() ou list.clear() ca delete tout dans le dict ou la liste, on va se servir de ca