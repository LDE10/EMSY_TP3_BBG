# EMSY_TP3_BBG LDE_SPY - Version 1.2

INSTALLATION LINUX
1: Dans une Vm windows utiliser le programme Win32 afin d'importer une image (.img) dans la carte SD fournie.
<img width="540" height="382" alt="image" src="https://github.com/user-attachments/assets/d734e362-2e7e-4993-bf5b-25c33c836d54" />

2: Une fois l'image importée, brancher la carte SD dans le BBG, appuyer sur le bouton "USER" et brancher l'alimentation (Attention cette opération doit être éffectuée en même temps et peux prendre un certain temps au démarrage).
Une fois l'opération bien effectuée le processus de flash est indiqué par un chenillard sur les leds, puis s'allument toute pour enfin s'éteindre.

3: Quand toutes les leds sont éteint, on peut débrancher l'alimentation, éjecter la carte SD et redémarrer le BBG.
Le BBG démarre son OS Linux stocké dans sa flash interne.

REGLAGE IP STATIQUE  
4: Brancher le BBG sur le réseau bleu.
 Dans la même Vm windows télécharger l'application "Advanced IP Scanner", cette application va servir à lire l'adresse IP du BBG.
 <img width="933" height="546" alt="image" src="https://github.com/user-attachments/assets/e9088828-df82-4b57-9b5b-b1b5498521e2" />

   Ouvrir Putty et inserer l'adress ip 10.228.134.52

5: Il faut se connecter au BBG avec le nom USE(Debian) et le mot de passe (temppwd)
<img width="645" height="425" alt="image" src="https://github.com/user-attachments/assets/0c21642a-ba1b-47dc-81c6-41af39b69213" />

6: Il faut configurer une adresse IP statique

<img width="643" height="422" alt="image" src="https://github.com/user-attachments/assets/d556ce3a-1876-4a7f-a009-fe82c7d6cd83" />

7: Pour sauvegarder le fichier li faut redémarer le BBG avec la commande "Sudo reboot"

8: Ouvrir Putty et inserer l'adress ip 10.228.134.255

<img width="647" height="543" alt="image" src="https://github.com/user-attachments/assets/9cc96b6e-b6cd-445d-8cbd-12cd5e1016a3" />

9: Crer un répertoire avec nos initiales

<img width="555" height="175" alt="image" src="https://github.com/user-attachments/assets/10564d78-f23d-45c7-8cd0-2ea2ff1aff8c" />

10: Editer un fichier texte avec la commande "vi" et le déplacer dans le bon répertoire avec la comande "mv"
<img width="768" height="85" alt="image" src="https://github.com/user-attachments/assets/512f441e-cdcd-487e-9da8-63788ed193d4" />

11: dans le navigateur accédez à http://checkip.dyndns.org

<img width="547" height="189" alt="image" src="https://github.com/user-attachments/assets/4515f0db-f0a5-4247-ab34-850eba5e54fa" />

12: On utilise la commande wget -qO- http://checkip.dyndns.org sur le BBG
<img width="842" height="59" alt="image" src="https://github.com/user-attachments/assets/13d916f0-c2fe-4abc-852d-6774839a6af4" />

Réponse aux questions

Q1. Comment pouvez-vous déterminer cette adresse IP ? 

Réponse : Grâce à un sniffer, nous avons utilisé application "Advanced IP Scanner"

Q2. Quel est le protocole de communication permettant de vous connecter à distance au BBG ?  

Réponse : Protocole SSH (Secure Shell), c'est une méthode sécurisée permettant d'accéder à distance à une machine, d'exécuter des commandes et de transférer des fichiers.

Q3. Dans le modèle OSI, dans quelle(s) couche(s) se trouve ce protocole ?  

Réponse : Le SSH se trouve dans la couche 7 mais s'exécute dans la couche 4 en parallèle du TCP.

Q4. Sur quel protocole de couche 4 s’appuie ce protocole ? Quel est le port utilisé côté serveur ?  

Réponse : Le protocole SSH s'exécute en parallèle du protocole TCP. Le port par défaut utilisé côté serveur est le port 22.

Q5. Si vous n’arriviez pas à vous connecter au BBG, quelle(s) commande(s), testeriez-vous depuis une autre machine connectée au même réseau ? 

Réponse : Aller dans les commande windows, puis écrire la commande "ping (adresse IP)" . (envoie une donnée et mesure le temp quel met pour revenir)
<img width="1069" height="580" alt="image" src="https://github.com/user-attachments/assets/125428e9-6592-47e4-b287-9797fb05c58a" />

Q6. A la suite de votre connexion, dans quel répertoire vous trouvez-vous ?  Quelle(s) commande(s) utilisez-vous pour le déterminer ?

Réponse : A l'ouverture on se trouve dans le répertoire personelle "/home/debian". 
          Pour le savoir utiliser la commande "pwd".

Q7. Quelle(s) commande(s) utilisez-vous pour créer ce répertoire ? Qui a les droits d’écriture dessus ?

Réponse : La commande utilisée pour créer un répertoire est "mkdir".
          Il n'y a que l'user (administrateur) ayant créer le répertoire, qui à les droits d'écriture.

