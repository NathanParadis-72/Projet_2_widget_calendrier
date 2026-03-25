from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import *
root = tk.Tk(baseName= 'Coming Week')


#obtient seulement la date d'aujourd'hui
now = datetime.now().date()

#a confirmer ce que cela fait!!!!
root.attributes('-alpha', 0.8)

Lundi_text = [[{"nom de l'evenement": 'evenement du lundi'}, {'temps de debut': '20260312T133000Z'}, {'temps de fin': '20260312T153000Z'}]]

#necessaire a faire fonctionner GUI avec python
var1 = tk.IntVar()
var2 = tk.IntVar()


#rend tout ce qui est rouge, transparent
root.attributes("-transparentcolor", "red")


#bg est pour background color
root.configure(bg='red')

# Label est du texte ecrit. 
lundi = tk.Label(text=f" lundi {now}             ", bg='red', fg='white', font = 20)
lundi.grid(row=0, column=0)
lundi_event = tk.Label(wraplength= 200,  anchor = W, justify= LEFT, text = Lundi_text, bg="red", fg='white', font = ("Arial", 10))
lundi_event.grid(row=1, column=0)


mardi = tk.Label(text = " mardi            ", bg='red', fg='white', font = 20)
mardi.grid (row=0, column=1)


mercredi = tk.Label(text = " mercredi         ", bg='red', fg='white', font = 20)
mercredi.grid (row=0, column=2)


jeudi = tk.Label(text = " jeudi        ", bg='red', fg='white', font = 20)
jeudi.grid (row=0, column=3)


vendredi = tk.Label(text = " vendredi          ", bg='red', fg='white', font = 20)
vendredi.grid (row=0, column=4)


samedi = tk.Label(text = " samedi           ", bg='red', fg='white', font = 20)
samedi.grid (row=0, column=5)


dimanche = tk.Label(text = " dimanche         ", bg='red', fg='white', font = 20)
dimanche.grid (row=0, column=6)


sepmardi = ttk.Separator(root, orient='vertical')

sepmardi.grid(row=0, column=1, columnspan=1,  rowspan=12, sticky="wns" , padx=0, pady=0)

sepmercredi = ttk.Separator(root, orient='vertical')

sepmercredi.grid(row=0, column=2, columnspan=1,  rowspan=12, sticky="wns" , padx=0, pady=0)

sepjeudi = ttk.Separator(root, orient='vertical')

sepjeudi.grid(row=0, column=3, columnspan=1,  rowspan=12,sticky="wns" , padx=0, pady=0)

sepvendredi = ttk.Separator(root, orient='vertical')

sepvendredi.grid(row=0, column=4, columnspan=1,  rowspan=12, sticky="wns" , padx=0, pady=0)

sepsamedi = ttk.Separator(root, orient='vertical')

sepsamedi.grid(row=0, column=5, columnspan=1,  rowspan=12, sticky="wns" , padx=0, pady=0)

sepdimanche = ttk.Separator(root, orient='vertical')

sepdimanche.grid(row=0, column=6, columnspan=1,  rowspan=12, sticky="wns" , padx=0, pady=0)


"""Sticky=tk.W fait que le widget(la coche et texte) colle l'endroit specifie apres le =. W veux dire West. la coche colle 
a gauche de la fenetre. exemple, S en bas."""
tk.Checkbutton(root, text="Fait", variable=var1, bg='red', fg='white').grid(row=7, sticky=tk.W)



root.mainloop()