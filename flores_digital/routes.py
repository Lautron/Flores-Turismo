from flask import render_template, request, redirect
from flores_digital import app, db
from flores_digital.models import ProductData, Admin
from flores_digital.forms import ProductForm, LoginForm

@app.route('/')
def index():
    #TODO create db to replace the dict.
    towns = {
    'La Región de las Flores': {'img': 'img/escudos/region de las flores.png'}, 
    'Ruiz de Montoya': {'img': 'img/escudos/Ruiz de Montoya.png'}, 
    'Puerto Rico': {'img': 'img/escudos/Puerto Rico.png'}, 
    'Capioví': {'img': 'img/escudos/Capiovi.png'}, 
    'Garuhapé': {'img': 'img/escudos/Garuhapé.png'}, 
    'Montecarlo': {'img': 'img/escudos/Montecarlo.png'}, 
    'Caraguatay': {'img': 'img/escudos/Caraguatay.png'}, 
    'El Alcazar': {'img': 'img/escudos/El Alcazar.png'}}
    return render_template('index.html', towns=towns)

@app.route('/grid')
def grid():
    data = ProductData.query.all()
    data_dict = dictify(data)

    return render_template('grid.html', items=data_dict)

def dictify(sql_obj_list):
    res = []
    contact = {'location', 'phone', 'facebook', 'email', 'instagram', 'website'}
    for obj in sql_obj_list:
        product_dict = {k: v for k, v in vars(obj).items() if not k.startswith('_') and 'id' not in k}
        contact_dict = {k: v for k, v in product_dict.items() if k in contact}
        res.append({**product_dict, 'contact': contact_dict})
    return res

@app.route('/productos')
def productos():
    args = request.args
    data = ProductData.query.filter_by(**args).all()
    data_dict = dictify(data)

    return render_template('grid.html', items=data_dict)

@app.route('/admin/products', methods=('GET', 'POST'))
def product_form():
    form = ProductForm(request.form)
    if form.validate_on_submit():
        #TODO handle image, and save path on db
        print(form.ptype.data)
        product = ProductData(
            name = form.name.data,
            description = form.description.data,
            town = form.town.data,
            ptype = form.ptype.data,
            location = form.location.data,
            phone = form.phone.data,
            facebook = form.facebook.data,
            email = form.email.data,
            instagram = form.instagram.data,
            website = form.website.data
        )
        db.session.add(product)
        db.session.commit()
        print('\n', 'Product uploaded succesfully', '\n')
    return render_template('form.html', form=form)

@app.route('/admin/login', methods=('GET', 'POST'))
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        admin = Admin.query.filter_by(name=form.user.data).first()
        print(admin.name)
        print(admin.password)
        if admin and admin.password == form.password.data:
            print(admin.password == form.password.data)
            return redirect('/admin/products')
    return render_template('form.html', form=form)

