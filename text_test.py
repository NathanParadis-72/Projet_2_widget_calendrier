import datetime as dt

temps = dt.datetime.now()
print(temps) #output example: 2026-03-25 08:51:17.747746

print(temps.strftime("%A, %p")) 
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

print(liste_test)

