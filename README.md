# Livre API 

## Getting Started

### Installation des Dépendances

#### Python 3.9
#### pip 22.0.3 from C:\Users\nn\AppData\Local\Programs\Python\Python39\lib\site-packages\pip (python 3.9)

Suivez les instructions suivantes pour installer l'ancienne version de python sur la plateforme [python docs](https://www.python.org/downloads/windows/#getting-and-installing-the-latest-version-of-python)

#### Dépendances de PIP

Pour installer les dépendances,placez-vous dans le dossier de  `requirements.txt` et exécuter la commande suivante:

```bash ou powershell ou cmd
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

Nous passons donc à l'installation de tous les packages se trouvant dans le fichier `requirements.txt`.

##### clé de Dépendances

- [Flask](http://flask.pocoo.org/)  est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

- [SQLAlchemy](https://www.sqlalchemy.org/) est un toolkit open source SQL et un mapping objet-relationnel écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

## Démarrer le serveur

Pour démarrer le serveur sur Linux ou Mac, executez:

```bash
export FLASK_APP=Routes.py
export FLASK_ENV=development
flask run
```
Pour le démarrer sur Windows, executez:

```bash
set FLASK_APP=Routes.py
set FLASK_ENV=development
flask run
``` 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Type d'erreur
Les erreurs sont renvoyées sous forme d'objet au format Json:
{
    "success":False
    "error": 404
    "message":"Not found"
}

L'API vous renvoie 5 types d'erreur:
. 400: Bad request ou ressource non disponible
. 500: Internal server error
. 401: Unauthorized
. 404: Not found
. 405: Method Not Allowed

## Endpoints
. ## GET/livres

    GENERAL:
        Cet endpoint retourne la liste des livres, la valeur du succès et le total des livres. 
    
        
    EXEMPLE: curl http://localhost:5000/livres
```
{
    "livres": [
        {
            "auteur": "Camara Laye",
            "categorie": {
                "id": 3,
                "libelle de la categorie": "Catégorie 3"
            },
            "date de publication": "Sun, 13 Feb 2022 00:00:00 GMT",
            "editeur": " laya Cotonou",
            "id": 1,
            "isbn": "AZER12",
            "titre": "Mon village"
        },
        {
            "auteur": "SEYDOU Badian",
            "categorie": {
                "id": 9,
                "libelle de la categorie": "Catégorie 8"
            },
            "date de publication": "Sun, 15 Dec 2002 00:00:00 GMT",
            "editeur": " laya Cotonou",
            "id": 4,
            "isbn": "MLrtd",
            "titre": "Maïmouna"
        },
        {
            "auteur": "SEYDOU Badian",
            "categorie": {
                "id": 8,
                "libelle de la categorie": "Catégorie 7"
            },
            "date de publication": "Fri, 15 Feb 2002 00:00:00 GMT",
            "editeur": " laya Cotonou",
            "id": 5,
            "isbn": "OPIrtd",
            "titre": "Le paysage"
        },
        {
            "auteur": "Sembene Ousmane",
            "categorie": {
                "id": 8,
                "libelle de la categorie": "Catégorie 7"
            },
            "date de publication": "Sun, 15 Sep 2002 00:00:00 GMT",
            "editeur": "Néa",
            "id": 6,
            "isbn": "AZSDFrtd",
            "titre": "Le village natal"
        }
    ],
    "nombre de livres": 4,
    "success": true
}
```

.##GET/livres(livre_id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/livres/4
```
 {
    "Livre": {
        "auteur": "SEYDOU Badian",
        "categorie": {
            "id": 9,
            "libelle de la categorie": "Catégorie 8"
        },
        "date de publication": "Sun, 15 Dec 2002 00:00:00 GMT",
        "editeur": " laya Cotonou",
        "id": 4,
        "isbn": "MLrtd",
        "titre": "Maïmouna"
    },
    "id du livre": 4,
    "succes": true
}
```


. ## DELETE/livres (livre_id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE http://localhost:5000/livres/5
```
   {
    "livre": [
        {
            "auteur": "Camara Laye",
            "categorie": {
                "id": 3,
                "libelle de la categorie": "Catégorie 3"
            },
            "date de publication": "Sun, 13 Feb 2022 00:00:00 GMT",
            "editeur": " laya Cotonou",
            "id": 1,
            "isbn": "AZER12",
            "titre": "Mon village"
        },
        {
            "auteur": "SEYDOU Badian",
            "categorie": {
                "id": 9,
                "libelle de la categorie": "Catégorie 8"
            },
            "date de publication": "Sun, 15 Dec 2002 00:00:00 GMT",
            "editeur": " laya Cotonou",
            "id": 4,
            "isbn": "MLrtd",
            "titre": "Maïmouna"
        },
        {
            "auteur": "Sembene Ousmane",
            "categorie": {
                "id": 8,
                "libelle de la categorie": "Catégorie 7"
            },
            "date de publication": "Sun, 15 Sep 2002 00:00:00 GMT",
            "editeur": "Néa",
            "id": 6,
            "isbn": "AZSDFrtd",
            "titre": "Le village natal"
        }
    ],
    "nombre": 3,
    "success": true
}
```

. ##PATCH/livres(livre_id)
  GENERAL:
  Cet endpoint permet de mettre à jour les champs d'un livre.
  Il retourne un livre mis à jour.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH http://localhost:5000/livres/1 -H "Content-Type:application/json" -d '{"titre": "Mon second livre" ,"categorie_id": 9}'
  ```
  {
    "livre": {
        "auteur": "Camara Laye",
        "categorie": {
            "id": 9,
            "libelle de la categorie": "Catégorie 8"
        },
        "date de publication": "Sun, 13 Feb 2022 00:00:00 GMT",
        "editeur": " laya Cotonou",
        "id": 1,
        "isbn": "AZER12",
        "titre": "Mon second livre"
    },
    "nombre": 3,
    "success": true
}
  ```
  


. ## GET/categories

    GENERAL:
        Cet endpoint retourne la liste des categories de livres, la valeur du succès et le total des categories disponibles. 
    
        
    EXEMPLE: curl http://localhost:5000/categories
 ```
    {
    "categorie": [
        {
            "id": 2,
            "libelle de la categorie": "Catégorie 2"
        },
        {
            "id": 3,
            "libelle de la categorie": "Catégorie 3"
        },
        {
            "id": 5,
            "libelle de la categorie": "Catégorie4"
        },
        {
            "id": 1,
            "libelle de la categorie": "nouvelle_categorie"
        },
        {
            "id": 6,
            "libelle de la categorie": "Catégorie 5"
        },
        {
            "id": 7,
            "libelle de la categorie": "Catégorie 6"
        },
        {
            "id": 8,
            "libelle de la categorie": "Catégorie 7"
        },
        {
            "id": 9,
            "libelle de la categorie": "Catégorie 8"
        },
        {
            "id": 10,
            "libelle de la categorie": "Catégorie 9"
        }
    ],
    "nombre": 9,
    "succes": true
}
```

.##GET/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/categories/6
```
   {
    "categorie": {
        "id": 6,
        "libelle de la categorie": "Catégorie 5"
    },
    "nombre": 9,
    "success": true
}
```

. ## DELETE/categories (categories_id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE http://localhost:5000/categories/8
```
  {
    "categorie": [
        {
            "id": 2,
            "libelle de la categorie": "Catégorie 2"
        },
        {
            "id": 3,
            "libelle de la categorie": "Catégorie 3"
        },
        {
            "id": 5,
            "libelle de la categorie": "Catégorie4"
        },
        {
            "id": 1,
            "libelle de la categorie": "nouvelle_categorie"
        },
        {
            "id": 6,
            "libelle de la categorie": "Catégorie 5"
        },
        {
            "id": 7,
            "libelle de la categorie": "Catégorie 6"
        },
        {
            "id": 9,
            "libelle de la categorie": "Catégorie 8"
        },
        {
            "id": 10,
            "libelle de la categorie": "Catégorie 9"
        }
    ],
    "nombre": 8,
    "success": true
}
```

. ##PATCH/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie.
  Il retourne une nouvelle categorie avec la nouvelle valeur.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH 'http://localhost:5000/categories/9' -H "Content-Type:application/json" -d '{"libelle_categorie": " Dessins animés"}'
  ```
  ```
  {
    "categorie": {
        "id": 9,
        "libelle de la categorie": "Dessins animés"
    },
    "id": 9,
    "nombre": 8,
    "success": true
}

.##GET/livres/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de lister les livres appartenant à une categorie donnée.
  Il renvoie la classe de la categorie et les livres l'appartenant.

    EXEMPLE: http://localhost:5000/categories/9/livres
```
{
    "Livre": [
        {
            "auteur": "SEYDOU Badian",
            "categorie": {
                "id": 9,
                "libelle de la categorie": "Dessins animées"
            },
            "date de publication": "Sun, 15 Dec 2002 00:00:00 GMT",
            "editeur": " laya Cotonou",
            "id": 4,
            "isbn": "MLrtd",
            "titre": "Maïmouna"
        },
        {
            "auteur": "Camara Laye",
            "categorie": {
                "id": 9,
                "libelle de la categorie": "Dessins animées"
            },
            "date de publication": "Sun, 13 Feb 2022 00:00:00 GMT",
            "editeur": " laya Cotonou",
            "id": 1,
            "isbn": "AZER12",
            "titre": "Mon second livre"
        }
    ],
    "nombre": 2,
    "success": true
}
```

