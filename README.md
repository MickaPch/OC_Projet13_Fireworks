# MyJOB app


Parcours développeur d'applications Python - Projet final  
> Application de suivi de recherche d'emploi


## Pré-requis


- Python 3
- Base de données MySQL  
    Name : *my_job*  
    User : *my_job_user*  
    **No password**  


## Installation

- Installation des packages  
`python3 -m pip install -r .\requirement.txt`  

- Création de la base de données  
`python3 .\manage.py migrate`

- Remplissage de la base de données avec les fixtures de donnée aléatoires crées  
`python3 .\manage.py loaddata users.json business.json skills.json contacts.json appliances.json events.json`


## Utilisateur enregistré

- Superuser (accès à l'interface administrateur) :  
Name : *User1*  
Password : *pwd$User1*

- Utilisateur normal :
Name : *User2*  
Password : *pwd$User2*
