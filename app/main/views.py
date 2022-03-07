from flask import render_template
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pitch Area. Where you pitch your ideas and get voted for'
    return render_template('index.html', title=title)


@main.route('/home/')
def home():
    return render_template('home.html')