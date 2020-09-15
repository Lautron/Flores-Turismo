from flask import render_template
from flores_digital import app
from flores_digital.models import GridTest

@app.route('/')
def index():
    towns = {'Ruiz de Montoya': {'color': 'bg-gray', 'img': 'img/escudos/Ruiz de Montoya.jpg'}, 
    'Puerto Rico': {'color': '', 'img': 'img/escudos/Puerto Rico.jpg'}, 
    'Capiovi': {'color': 'bg-gray', 'img': 'img/escudos/Capiovi.jpg'}, 
    'Garuhapé': {'color': '', 'img': 'img/escudos/Garuhapé.jpg'}, 
    'Montecarlo': {'color': 'bg-gray', 'img': 'img/escudos/Montecarlo.jpg'}, 
    'Caraguatay': {'color': '', 'img': 'img/escudos/Caraguatay.jpg'}, 
    'Ruiz de Montoya': {'color': 'bg-gray', 'img': 'img/escudos/Ruiz de Montoya.jpg'}}
    return render_template('index.html', towns=towns)

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/grid')
def grid():
    items = GridTest.query.all()
    return render_template('grid.html', items=items)