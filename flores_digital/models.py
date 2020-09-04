from flores_digital import db

class GridTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(30), unique=True, nullable=False)
    image_file = db.Column(db.String(50), default='img/default.jpg')

    def __repr__(self):
        return f"GridTest('{self.city_name}', '{self.image_file}')"
