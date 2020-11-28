from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField, PasswordField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    #Name string
    name = StringField('Nombre', validators=[DataRequired()])
    # Img file
    # img = FileField('Imagen del producto', validators=[FileAllowed(['jpg', 'png', 'jpeg'])]) # validators=[FileRequired()]
    # Description textarea
    # description = TextAreaField('Descripción')
    # Town select
    town = SelectField('Localidad', choices=[
        ('capiovi','Capioví'),
        ('caraguatay', 'Caraguatay'),
        ('el_alcazar', 'El Alcazar'),
        ('garuhape', 'Garuhapé'),
        ('montecarlo', 'Montecarlo'),
        ('puerto_rico', 'Puerto Rico'),
        ('ruiz_de_montoya', 'Ruiz de Montoya'),
    ])
    # type select
    ptype = SelectField('Tipo de producto', choices=[
        ('alojamiento','Alojamiento'),
        ('atraccion','Atracción'),
        ('gastronomia','Gastronomía'),
    ])
    # Location string
    location = StringField('Dirección')
    # phone
    phone = StringField('Telefono')
    # facebook
    facebook = StringField('Facebook')
    # email
    email = StringField('Email')
    # instagram
    instagram = StringField('Instagram')
    # website
    website = StringField('Pagina Web')
    # submit
    submit = SubmitField()

class LoginForm(FlaskForm):
    user = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField()



