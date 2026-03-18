import tkinter as tk

root = tk.Tk(baseName= 'Coming Week')

root.attributes('-alpha', 0.8)



#necessaire a faire fonctionner GUI avec python
var1 = tk.IntVar()
var2 = tk.IntVar()


#rend toout ce qui est rouge, transparent
root.attributes("-transparentcolor", "red")


#bg est pour background color
root.configure(bg='red')
# Widgets are added here
lundi = tk.Label(root, text="lundi              ", bg='red', fg='white', font = 20)
lundi.grid(row=0, column=0)


mardi = tk.Label(root, text = "mardi            ", bg='red', fg='white', font = 20)
mardi.grid (row=0, column=1)


mercredi = tk.Label(root, text = "mercredi         ", bg='red', fg='white', font = 20)
mercredi.grid (row=0, column=2)


jeudi = tk.Label(root, text = "jeudi        ", bg='red', fg='white', font = 20)
jeudi.grid (row=0, column=3)


vendredi = tk.Label(root, text = "vendredi          ", bg='red', fg='white', font = 20)
vendredi.grid (row=0, column=4)


samedi = tk.Label(root, text = "samedi           ", bg='red', fg='white', font = 20)
samedi.grid (row=0, column=5)


dimanche = tk.Label(root, text = "dimanche         ", bg='red', fg='white', font = 20)
dimanche.grid (row=0, column=6)



separator = tk.Separator(root, orient='vertical')

separator.grid(row=0, column=1, rowspan=2, sticky='ns', padx=5, pady=5)


"""Sticky=tk.W fait que le widget(la coche et texte) colle l'endroit specifie apres le =. W veux dire West. la coche colle 
a gauche de la fenetre. exemple, S en bas."""
tk.Checkbutton(root, text="Fait", variable=var1, bg='red', fg='white').grid(row=7, sticky=tk.W)



root.mainloop()