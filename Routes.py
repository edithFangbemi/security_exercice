from flask import Flask, abort, jsonify,request
from flask_cors import CORS, cross_origin
import os
from flask_sqlalchemy import SQLAlchemy  # importer SQLAlchemy
#import urllib.parse
from urllib.parse import quote_plus
from dotenv import load_dotenv  # permet d'importer les variables d'environnement
load_dotenv()
dialect = quote_plus(os.getenv('dialect'))
user = quote_plus(os.getenv('user'))
mot_de_passe = quote_plus(os.getenv('pswrd'))
host = quote_plus(os.getenv('host'))
port = quote_plus(os.getenv('port'))
database = quote_plus(os.getenv('database'))
app = Flask(__name__)
CORS(app, ressources={})
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://uauvkemigerxxc:08f65899df3f6dc71b3a5a51ee0bc0c27acbce2c6f5d5cb1fbfd8d6b88dcb7fe@ec2-72-44-41-8.compute-1.amazonaws.com:5432/d7gg5kbq0bk9id"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Categorie (db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    libelle_categorie = db.Column(db.String(50), nullable=False)  # FastUnmarshaller#
    les_livres = db.relationship('Livre', backref='Categorie', lazy=True)

    def __init__(self, libelle_categorie):
        self.libelle_categorie = libelle_categorie

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format2(self):
        return{
            'id': self.id,
            'libelle de la categorie': self.libelle_categorie
        }


