"""
programme pour extraire de l'information pertinente d'un fichier .ical, afin de pouvoir l'utiliser dans le widget

"""



#test de lecture de fichier

fichiercal = r"C:\users\parad\Desktop\test2.ics" #path du fichier (pour mon ordi, va falloir le modifier pour le final)

calendrier = open(fichiercal, "r") #open('nomdufichier', 'parametre') le parametre 'r' fait que le open peut juste lire le fichier
lirecal = calendrier.read()
calpropre = lirecal.replace("\n", ",") #enleve les newlines et les remplace avec des virgules pour pouvoir separer les composantes plus tard
listecal = calpropre.split("BEGIN:VEVENT") # crée une liste et sépare les items par toutes les fois ou c'est écrit "begin:vevent"


print(listecal)



#remove list item 0 a la place d'ecrire une variable nombre avec une fonction "reverse append"

nombre = 1
for item in listecal:
    evennement = listecal[nombre]
    options = str(evennement).split(",")
    print(evennement)

    nombre += 1












import datetime #pour avoir des fonctions de date



#dictionnaires de la semaine

lundi = [{
    "event1" : "dictionnaire_event"
}]

mardi = []


mercredi = []

jeudi = []

vendredi = []

samedi = []

dimanche = []


# liste des dictionnaires
dictlist = [lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche]



#fonction pour mettre des donnés spécifiques de ficher ical dans des variables

def infos_evenement(fichier_ical):
    
    for text in fichier_ical:
        """sortir ces infos entre BEGIN:VEVENT et END:VEVENT et les mettre dans variable "text"?"""

        date = "date trouvée dans le ical"
        heuredebut = "heure début trouvée dans ical"
        heurefin = "heure fin trouvée dans ical"
        nom_evenement = "nom d'evennement trouvé dans le ical (summary)"
    return (date, nom_evenement, heuredebut, heurefin)

















#fonction pour rajouter des événements aux dictionnaire apres avoir lu le fichier ical

#utiliser une for loop pour append des nouveaux events a chaque jour


def rajout_evenement_dict(date, nom, heuredebut, heurefin):

    date = 20260318
    semaine = date + 7

    while date < semaine:

        for event in fichier_ical:
            journee = "date" #date de la journée qu'on veut dans une variable qu'on modifie a priori, trouver la date dans le ical
            dictlist[journee]["nom evenement"] = "valeur nom" #va chercher dans la liste le dictionnaire de la journée et rajoute une nouvelle key
            dictlist[journee]["date"] = date #date en int
            dictlist[journee]["heure début"] = "valeur heure int"
            dictlist[journee]["heure fin"] = "valeur heure int (ex: 1315 pour 1h15 de l'apres midi)"



#dictionaire.clear() ou list.clear() ca delete tout dans le dict ou la liste, on va se servir de ca




# .append a la liste qui a pas besoin de nom exemple list[1,2,3,4 etc] quand tu append a une liste ca lui donne un chiffre
# les positions dans la liste sont des dicts pour chaque event, la liste = le jour de la semaine