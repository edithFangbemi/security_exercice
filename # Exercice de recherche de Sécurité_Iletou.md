# Exercice de recherche de Sécurité

## Différentes attaques liées aux concepts :Intégrité , authentification , confidentialité et disponibilité 


|Concepts | Attaques      |
|-------- |--------------    |
|Intégrité |Modification|
|Authentification|Fabrication|
|Confidentialité|Interception
|Disponibilité|Interruption


## Les différents types d'attaques 

1. Attaque par déni de service
1. Attaque de l'homme au milieu
1. Attaque fishing

1. Attaque par drive by download
1. Attaque par mot de passe
1. Attaque par injection sql
1. Attaque xcss (cross site scripting)
1. Attaque par écoute illicite
1. Attaque d'anniversaire

1. Attaque par des logiciels malveillants


## Chemins des fichiers de données des SGBD suivants et leurs extensionsracl

* Oracle 
les fichiers de données ont pour extension .dbf (database files)

* Sql Server 
Il est constitué de deux fichiers système qui sont les fichiers de données et les fichiers de journalisation.
les fichiers de données ont pour extension .mdf et le repertoire est:
C:\Program Files\Microsoft SQL Server\MSSQL{nn}.<nom_instance>\MSSQL\Data.

* MySQL
le chemin des fichiers ont pour repertoire C:\Program files\MySQL\data
l'extension des fichiers de données est .frm 

* PostgresSQL
les fichiers de données ont pour extension .psql
le repertoire est: C:\Program files\PostgresSQL\data
## La Norme ITSEC
selon la norme ITSEC, la securité est définie comme l'ensemble des règles et lois qui regissent la façon dont les informations sensibles et les autres ressoures sont gérées, protegées et distribées à l'interieur d'un système d'information.

## Les attaques qui se rapportent aux bases de données
- Injection SQL
- Déni de service
- Usurpation d'identité

# suite de l'exercice de securité
## La norme SQL actuelle
SQL:2011 ou ISO/CEI 9075:2011 (sous le nom "Information technology – Database languages – SQL") est la septième révision de la norme du Langage de requête de Base de données SQL par l'ISO (1987) et l'ANSI (1986). Il remplace la version précédente, SQL:2008, et a été officiellement adoptée le 15 décembre 2011.
## L'option par defaut de revoke est Cascade
## L'option par defaut de grant est " With Grant option"
# les droits en Postgres sont :

|Type d'objet|	Tous les privilèges|	Privilèges par défaut pour PUBLIC|	Commande psql|
|DATABASE|	CTc|	Tc|	\l|
|DOMAIN|	U|	U|	\dD+|
|FUNCTION ou PROCEDURE|	X|	X|	\df+|
|FOREIGN DATA WRAPPER|	U|	aucun|	\dew+|
|FOREIGN SERVER|	U|	aucun|	\des+|
|LANGUAGE|	U|	U|	\dL+|
LARGE OBJECT|	rw|	aucun|	 
|SCHEMA| UC|	aucun|	\dn+|
|SEQUENCE|	rwU|	aucun|	\dp|
|TABLE (et objets similaires)|	arwdDxt|	aucun|	\dp|
|Colonne de table|	arwx|	aucun|	\dp|
|TABLESPACE|	C|	aucun|	\db+|
|TYPE|	U|	U|	\dT+|






 