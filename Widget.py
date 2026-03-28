from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk

#fait apparaitre de GUI
root = tk.Tk()

#configure rend le background rouge et suite attribute rend tout ce qui est rouge transparent
root.configure(bg='red')
root.attributes("-transparentcolor", "red")

#obtient seulement la date d'aujourd'hui
jour1 = datetime.now().date()

#la variable contenant le calendrier.
ical = [{'nom': "Nom de l'evenement", 'debut': ['20260328', '160000z'], 'fin': ['20260314', '170000Z']}, {'nom': 'evenement 2', 'debut': ['20260329', '133000Z'], 'fin': ['20260312', '153000Z']}]

def affichage(day,jour,colonne):
    daycal = tk.Label(text=f"       {jour}      ", bg = 'red', fg ='white', font = 20)
    daycal.grid(row = 0, column = colonne)
    now_compare = jour.strftime("%Y%m%d")
    horaire = ""
    for event in range(len(ical)):
        if ical[event]['debut'][0] == now_compare:
            day.append(ical[event])
    for event in range(len(day)):
       horaire += f"{day[event]['nom']}\n start:{day[event]['debut'][1]}\n end:{day[event]['fin'][1]}\n\n "
    day_event = tk.Label(wraplength= 400,  anchor = tk.W, justify= tk.LEFT, text = f" {horaire}", bg="red", fg='white', font = ("Arial", 10))
    day_event.grid(row = 1, column = colonne)
    separateur = ttk.Separator(orient='vertical')
    separateur.grid(row=0, column=colonne, columnspan=1,  rowspan=12, sticky="wns")

for i in range(7):
    agenda = jour1 + timedelta(days = i)
    day = []
    affichage(day, agenda, i)

root.mainloop()