<img width="813" height="543" alt="image" src="https://github.com/user-attachments/assets/ab677767-5b30-4164-9032-efbc88a6c1ac" />

Q8. Comment pouvez-vous contrôler ce que vous avez écrit sans réouvrir le fichier en écriture ?  

Réponse : Dans le répertoire du fichier, La commande "cat <nom du fichier>" permet d'afficher tout le contenu de celui-ci.
<img width="545" height="36" alt="image" src="https://github.com/user-attachments/assets/2d17a505-2ac6-4a64-a12a-f337ca178a1f" />

Q9. Comment contrôlez-vous qu’un logiciel soit bien installé ? Quelle(s) est/sont les commandes pour installer un logiciel (vous pouvez tester par exemple avec sl ou cmatrix) ?

<img width="575" height="296" alt="image" src="https://github.com/user-attachments/assets/33f3482e-1cdf-4a41-a49c-c2853a3f68c2" />

Réponse : La commande "apt list" permet lister tous les paquets disponibles et installés, sela permet de vérifier si le logiciel y figure. 
          La commande "sudo apt install <nom logiciel>" permet l'instalation d'un logiciel.


Q10. Sur le BBG, quelle(s) est/sont la/les commande(s) pour connaitre la configuration du réseau Ethernet ? 
a. Quelle est l’adresse IP du BBG ?
b. Quelle est le masque de sous réseau ?
c. Quelle est l’adresse réseau ?
d. Quelle est la passerelle par défaut ?
e. Quelle est l’adresse MAC du BBG ?

Réponse :
La commande "ip addr show eth0" est utilisé pour affiché en détail la configuration résaux Ethernet
la commande ip a est utilisé pour connaitre les différente interface résaux
la commande ifconfi est utilisée pour affiché les inteface résaux, mais il faut au préalable instaler le paquet "net-tools"

a) 10.228.134.225

<img width="733" height="236" alt="image" src="https://github.com/user-attachments/assets/f03f92b2-2331-4c08-8163-f05ea6e00410" />

b) 10.228.134.225/24 le masque sous réseau est sous la notation"CIDR( Classless Inter Domain Routing).Le /24 indique 24 bit à 1, soit 255.255.255.0

c) 127.0.0.1

<img width="837" height="180" alt="image" src="https://github.com/user-attachments/assets/db74e149-186d-49c8-9941-f32f48c6aa9a" />

d) 10.228.134.1

<img width="637" height="118" alt="image" src="https://github.com/user-attachments/assets/26e26660-be43-4ff4-8159-967eaab23d09" />

e) b4:10:7b:74:b6:36
<img width="881" height="344" alt="image" src="https://github.com/user-attachments/assets/4e0d068e-1758-40d2-a47d-ead8fa78f306" />

Q11. Qu’est-ce qui s’affiche en retour ?  Commentez. 

Réponse : Current IP Addres: 193.5.240.10
          C'est l'ip public qui sort de l'établissement
<img width="537" height="187" alt="image" src="https://github.com/user-attachments/assets/b5005dad-8194-4e26-80af-7cd3c45d66dd" />

Q12. Expliquez ce que fait cette commande. Qu’est-ce qui s’affiche en retour ?  Quel est format de la réponse ?  Faites le parallèle avec la réponse à la Q11. 

Réponse : <html><head><title>Current IP Check</title></head><body>Current IP Address: 193.5.240.10</body></html>
          Le format de la réponse est donné sous format brut sur le terminal.
          La différence entre la question 11 et 12 est du au format utilisé pour afficher l'ip.
          A la question 11 le navigateur va comprendre le code html et va l'interpréter pour le rendre graphiquement visible.
          A la question 12 linux ne comprend pas le format html et affiche seulement les données brut.


Q13. Comparez l’adresse IP locale de votre BBG à celles trouvées aux Q11 et Q12.  Commentez. 

Réponse : L'adresse du BBG est privé, elle est statyque.
          L'adresse au question 11 et 12 est public, elle est dynamique.

13: Branchement du capteur sur le BBG
Selon le datasheet du BBG il est conseil de brancher le capteur sur I2C Grove interface(Connecté au peripérique I2C2)
<img width="1043" height="563" alt="Capture d’écran 2026-03-19 154251" src="https://github.com/user-attachments/assets/e7aa5ca7-2d4f-4552-9f3d-284034141ff0" />

Q14. Le driver SHT4x s'occupe de faire le lien entre L'OS et le capteur.
Nous avons procédez selon ce shéma bloc:

<img width="1920" height="1080" alt="dw" src="https://github.com/user-attachments/assets/152d673e-23be-4aeb-9786-454dd82e3f99" />

Le scripte fourni dans le support de cours, est lu par l'interpréteur(python3) ensuit selui ci va tranmettre le code en format linux sur le driver qui va piloter le capteur.
1)Script fournis: tp_emsy.py
2)Interpréteur python3: instalation avec la commande "sudo apt update && sudo install python3"
3)Instalation du driver générale via la commande "sudo apt-get install sht4x"
4)Instalation du driver plus spécifique pour une comunication "API" en l'OS et le capteur: sensirion-i2c-driver sensirion-i2c-sht via la comande "pip3 install sensirion-i2c-driver sensirion-i2c-sht"

