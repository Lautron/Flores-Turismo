from flask import render_template
from flores_digital import app
from flores_digital.models import ProductData

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

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/grid')
def grid():
    data = ProductData.query.all()
    data_dict = dictify(data)

    return render_template('grid.html', items=data_dict)

def dictify(sql_obj_list):
    res = []
    for obj in sql_obj_list:
        product_dict = {k: v for k, v in vars(obj).items() if not k.startswith('_') and 'id' not in k}
        contact_dict = {k: v for k, v in vars(obj.contact[0]).items() if not k.startswith('_') and 'id' not in k}
        res.append({**product_dict, 'contact': contact_dict})
    return res

@app.route('/productos/<name>')
def productos(name):
    data = ProductData.query.filter_by(product_type=name).all()
    data_dict = dictify(data)

    return render_template('grid.html', items=data_dict)

