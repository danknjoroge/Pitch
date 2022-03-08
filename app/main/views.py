from flask import redirect, render_template, request, url_for,abort
from flask_login import login_required, current_user
from . import main
from ..models import Pitches, User
from .forms import PitchForm, UpdateProfile
from .. import db

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pitch Area. Where you pitch your ideas and get voted for'
    return render_template('index.html', title=title)


@main.route('/home',methods = ['GET','POST'])
def home():
    pitches= Pitches.query.all()
    return render_template('home.html', pitches=pitches)


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



##....
@main.route('/pitch/', methods = ['GET','POST'])
@login_required
def pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        pitches = form.pitches.data

        # Updated review instance
        new_pitch = Pitches(title=title,category=category,pitches=pitches,user=current_user)

        # save review method
        new_pitch.save_pitches()
        return redirect(url_for('.home'))

    return render_template('pitch.html',form=form)






