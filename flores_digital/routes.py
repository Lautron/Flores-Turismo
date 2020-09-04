from flask import render_template
from flores_digital import app
from flores_digital.models import GridTest

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/grid')
def grid():
    items = GridTest.query.all()
    return render_template('grid.html', items=items)