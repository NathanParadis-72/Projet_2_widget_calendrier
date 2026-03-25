from datetime import datetime, timedelta

import tkinter as tk
from tkinter import ttk
from tkinter import *
root = tk.Tk(baseName= 'Coming Week')


#obtient seulement la date d'aujourd'hui
now = datetime.now().date()

#cree un nombre a partir de la date pour comparer
now_compare = datetime.now().strftime("%y%m%d")

#donne la date des jours a venir avec des additions de journees
jour2 = now + timedelta(days=1)
jour3 = now + timedelta(days=2)
jour4 = now + timedelta(days=3)
jour5 = now + timedelta(days=4)
jour6 = now + timedelta(days=5)
jour7 = now + timedelta(days=6)

liste_lundi = [{"nom": 'nom event', 'debut': '20260314T160000Z', 'temps de fin': '20260314T170000Z'}, {"nom de l'evenement": 'TESTTESTTEST', 'temps de debut': '20260312T133000Z', 'temps de fin': '20260312T153000Z'}]

#necessaire a faire fonctionner GUI avec python
var1 = tk.IntVar()
var2 = tk.IntVar()


#rend tout ce qui est rouge, transparent
root.attributes("-transparentcolor", "red")


#bg est pour background color
root.configure(bg='red')

# Label est du texte ecrit. 
lundi = tk.Label(text=f" {now}             ", bg='red', fg='white', font = 20)
lundi.grid(row=0, column=0)
lundi_event = tk.Label(wraplength= 200,  anchor = W, justify= LEFT, text = f"{liste_lundi[0]["nom"]}\n {liste_lundi[0]["debut"]}" , bg="red", fg='white', font = ("Arial", 10))
lundi_event.grid(row=1, column=0)


mardi = tk.Label(text = f" {jour2}             ", bg='red', fg='white', font = 20)
mardi.grid (row=0, column=1)


mercredi = tk.Label(text = f" {jour3}         ", bg='red', fg='white', font = 20)
mercredi.grid (row=0, column=2)


jeudi = tk.Label(text = f" {jour4}        ", bg='red', fg='white', font = 20)
jeudi.grid (row=0, column=3)


vendredi = tk.Label(text = f" {jour5}          ", bg='red', fg='white', font = 20)
vendredi.grid (row=0, column=4)


samedi = tk.Label(text = f" {jour6}           ", bg='red', fg='white', font = 20)
samedi.grid (row=0, column=5)


dimanche = tk.Label(text = f" {jour7}         ", bg='red', fg='white', font = 20)
dimanche.grid (row=0, column=6)


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

