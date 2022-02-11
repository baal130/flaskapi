from flask import Flask
import json,os
from flask_restful import Api, Resource , reqparse, abort
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)


db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
db_uri = 'sqlite:///{}'.format(db_path)

app.config.update(dict(
   
    SQLALCHEMY_DATABASE_URI=db_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
))

db = SQLAlchemy(app)



from .products.views import *
#from .productslist.views import *
@app.route("/")
def home_view():
	return "<h1>Hi</h1>"


