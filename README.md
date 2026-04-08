# README: Widget calendrier
### Par: Arnaud Baril et Nathan Paradis
<br><br>


# Résumé du projet:
Ce projet est un widget de calendrier pour PC, il permet de voir les taches/evenement des 7 prochains jours a partir d'un fichier de calendrier de type .ical/.ics, un peu comme la fenetre calendrier que l'on pourrait voir sur un écran de cellulaire.
<br><br>


# Entrées:
Un url de calendrier .ical/.ics, entré dans le terminal au premier lancement du programme.
<br><br>


# Sorties:
Une fenetre de style widget sur votre écran d'ordinateur qui affiche les informations du fichier .ical/.ics sous la forme d'événements avec toutes les informations pertinentes telles que l'heure de début, l'heure de fin et le nom de l'événement.
<br><br>


# Controle:
Au démarrage du programme, l'utilisateur devra entrer un url particulier dans le terminal (les instructions sont affichées, il s'agit de "l'url secret" du calendrier google de l'utilisateur), cet url s'occupe d'aller chercher les informations dans le calendrier de l'utilisateur ainsi que de le mettre à jour à chaque lancement du programme. Si l'url existe deja dans sauvegarde_url.txt (créé automatiquement à la première utilisation), le programme ne demande pas d'url et met le calendrier à jour.

Pour changer le calendrier affiché, supprimer le fichier "sauvegarde_url.txt". le programme demandera alors un nouvel url au prochain lancement.

Après la sauvegarde de l'url, le programme crée, au besoin, et sauvegarde automatiquement, la version la plus récente du calendrier dans un fichier .ics, afin de pouvoir continuer à utiliser le calendrier hors ligne.
<br><br>


# Fonctionalités:
Entrer l'url d'un fichier .ical/.ics pour avoir access à tous les événements de son calendrier sur le bureau de son ordinateur. 

Le calendrier se met automatiquement à jour grace au lien url du calendrier si l'ordinateur à acces à internet.
 Si l'ordinateur n'a pas de connexion internet ou que l'adresse rentré est fautive, un message apparait disant que la mise à jour se fera la prochaine fois que le programme sera ouvert.
<br><br>


# Limitations:
- Le calendrier ne doit pas contenir d'événement avec:
  - des descriptions
  - des evenements partagés
  - une location
  - un événement sur plusieurs jours 
  - un événement qui se repete automatiquement
- vous ne pouvez pas utiliser un calendrier partagé
- Une connexion internet est nécessaire a la première utilisation.
- Une connexion internet est necessaire pour une mise a jour du calendrier.
- Le programme ne peut pas afficher plus d'un calendrier a la fois.
<br><br>










### TRUCS A CHANGER AVANT LA REMISE ###
- aligner les evenements a gauche a la place d'au centre dans les cases du calendrier?
- double check que jai pas écrit des niaiseries ou laissé des commentaires pour moi meme dans le code
- autres idées/points?