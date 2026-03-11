import tkinter as tk

root = tk.Tk(baseName= 'Coming Week')
# Widgets are added here
label = tk.Label(root, text="Prochain 7 jours")
label.grid(row=0, column=0)
var1 = tk.IntVar()
var2 = tk.IntVar()

"""Sticky=tk.W fait que le widget(la coche et texte) colle l'endroit specifie apres le =. W veux dire West. la coche colle 
a gauche de la fenetre. exemple, S en bas."""
tk.Checkbutton(root, text="Fait", variable=var1).grid(row=1, sticky=tk.W)



root.mainloop()