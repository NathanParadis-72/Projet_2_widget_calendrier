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
calendrier = [{'nom': 'ANOTHER', 'debut': ['20260403', '09h30'], 'fin': ['20260403', '18h00']}, {'nom': 'TESTTESTTEST', 'debut': ['20260312', '13h30'], 'fin': ['20260312', '15h30']}, {'nom': 'TEST2', 'debut': ['20260314', '16h00'], 'fin': ['20260314', '17h00']}, {'nom': 'THIS IS TEST', 'debut': ['20260331', '22h00'], 'fin': ['20260401', '01h30']}]


"""
Fonction gerant l'affichage des evenements, des dates et leur positionnnement dans le GUI.
Input: La date represente la date actuelle ou futur. evenements est quel evenement du ical sera mis dans l'affichage.
Colonne est pour positionner la date et positionner les separateurs dans le GUI.
output: Les evenements formater d'une journee, sous la date, dans la bonne colonne du GUI
"""

def affichage(evenements,date,colonne):
    horaire = ""
    date_du_jour = tk.Label(text=f"       {date}      ", bg = 'red', fg ='white', font = 20)
    date_du_jour.grid(row = 0, column = colonne)
    now_compare = date.strftime("%Y%m%d") 
    for event in range(len(calendrier)):
        if calendrier[event]['debut'][0] == now_compare:
            evenements.append(calendrier[event])
    for event in range(len(evenements)):
       horaire += f"{evenements[event]['nom']}\n start:{evenements[event]['debut'][1]}\n end:{evenements[event]['fin'][1]}\n\n "
    evenement_du_jour = tk.Label(wraplength= 400,  anchor = tk.W, justify= tk.LEFT, text = f" {horaire}", bg="red", fg='white', font = ("Arial", 10))
    evenement_du_jour.grid(row = 1, column = colonne)
    separateur = ttk.Separator(orient='vertical')
    separateur.grid(row=0, column=colonne, columnspan=1,  rowspan=12, sticky="wns")



for i in range(7):
    date = jour1 + timedelta(days = i)
    evenements = []
    affichage(evenements, date, i)

root.mainloop()