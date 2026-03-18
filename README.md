# EMSY_TP3_BBG

INSTALLATION LINUX
1: Dans une Vm windows utiliser le programme Win32 afin d'importer une image (.img) dans la carte SD fournie.

2: Une fois l'image importée, brancher la carte SD dans le BBG, appuyer sur le bouton "USER" et brancher l'alimentation (Attention cette opération doit être éffectuée en même temps et peux prendre un certain temps au démarrage).
Une fois l'opération bien effectuée le processus de flash est indiqué par un chenillard sur les leds, puis s'allument toute pour enfin s'éteindre.

3: Quand toutes les leds sont éteint, on peut débrancher l'alimentation, éjecter la carte SD et redémarrer le BBG.
Le BBG démarre son OS Linux stocké dans sa flash interne.

REGLAGE IP STATIQUE  
1: Brancher le BBG sur le réseau bleu.

2: Dans la même Vm windows télécharger l'application "Advanced IP Scanner", cette application va servir à pour lire l'adresse IP du BBG.
Une fois l'installasion éffectué copier l'application dans l'ordinateur.

3: 


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
