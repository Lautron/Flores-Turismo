from flores_digital import db
import json

class ProductData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), unique=True, nullable=False)
    img = db.Column(db.String(100), default='img/default.jpg')
    # description = db.Column(db.Text, nullable=False)
    town = db.Column(db.String(30))
    ptype = db.Column(db.String(30))

    location = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100))
    facebook = db.Column(db.String(100))
    email = db.Column(db.String(100))
    instagram = db.Column(db.String(100))
    website = db.Column(db.String(100))

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(15), unique=True, nullable=False)

if __name__ == "__main__":
    pass

    


