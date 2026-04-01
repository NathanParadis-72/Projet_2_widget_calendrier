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




url = "https://calendar.google.com/calendar/ical/85ab5d95814f9e369157bc1447ed8e2519614f72cdbc364c87e6548fdde37400%40group.calendar.google.com/private-648733675222b475c39e98fbfc425360/basic.ics"
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
# Extract the filename from the URL
filename = url.split("/")[-1]
print(filename)
# Create the full path
save_path = os.path.join(script_dir, filename)
print(save_path)
urllib.request.urlretrieve(url, save_path)
print(f"File saved to: {save_path}")