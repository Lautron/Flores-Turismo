from flask import render_template
from flores_digital import app
from flores_digital.models import GridTest

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
    items = GridTest.query.all()
    icons = [
            'marker', 'phone',
            'facebook2', 'mail', 
            'instagram','globe',
            ]
    icons_fp = ['icons/' + icon + '.svg' for icon in icons]
    return render_template('grid.html', items=items, icons=icons_fp)