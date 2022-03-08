from flask import redirect, render_template, request, url_for,abort
from flask_login import login_required
from . import main
from ..models import User
from .forms import UpdateProfile
from .. import db

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


@main.route('/categories/')
def categories():
    return render_template('categories.html')



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)