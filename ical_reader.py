"""
programme pour extraire de l'information pertinente d'un fichier .ical, afin de pouvoir l'utiliser dans le widget

"""

#test de lecture de fichier

file_path = r"C:\users\parad\Desktop\testcalendrier.ics" #path du fichier (pour mon ordi, va falloir le modifier pour le final)

filecontent = open(file_path, "r") #open('nomdufichier', 'parametre') le parametre 'r' fait que le open peut juste lire le fichier

filestring = filecontent.read()

print(filestring)


