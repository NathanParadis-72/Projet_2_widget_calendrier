import datetime as dt

temps = dt.datetime.now()
#print(temps) #output example: 2026-03-25 08:51:17.747746

#print(temps.strftime("%A, %p")) 
# strftime, string format time, parametres: (tu peux en stack plusieurs: strftime("%1, %2, 3%") )
# %a semaine abréviée: sun mon tue
# %A semaine: sunday monday tuesday
# %b mois abrévié: jan feb mar
# %B mois: january february march
# %d jour du mois: 01 02 03
# %m mois en tant que chiffre: 01 02 03
# %Y année: 2026
# %H heure 24h: 00 01 ... 22 23
# %I heure 12h: 00 01 ... 12 01
# %p AM ou PM: AM PM
# %M minute: 00 01 ... 59
# %S seconde: 00 01 ... 59
# %c date et heure complete: Mon Feb 28 08:30:27 2026




"""
liste = [{"time" : ['20260312', '133000']}]

stringheure = liste[0]["time"][1]
newheure = stringheure[:-2]
newheure2 = newheure[:2] + "h" + newheure[2:]
print(newheure2)

my_string = "hello"
new_string = my_string[:-2] + "l" + my_string[-2:]
print(new_string)
"""






from pathlib import Path


directory = Path(r'C:/Users/parad/Desktop')
liste_test = list(directory.glob('*.ics'))

#print(liste_test)




import os

import urllib.request


try: 

    url = "https://calendar.google.com/calendar/ical/85ab5d95814f9e369157bc1447ed8e2519614f72cdbc364c87e6548fdde37400%40group.calendar.google.com/private-648733675222b475c39e98fbfc425360/basic.ics"
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(script_dir)
    # Extract the filename from the URL
    filename = "testblablabla"
    print(filename)
    # Create the full path
    save_path = os.path.join(script_dir, filename)
    print(save_path)
    urllib.request.urlretrieve(url, save_path)
    print(f"File saved to: {save_path}")
except urllib.error.URLError:
    print("fail")




#fonction non fonctionnelle but took me 4 h so I keep


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
            
        

    return pathfichiercal

