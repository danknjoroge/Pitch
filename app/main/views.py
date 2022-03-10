from flask import redirect, render_template, request, url_for,abort
from flask_login import login_required, current_user
from . import main
from ..models import Pitches, User,Comments
from .forms import PitchForm, UpdateProfile, CommentForm
from .. import db,photos

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pitch Area. Where you pitch your ideas and get voted for'
    return render_template('index.html', title=title)


@main.route('/home',methods = ['GET','POST'])
@login_required
def home():
    pitches= Pitches.query.all()
    comments= Comments.query.all()
    return render_template('home.html', pitches=pitches, comments=comments)

@main.route('/view/',methods = ['GET','POST'])
@login_required
def view():
    comments= Comments.query.all()
    return render_template('view.html', comments=comments)


# @main.route('/categories/')
# def categories():
#     return render_template('categories.html')

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

        # Updating 
        new_pitch = Pitches(title=title,category=category,pitches=pitches,user=current_user)

        # save review method
        new_pitch.save_pitches()
        return redirect(url_for('.home'))

    return render_template('pitch.html',form=form)


@main.route('/comment/', methods=['GET','POST'])
@login_required
def comment():
    form= CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(comment=comment)

        new_comment.save_comments()
        return redirect(url_for('.home'))

    return render_template('comment.html', form=form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))






