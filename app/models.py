from . import db 
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users' #Allows us ggive table a name of our choices
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitches',backref = 'user',lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute on this object')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):    # makes it easier to debug our application
        return f'User {self.username}'

   


class Pitches(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    category = db.Column(db.String(255))
    pitches = db.Column(db.String(2555))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship('Comments',backref = 'pitch',lazy = "dynamic")


    # users = db.relationship('User',backref = 'role',lazy="dynamic")

    def save_pitches(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        pitches= Pitches.query.filter_by(id=id).all()
        return pitches

    def __repr__(self):
        return f'User {self.name}'


class Comments(db.Model):
    __tablename__ ='comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))


    def save_comments(self):
        db.session.add(self)
        db.session.commit()



# python3.8 manage.py db init
# python3.8 manage.py db migrate -m "Initial Migration"
# python3.8 manage.py db upgrade

    



