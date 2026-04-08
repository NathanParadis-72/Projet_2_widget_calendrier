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
- Une fenetre de style widget sur votre écran d'ordinateur qui affiche les informations du fichier .ical/.ics sous la forme d'événements avec toutes les informations pertinentes telles que l'heure de début, l'heure de fin et le nom de l'événement.
- Un fichier de sauvegarde du calendrier en format .ics
- un fichier de sauvegarde de l'url du calendrier en format .txt
- un fichier de sauvegarde de la liste formattée et triée utilisée par le widget pour
<br><br>


# Controle:
Lorsque le programme est démarré, il demandera a l'utilisateur d'entrer un url particulier dans le terminal (les instructions sont affichées, il s'agit de "l'url secret" du calendrier google de l'utilisateur), cet url est très important car c'est lui qui s'occupe d'aller chercher les informations dans le calendrier de l'utilisateur ainsi que de le mettre a jour a chaque lancement du programme. Si l'url existe deja dans un fichier de sauvegarde (créé automatiquement a la première utilisation), le programme ne demande pas d'url et met simplement le calendrier a jour s'il a accès a l'internet.

Dans le cas ou l'utilisateur voudrait changer le calendrier affiché, il doit simplement supprimer le fichier "sauvegarde_url.txt", le programme demandera alors un nouvel url au prochain lancement.

Après la sauvegarde de l'url, le programme sauvegarde automatiquement la version la plus récente du calendrier dans un fichier .ics, afin de pouvoir continuer a utiliser le calendrier même dans le cas ou l'utilisateur n'a pas accès a l'internet. Aucune action n'est requise de la part de l'utilisateur pour cette sauvegarde.
<br><br>


# Fonctionalités:
Entrer l'url d'un fichier .ical/.ics pour avoir accès a tous les événements de son calendrier sur le bureau de son ordinateur. 

Le calendrier se met automatiquement a jour grace au lien url du calendrier si l'ordinateur a accès a internet Si l'ordinateur n'a pas de connexion internet, un message apparait disant que la mise a jour se fera la prochaine fois que le programme sera ouvert et qu'il pourra acceder a l'internet.
<br><br>


# Limitations:
- Pas tous les fichiers .ical/.ics ont toutes les informations de votre calendrier, il semble y avoir un probleme avec les calendriers qui existent depuis longtemps et ou qui ont été créés par un autre utilisateur avant de vous être transférés. 
- Le programme ne peut pas afficher plus d'un fichier calendrier a la fois.
- Si on veut changer de calendrier a afficher il faut aller manuellement changer le url dans le fichier "sauvegarde_url". 
- Ne pas avoir accès a internet pendant le premier lancement du programme (pour creer le fichier de backup du calendrier) ne fonctionne pas, car le programme a besoin d'aller chercher un fichier .ical/.ics afin de le sauvegarder pour les prochaines utilisations.
- Si par une erreur quelconque le fichier sauvegarde_url est vide (ou contient un mauvais url), le programme ne fait rien. Pour le réparer, seulement supprimer le fichier sauvegarde_url, ou écrire un url valide dedans.
<br><br>










### TRUCS A CHANGER AVANT LA REMISE ###
- aligner les evenements a gauche a la place d'au centre dans les cases du calendrier?
- double check que jai pas écrit des niaiseries ou laissé des commentaires pour moi même dans le code
- autres idées/points?