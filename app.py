from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file___))

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Init db
db = SQLAlchemy(app)
#Init ma

ma = Marshmallow(app)

#Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Column(db.Float))
    qty = db.Column(db.Integer)

    def __init__(self):


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello World'})

#Run server

if __name__ == '__main__':
    app.run(debug=True)