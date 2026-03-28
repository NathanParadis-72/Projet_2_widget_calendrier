from datetime import datetime, timedelta

import tkinter as tk
from tkinter import ttk
from tkinter import *
root = tk.Tk()

#necessaire a faire fonctionner GUI avec python
var1 = tk.IntVar()
var2 = tk.IntVar()

#obtient seulement la date d'aujourd'hui
jour1 = datetime.now().date()

#cree un nombre a partir de la date pour comparer
now_compare = jour1.strftime("%Y%m%d")

#donne la date des jours a venir avec des additions de journees
jour2 = jour1 + timedelta(days=1)
jour3 = jour2 + timedelta(days=2)
jour4 = jour3 + timedelta(days=3)
jour5 = jour4 + timedelta(days=4)
jour6 = jour5 + timedelta(days=5)
jour7 = jour6 + timedelta(days=6)


#la variable contenant le calendrier.
ical = [{'nom': "Nom de l'evenement", 'debut': ['20260328', '160000z'], 'fin': ['20260314', '170000Z']}, {'nom': 'evenement 2', 'debut': ['20260327', '133000Z'], 'fin': ['20260312', '153000Z']}]

#les listes vide prete a etre remplie pour les 7 jours du calendrier
day1 = []
day2 = []
day3 = []
day4 = []
day5 = []
day6 = []
day7 = []


def Finalcalendar(day):
    now_compare = day.strftime("%Y%m%d")
    horaire = ""
    for event in range(len(ical)):
    if ical[event]['debut'][0] == now_compare:
        day1.append(ical[event])
    
    for event in range(len(day)):
       horaire += f"{day[event]['nom']}\n start:{day[event]['debut'][1]}\n end:{day[event]['fin'][1]}\n\n "
    return horaire


for event in range(len(ical)):
    if ical[event]['debut'][0] == now_compare:
        day1.append(ical[event])


def journee(day):
    horaire = ""
    for event in range(len(day)):
       horaire += f"{day[event]['nom']}\n start:{day[event]['debut'][1]}\n end:{day[event]['fin'][1]}\n\n "
    return horaire



#rend tout ce qui est rouge, transparent
root.attributes("-transparentcolor", "red")


#bg est pour background color
root.configure(bg='red')

# Label est du texte ecrit. 
day1cal = tk.Label(text=f" {jour1}             ", bg='red', fg='white', font = 20)
day1cal.grid(row=0, column=0)
day1_event = tk.Label(wraplength= 200,  anchor = W, justify= LEFT, text = f" {journee(day1)}", bg="red", fg='white', font = ("Arial", 10))
day1_event.grid(row=1, column=0)


day2cal = tk.Label(text = f" {jour2}             ", bg='red', fg='white', font = 20)
day2cal.grid (row=0, column=1)


day3cal = tk.Label(text = f" {jour3}         ", bg='red', fg='white', font = 20)
day3cal.grid (row=0, column=2)


day4cal = tk.Label(text = f" {jour4}        ", bg='red', fg='white', font = 20)
day4cal.grid (row=0, column=3)


day5cal = tk.Label(text = f" {jour5}          ", bg='red', fg='white', font = 20)
day5cal.grid (row=0, column=4)


day6cal = tk.Label(text = f" {jour6}           ", bg='red', fg='white', font = 20)
day6cal.grid (row=0, column=5)


day7cal = tk.Label(text = f" {jour7}         ", bg='red', fg='white', font = 20)
day7cal.grid (row=0, column=6)


sepmardi = ttk.Separator(orient='vertical')

sepmardi.grid(row=0, column=1, columnspan=1,  rowspan=12, sticky="wns")

sepmercredi = ttk.Separator(orient='vertical')

sepmercredi.grid(row=0, column=2, columnspan=1,  rowspan=12, sticky="wns")

sepjeudi = ttk.Separator(orient='vertical')

sepjeudi.grid(row=0, column=3, columnspan=1,  rowspan=12,sticky="wns")

sepvendredi = ttk.Separator(orient='vertical')

sepvendredi.grid(row=0, column=4, columnspan=1,  rowspan=12, sticky="wns")

sepsamedi = ttk.Separator(orient='vertical')

sepsamedi.grid(row=0, column=5, columnspan=1,  rowspan=12, sticky="wns")

sepdimanche = ttk.Separator(orient='vertical')

sepdimanche.grid(row=0, column=6, columnspan=1,  rowspan=12, sticky="wns")


"""Sticky=tk.W fait que le widget(la coche et texte) colle l'endroit specifie apres le =. W veux dire West. la coche colle 
a gauche de la fenetre. exemple, S en bas."""
tk.Checkbutton(root, text="Fait", variable=var1, bg='red', fg='white').grid(row=7, sticky=tk.W)



root.mainloop()

