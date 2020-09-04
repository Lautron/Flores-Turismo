from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/grid')
def grid():
    items = {
    'Ruiz de Montoya': 'img/Ruiz de Montoya.jpg', 
    'Puerto Rico': 'img/Puerto Rico.jpg', 
    'Capiovi': 'img/Capiovi.jpg', 
    'El alcazar': 'img/El alcazar.jpg',
    'Ruiz de Montoya2': 'img/Ruiz de Montoya.jpg', 
    'Puerto Rico2': 'img/Puerto Rico.jpg', 
    'Capiovi2': 'img/Capiovi.jpg', 
    'El alcazar2': 'img/El alcazar.jpg',
    'Ruiz de Montoya3': 'img/Ruiz de Montoya.jpg', 
    'Puerto Rico3': 'img/Puerto Rico.jpg', 
    'Capiovi3': 'img/Capiovi.jpg', 
    'El alcazar3': 'img/El alcazar.jpg',
    'Ruiz de Montoya': 'img/Ruiz de Montoya.jpg', 
    'Puerto Rico': 'img/Puerto Rico.jpg', 
    'Capiovi': 'img/Capiovi.jpg', 
    'El alcazar': 'img/El alcazar.jpg',
    }
    return render_template('grid.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)