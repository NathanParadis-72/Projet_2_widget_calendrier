"""
programme pour extraire de l'information pertinente d'un fichier .ical, afin de pouvoir l'utiliser dans le widget

"""


"""
#test de lecture de fichier

file_path = r"C:\users\parad\Desktop\test2.ics" #path du fichier (pour mon ordi, va falloir le modifier pour le final)

filecontent = open(file_path, "r") #open('nomdufichier', 'parametre') le parametre 'r' fait que le open peut juste lire le fichier

filestring = filecontent.read()

print(filestring)

"""



#dictionnaires de la semaine

lundi = {
    "blabla" : "hello"
}

mardi = {

}

mercredi = {

}

jeudi = {

}

vendredi = {

}

samedi = {

}

dimanche = {

}


# liste des dictionnaires
dictlist = [lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche]



#fonction pour rajouter des événements aux dictionnaire apres avoir lu le fichier ical

#utiliser une for loop pour append des nouveaux events a chaque jour

#for event in calendar_file:
dictlist[0]["nom evenement"] = "nouvelle valeur" #va chercher dans la liste le dictionnaire de la journée et rajoute une nouvelle key




