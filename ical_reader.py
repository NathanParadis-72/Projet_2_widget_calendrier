"""
programme pour extraire de l'information pertinente d'un fichier .ical, afin de pouvoir l'utiliser dans le widget

"""



file_path = r"C:\users\parad\Desktop\testcalendrier.ics"

filecontent = open(file_path, "r") #open('nomdufichier', 'parametre') le parametre 'r' fait que le open peut juste lire le fichier
filestring = filecontent.read()
print(filestring)


