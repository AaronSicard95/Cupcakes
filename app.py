"""Flask app for Cupcakes"""
from flask import Flask, render_template, jsonify, request
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcake"
app.config['SECRET_KEY'] = "LMAONO"

connect_db(app)
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/api/cupcakes', methods=['GET'])
def getCakes():
    cakes = Cupcake.query.all()
    toGive = [serializeCake(cake) for cake in cakes]

    return jsonify(cakes=toGive)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
def getCake(cupcake_id):
    cake = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(serializeCake(cake))

@app.route('/api/cupcakes', methods=['POST'])
def addCake():
    new_cake = Cupcake(
        flavor = request.form['flavor'],
        size = request.form['size'],
        rating = request.form['rating'],
        image = request.form['image'])
    db.session.add(new_cake)
    db.session.commit()
    return jsonify(serializeCake(new_cake))

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def updateCake(cupcake_id):
    cake = Cupcake.query.get_or_404(cupcake_id)
    cake.flavor = request.form['flavor'],
    cake.size = request.form['size'],
    cake.rating = request.form['rating'],
    cake.image = request.form['image']
    db.session.add(cake)
    db.session.commit()

    return jsonify(serializeCake(cake))

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def deleteCake(cupcake_id):
    cake = Cupcake.query.get_or_404(cupcake_id)
    db.session.remove(cake)
    db.session.commit()

    return jsonify({"message": "Deleted"})


def serializeCake(cake):
    return{"flavor": cake.flavor,"rating":cake.rating,"size":cake.size,"image":cake.image}