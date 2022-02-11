from app import db

class ProductDB(db.Model):
    id          = db.Column(db.Integer, primary_key=True,unique=True,) # primary_key
    name        = db.Column(db.String(120), nullable=True)
    price       = db.Column(db.String(120),  nullable=False)