14. Conception du script Python
Le scrypt est disponible dans le dossier TP_EMSY.

15. Documentation du code

Le code du main est utilisé dans le tp_emsy pour n'avoir qu'un main.
Il y a une codition qui est demandée "Le but est d’envoyer un e-mail d’alarme lorsqu’une valeur limite est dépassée (28°C)".
Pour cela une condition "if" est utilisée si la température est au dessu de 28° alors l'e-mail sera envoyé.
Le "subject" est l'object de l'e-mail dans notre cas "Aletre température".
Puis l'écriture du message est fait dans un tableau "message" qui contientle message d'alerte avec toutes les mesures données.
Enfin envoyer notre tableau "message" et le "subject dans le send_email sans oublier l'adresse mail de reception.
ATTENTION en même temps de donner les valeurs dans le send_email faire l'appel de fonction d'envoie.

![image 26](/Image/Image 26.png "image 26")


Image 26
Image 27

-Capture température
Une bonne partie du code à déjà été éffectuée, le travail consiste à faire le calcul et l'écrire du résultat dans un fichier .csv

1) Opération mathématique
l'opération à été donnée dans la consigne, il suffit d'ajouter les opérations mathématiques
Image 28

2)Main
En premier afficher un texte pour prouver que le main est éxecuté.
Appel de la fonction des mesures pour prendre les valeurs de la température et l'humidité.
Appel de la fonction mathion mathématique.
Arrondissement des valeurs.
Affichage des valeurs en printf.
Réception de la date et de l'heure dans un tableau avec la température l'humidité et le dp arrondi.
ATTENTION un ordre à été demandé : <date>,<heure>,<température>,<humidité>,<point de rosée>. 
écriture du tableau dans le fichier .csv
Image 29
Image 30
Image 31


Eratum:
Q10 c) Valleur adresse réseau = masquage de l'adresse ip avec le masque de sous réseau, soit 10.228.134.255 Masqué par 255.255.255.0 = 10.228.134.0
    L'adress 127.0.0.1 représente le localhost (un serveur éxecuté sur notre propre ordinateur) c'ette adress IP est généralement réservé à un loopback.
    Pour résumé, c'est l'adresse d'une interface virtuel. Cette interface est utilisé pour tester des programmes et des applications web, on peut aussi l'utiliser pour bloquer des sites web dangereux.


Partie B Automatisation

-Enregistrement CSV
Pour enregistrer nos valeur dans le fichier TempLog.csv, il convient d'abord de créer celui-ci dans le répertoire /home/debian avec la commande "touch TempLog.csv"
On peut aussi le faire avec la commande "nano TempLog.csv". Nous avons utiliser la commande touch par curiosité.

Verification après création:

<img width="322" height="145" alt="Verification fichier csv" src="https://github.com/user-attachments/assets/5feba1eb-2f24-40c3-bb96-3bf32b1bec43" />

Verification du script après execution de celui-ci:

------mettre image--------------

-Envoi d'E-MAIL
Pour envoyer le mail, il suffit de moddifier le fichier "send_email.py" qui nous est fournit.
Il est conseiller de le modifier et de le tester avec visual studio avant de le téléverser dans le BBG.
1) Ouverture du fichier dans visualstudio en python.
2) Modification des éléments entre parentèse.

<img width="444" height="95" alt="image" src="https://github.com/user-attachments/assets/0f3f9fc5-c6a4-4ae2-96fe-af3ad05a8e0c" />

2.1) Explication sur ce qui doit être modifié.
- server = smtplib.SMTP("mail.etml-es.ch") --- Veuillez indiquer le nom de serveur ainsi que son port sortant (587).
- server.login("user","password") --- Veuillez indiquer l'adresse mail de réception ainsi qu'un code appareil créer dans cette boite mail.
- sender = "XXX@etml-es.ch" --- Veillez indiquer l'adresse d'envoie.

2.2) Exemple de modification.

<img width="673" height="115" alt="image" src="https://github.com/user-attachments/assets/1c49fc0e-5c79-4cc4-a223-85682b3cdb97" />

2.3) Resultats devant être obtenu après modification sur la boîte mail.

<img width="626" height="308" alt="image" src="https://github.com/user-attachments/assets/2100d10e-12ef-43d7-8798-015807926238" />

-Execution Automatique
Pour lancer notre script à intérval régulier, on utilise la tâche/commande "crontab" (crono Tableau)
Explication sur l'utilisation de la commande "crontab":
- "crontab -l permet d'afficher la liste des tâches dégà existantes.
image 32
- "crontab -e permet de pouvoir étider une tâche selon les editeur de texte disponible.
il convient t'abord de sélectionner un éditeur de texte.
image 35

Dans l'éditeur de texte il faut donner er 1er la notion de temps 
image 33

En second le fichier source de l'executeur(python3) et le fichier source du scrypt à executer
image 34

