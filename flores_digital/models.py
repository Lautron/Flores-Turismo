from flores_digital import db
import json

class ProductData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    img = db.Column(db.String(30), default='img/default.jpg')
    description = db.Column(db.Text, nullable=False)
    town = db.Column(db.String(30))
    product_type = db.Column(db.String(30))
    contact = db.relationship('Contact', backref='product', lazy=True)
    def __init__(self, data_dict, contact):
        self.name = data_dict.get('name', None)
        self.img = data_dict.get('img', None) 
        self.description = data_dict.get('description', None) 
        self.town = data_dict.get('town', None) 
        self.product_type = data_dict.get('product_type', None)
        self.contact = [contact]


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product_data.id'), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50))
    facebook = db.Column(db.String(50))
    email = db.Column(db.String(50))
    instagram = db.Column(db.String(50))
    website = db.Column(db.String(50))

    def __init__(self, **kwargs):
        self.location = data_dict.get('location', None)
        self.phone = data_dict.get('phone', None)
        self.facebook = data_dict.get('facebook', None)
        self.email = data_dict.get('email', None)
        self.instagram = data_dict.get('instagram', None)
        self.website = data_dict.get('website', None)


if __name__ == "__main__":

    test = ProductData({'name': 'Ruiz de Montoya Spa', 'description': 'This is a test', 'town': 'Ruiz de Montoya', 'product_type': 'atraction'},
            Contact({'location': 'Ruiz de Montoya', 'phone': '1244556', 'facebook': 'Ruiz de Montoya', 'email': 'ruizdemontoya@gob.ar', 
            'instagram': '@ruizdemontoyaturismo', 'website': 'ruizdemontoya.com.ar'}))
    test2 = ProductData({'name': 'Ruiz de Montoya Salto', 'description': 'This is a test', 'town': 'Ruiz de Montoya', 'product_type': 'atraction'},
            Contact({'location': 'Ruiz de Montoya', 'phone': '1244556', 'facebook': 'Ruiz de Montoya', 'email': 'ruizdemontoya@gob.ar', 
            'instagram': '@ruizdemontoyaturismo', 'website': 'ruizdemontoya.com.ar'}))

    


