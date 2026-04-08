# README: Widget calendrier
### Par: Arnaud Baril et Nathan Paradis
<br><br>


# Résumé du projet:
Ce projet est un widget de calendrier pour PC, il permet d'afficher les tâches/événements des 7 prochains jours à partir d'un fichier de calendrier de type .ics, un peu comme la fenêtre calendrier que l'on pourrait voir sur un écran de cellulaire.
<br><br>


# Entrées:
Un URL de calendrier .ics, entré dans le terminal au premier lancement de Widget.py.
<br><br>


# Sorties:
Une fenêtre de style widget qui affiche les informations du fichier .ics sous la forme d'événements avec toutes les informations pertinentes telles que l'heure de début, l'heure de fin et le nom de l'événement.
Le programme crée aussi:
- un fichier de sauvegarde de l'URL du calendrier en format .txt
- un fichier de sauvegarde du calendrier en format .ics
- un fichier de sauvegarde de la liste formatée utilisée dans widget.py en format .txt
<br><br>


# Controle:
Ouvrez Widget.py, l'utilisateur devra entrer un URL particulier dans le terminal (les instructions pour l'obtention de cet URL sont offertes dans le terminal lors de la demande de l'URL). Le programme créera sauvegarde_url.txt. Si sauvegarde_url.txt existe déja, le programme ne demande pas d'URL et met le calendrier à jour.

Pour changer le calendrier affiché, supprimer le fichier "sauvegarde_url.txt". le programme demandera alors un nouvel URL au prochain lancement.

Le calendrier se mettra à jour automatiquement à chaque ouverture du programme si une connection internet est présente.
<br><br>


# Fonctionalités:
Entrer l'URL d'un fichier .ics pour avoir accès à tous les événements des 7 prochains jours du calendrier, classés par journée. 

Le calendrier se met automatiquement à jour grâce au lien URL du calendrier si l'ordinateur à accès à internet.

Si l'ordinateur n'a pas de connexion internet ou que l'adresse entrée est fautive, un message apparait disant que la mise à jour se fera la prochaine fois que le programme sera ouvert.
<br><br>


# Limitations:
- Le calendrier ne doit pas contenir d'événement avec:
  - Une description
  - Des événements partagés
  - Une location
  - Un événement sur plusieurs jours 
  - Un événement qui se répète automatiquement
  - Un titre avec des accents ou des caractères spéciaux (ca ne brise pas le programme mais c'est pas très beau)
- Le calendrier affiche l'heure en Coordinated Universal Time ou UTC, peu importe votre fuseau horaire
- Il est déconseillé d'utiliser un calendrier partagé, il pourrait causer des erreurs
- Une connexion internet est nécessaire à la première utilisation
- Une connexion internet est necessaire pour une mise à jour du calendrier
- Le programme ne peut pas afficher plus d'un calendrier à la fois
<br><br><br><br><br>


### URL de calendrier pour tester le programme ###
https://calendar.google.com/calendar/ical/5c00938c1050bc95afbdd5adff43864f7f85c741f09dd4eeddcebd66574ff589%40group.calendar.google.com/private-932dca24babb4051bff064591932eac5/basic.ics