from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField, PasswordField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    #Name string
    name = StringField('Nombre', validators=[DataRequired()])
    # Img file
    img = FileField() # validators=[FileRequired()]
    # Description textarea
    description = TextAreaField('Descripción')
    # Town select
    town = SelectField('Localidad', choices=[
        ('capiovi','Capioví'),
        ('caraguatay', 'Caraguatay'),
        ('el alcazar', 'El Alcazar'),
        ('garuhape', 'Garuhapé'),
        ('montecarlo', 'Montecarlo'),
        ('puerto rico', 'Puerto Rico'),
        ('ruiz de montoya', 'Ruiz de Montoya'),
    ])
    # type select
    ptype = SelectField('Tipo de producto', choices=[
        ('actividad','Actividad'),
        ('alojamiento','Alojamiento'),
        ('atraccion','Atracción'),
        ('gastronomia','Gastronomía'),
    ])
    # Location string
    location = StringField('Ubicación')
    # phone
    phone = StringField('Telefono')
    # facebook
    facebook = StringField('Facebook')
    # email
    email = StringField('eMail')
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



