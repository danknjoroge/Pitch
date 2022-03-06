from . import db 
from werkzeug.security import generate_password_hash,check_password_hash



class User(db.Model):
    __tablename__ = 'users' #Allows us ggive table a name of our choices
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(121))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(45))


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



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'




# python3.8 manage.py db migrate -m "Initial Migration"
# python3.8 manage.py db upgrade

    



