from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk

#fait apparaitre de GUI
root = tk.Tk()

#configure rend le background rouge et attribute rend tout ce qui est rouge transparent
root.configure(bg='red')
root.attributes("-transparentcolor", "red")

root.overrideredirect(True) #



#obtient seulement la date d'aujourd'hui
jour1 = datetime.now().date()

#la variable contenant le calendrier.
calendrier = [{'nom': "Nom de l'evenement", 'debut': ['20260401', '160000z'], 'fin': ['20260314', '170000Z']}, {'nom': 'evenement 2', 'debut': ['20260329', '133000Z'], 'fin': ['20260312', '153000Z']}]


"""
Fonction gerant l'affichage des evenements, des dates et leur positionnnement dans le GUI.
Input: La date represente la date actuelle ou futur. evenements est quel evenement du ical sera mis dans l'affichage.
Colonne est pour positionner la date et positionner les separateurs dans le GUI.
output: Les evenements formater d'une journee, sous la date, dans la bonne colonne du GUI
"""

def affichage(evenements,date,colonne):
    horaire = ""
    date_du_jour = tk.Label(text=f"  {(date.strftime("%a"))}  {date} ", bg = 'red', fg = 'cyan', font = ('Helvetica', 12, "bold")) #cree le label en haut de la journee avec la date et le jour.
    date_du_jour.grid(row = 0, column = colonne) #positionnement de la date
    now_compare = date.strftime("%Y%m%d") 
    for event in range(len(calendrier)): #pour chaque evenement du calendrier, regarde si les dates correspondent.
        if calendrier[event]['debut'][0] == now_compare: 
            evenements.append(calendrier[event])
    for event in range(len(evenements)): #chaque evenement est rajoutee a la bonne journee et est formater pour etre lisible.
       horaire += f"{evenements[event]['nom']}\n start:{evenements[event]['debut'][1]}\n end:{evenements[event]['fin'][1]}\n\n "
    evenement_du_jour = tk.Label(wraplength= 300,  anchor = tk.W, justify= tk.LEFT, text = f" {horaire}", bg="red", fg='white', font = ("Arial", 10))
    evenement_du_jour.grid(row = 1, column = colonne)
    separateur = ttk.Separator(orient='vertical')
    separateur.grid(row=0, column=colonne, columnspan=1,  rowspan=12, sticky="wns")


#Sert pour faire les 7 jours du calendrier. chaque loop fait remplie une journee.
for i in range(7):
    date = jour1 + timedelta(days = i)
    evenements = []
    affichage(evenements, date, i)

#Maintient le GUI existant
root.mainloop() 