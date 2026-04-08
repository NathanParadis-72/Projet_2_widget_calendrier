"""
Nom du projet: Calendrier du moment
Par: Arnaud Baril & Nathan Paradis
Version de remise
"""

from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
from ical_reader import formatage_listemere

#fait apparaitre de GUI.
root = tk.Tk()

#.configure rend le background rouge et .attribute rend tout ce qui est rouge transparent.
root.configure(bg='red')
root.attributes("-transparentcolor", "red")

#obtient seulement la date d'aujourd'hui.
jour1 = datetime.now().date()

#la variable contenant le calendrier.
calendrier = formatage_listemere() #voir notes ical_reader



def affichage(evenements,date,colonne):
    """
    Fonction gerant l'affichage des evenements, des dates et leur positionnnement dans le GUI.
    Input: La date represente la date la journee du calendrier qui sera afficher et remplie. evenements est quel evenement du ical sera mis dans l'affichage.
    Colonne est pour positionner la date et positionner les separateurs dans le GUI.
    output: Les evenements formater d'une journee, sous la date, dans la bonne colonne du GUI
    """
    horaire = ""
    date_du_jour = tk.Label(text=f"  {(date.strftime("%a"))}  {date} ", bg = 'red', fg = 'cyan', font = ('Helvetica', 12, "bold")) #cree le label en haut de la journee avec la date et le jour.
    date_du_jour.grid(row = 0, column = colonne) #positionnement de la date.
    now_compare = date.strftime("%Y%m%d") 
    for event in range(len(calendrier)): #pour chaque evenement du calendrier, regarde si les dates correspondent.
        if calendrier[event]['debut'][0] == now_compare: 
            evenements.append(calendrier[event])
    for event in range(len(evenements)): #chaque evenement est rajoutée à la bonne journee et est formatée pour être lisible.
       horaire += f"{evenements[event]['nom']}\n start:{evenements[event]['debut'][1]}\n end:{evenements[event]['fin'][1]}\n\n "
    evenement_du_jour = tk.Label(wraplength= 300,  anchor = tk.W, justify= tk.LEFT, text = f" {horaire}", bg="red", fg='white', font = ("Arial", 10))
    evenement_du_jour.grid(row = 1, column = colonne)
    separateur = ttk.Separator(orient='vertical')
    separateur.grid(row=0, column=colonne, columnspan=1,  rowspan=12, sticky="wns")


#chaque loop remplit une journée du calendrier.
for i in range(7):
    date = jour1 + timedelta(days = i)
    evenements = []
    affichage(evenements, date, i)

#Maintient le GUI existant.
root.mainloop() 