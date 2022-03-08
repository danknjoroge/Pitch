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
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")


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
    pitches = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

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




# python3.8 manage.py db migrate -m "Initial Migration"
# python3.8 manage.py db upgrade

    



