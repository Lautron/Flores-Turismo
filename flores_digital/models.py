from flores_digital import db
import json

class ProductData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    img = db.Column(db.String(30), default='img/default.jpg')
    description = db.Column(db.Text, nullable=False)
    town = db.Column(db.String(30))
    product_type = db.Column(db.String(30))

    location = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50))
    facebook = db.Column(db.String(50))
    email = db.Column(db.String(50))
    instagram = db.Column(db.String(50))
    website = db.Column(db.String(50))

if __name__ == "__main__":

    test = ProductData({'name': 'Ruiz de Montoya Spa', 'description': 'This is a test', 'town': 'Ruiz de Montoya', 'product_type': 'atraction'},
            Contact({'location': 'Ruiz de Montoya', 'phone': '1244556', 'facebook': 'Ruiz de Montoya', 'email': 'ruizdemontoya@gob.ar', 
            'instagram': '@ruizdemontoyaturismo', 'website': 'ruizdemontoya.com.ar'}))
    test2 = ProductData({'name': 'Ruiz de Montoya Salto', 'description': 'This is a test', 'town': 'Ruiz de Montoya', 'product_type': 'atraction'},
            Contact({'location': 'Ruiz de Montoya', 'phone': '1244556', 'facebook': 'Ruiz de Montoya', 'email': 'ruizdemontoya@gob.ar', 
            'instagram': '@ruizdemontoyaturismo', 'website': 'ruizdemontoya.com.ar'}))

    