class Livre(db.Model):
    __tablename__ = 'livres'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(10), nullable=False, unique=True)
    titre = db.Column(db.String(50), nullable=False)
    date_publication = db.Column(db.Date, nullable=False)
    auteur = db.Column(db.String(50), nullable=False)
    editeur = db.Column(db.String(50), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __init__(self, isbn, titre, date_publication, auteur, editeur,categorie_id):
        self.isbn = isbn
        self.titre = titre
        self.date_publication = date_publication
        self.auteur = auteur
        self.editeur = editeur
        self.categorie_id = categorie_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        cat = Categorie.query.get(self.categorie_id)
        return {
            'id' : self.id,
            'isbn': self.isbn,
            'titre': self.titre,
            'date de publication': self.date_publication,
            'auteur': self.auteur,
            'editeur': self.editeur,
            'categorie' : cat.format2()
        }

db.create_all()

            ######################
            # Liste des Personnes #
            ######################

@app.route('/livres')
def get_all_books():
    mon_livre = Livre.query.all()
    mon_livre = [p.format() for p in mon_livre]
    return jsonify(
        {
            'success':True,
            'livres': mon_livre,
            'nombre de livres':len(Livre.query.all())
        }
    )

        ##### chercher un livre par son identifiant####

@app.route('/livres/<int:id_livre>')
def find_book(id_livre):
    mon_livre = Livre.query.get(id_livre)
    if mon_livre is None:
        abort(404)
    else:
        return jsonify({
            'succes':True,
            'id du livre':id_livre,
            'Livre': mon_livre.format()
        })
        #### Donner la liste des livres d'une categorie###
@app.route('/categories/<int:categorie_id>/livres')
def liste_art(categorie_id):
    if Categorie.query.get(categorie_id) is None:
        return jsonify({
            "Erreur" : "La catégorie n'existe pas"
        })
    livre = Livre.query.filter(Livre.categorie_id == categorie_id)
    cat = Categorie.query.get(categorie_id)
    if livre is None:
        abort(404)
    else:
        livres = [p.format() for p in livre]
        nombre = livre = Livre.query.filter(Livre.categorie_id == categorie_id).count()
        return jsonify({
            
            'success':True,
            'Livre':livres,
            'nombre':nombre
            })
        ### Chercher une categorie par son id####
@app.route('/categories/<int:id>')
def one_categorie(id):
    categorie = Categorie.query.get(id)
    categorie = categorie.format2()
    return jsonify({
        'success':True,
        'categorie':categorie,
        'nombre':len(Categorie.query.all())
    })

        #### liste de toutes les categories####

@app.route('/categories')
def all_categories():
    categories = Categorie.query.all()
    category = [c.format2() for c in categories]
    return jsonify({
        'succes':True,
        'categorie':category,
        'nombre':len(categories)
    })

    ##Ajouter une catégorie###

@app.route('/categories',methods = ['POST'])
def add_categorie():
    body = request.get_json()
    new_libelle = body.get('libelle')
    cat = Categorie(libelle_categorie = new_libelle)
    cat.insert()
    categories = Categorie.query.all()
    categories = [ ca.format2() for ca in categories]

    return jsonify({
        'succes':True,
        'categorie': categories,
        'nombre':len(Categorie.query.all())
    })

    #### Ajouter un livre #####
@app.route('/livres', methods =['POST'] )
def one_book():
    body = request.get_json()
    new_isbn = body.get('isbn')
    new_titre = body.get('titre')
    new_auteur = body.get('auteur')
    new_editeur = body.get('editeur')
    new_date_publication = body.get('date_publication')
    new_categorie_id = body.get('categorie_id')

    livre = Livre(isbn = new_isbn, auteur = new_auteur, titre = new_titre, editeur = new_editeur, date_publication= new_date_publication,categorie_id = new_categorie_id )
    livre.insert()
    livre = Livre.query.all()
    livres = [l.format() for l in livre]
    return jsonify({
        'success': True,
        'livre':livres,
        'nombre':len(livre)

    })

        ### supprimer un livre ####
@app.route('/livres/<int:id>', methods = ['DELETE'])
def supprimer_livre(id):
    livre = Livre.query.get(id)
    if livre is None:
       abort(404)
    livre.delete()
    livres = Livre.query.all()
    livres_format = [ l.format() for l in livres]
    nombre = len(livres)
    return jsonify({
        'success': True,
        'livre':livres_format,
        'nombre':nombre
    })

        ### supprimer une categorie ####

@app.route('/categories/<int:id>', methods = ['DELETE'])
def supprimer_categorie(id):
    categorie = Categorie.query.get(id)
    livres = Livre.query.filter_by(categorie_id = id)
    livres.delete()
    categorie.delete()
    categorie_restant = Categorie.query.all()
    categorie_format = [l.format2() for l in categorie_restant]
    nombre = len(categorie_restant)
    return jsonify({
        'success':True,
        'categorie':categorie_format,
        'nombre':nombre

    })
    ### Modifier un livre ###

@app.route('/livres/<int:id_livre>',methods = ['PATCH'])
def modifier_livre(id_livre):
    body = request.get_json()
    try:
        livre = Livre.query.get(id_livre)
        if livre is None:
            abort(404)
        else:
            if 'isbn' in body:
                livre.isbn = body.get('isbn')
            if 'titre' in body:
                livre.titre = body.get('titre')
            if 'date_publication' in body:
                livre.date_publication = body.get('date_publication')
            if 'auteur' in body:
                livre.auteur = body.get('auteur')
            if 'editeur' in body:
                livre.editeur = body.get('editeur')
            if 'categorie_id' in body:
                livre.categorie_id = body.get('categorie_id')        
        livre.update()
        return jsonify({
            'success': True,
            'livre':livre.format(),
            'nombre':len(Livre.query.all())
        })
    except:
        abort(400)


        #### Modifier libelle d'une categorie###

@app.route('/categories/<int:id>', methods = ['PATCH'])
def modifier_categorie(id):
    body = request.get_json()
    try:
        categorie = Categorie.query.get(id)
        if categorie is None:
            abort(404)
        else:
            if "libelle_categorie" in body:
                categorie.libelle_categorie = body.get('libelle_categorie')
                categorie.update()
            else:
                return jsonify({
                    'Erreur' : "Veuillez vérifier le libelle"
                })
        return jsonify({
            'success':True,
            'id':id,
            'categorie': categorie.format2(),
            'nombre':len(Categorie.query.all())
        })
    except:
        abort(400)

@app.errorhandler(400)
def not_found(error):
    return jsonify({
        "success" : False,
        "error" : 400,
        "message" : "Bad request"
    }),400
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success" : False,
        "error" : 404,
        "message" : "Not found"
    }),404

@app.errorhandler(500)
def not_found(error):
    return jsonify({
        "success" : False,
        "error" : 500,
        "message" : "Internal server error"
    }),500
@app.errorhandler(405)
def not_found(error):
    return jsonify({
        "success" : False,
        "error" : 405,
        "message" : "method not allowed"
    }),405
@app.errorhandler(422)
def not_found(error):
    return jsonify({
        "success" : False,
        "error" : 422,
        "message" : "Unprocessable"
    }),422

