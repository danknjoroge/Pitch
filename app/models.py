from . import db 


class User(db.Model):
    __tablename__ = 'users' #Allows us ggive table a name of our choices
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(11))

    def __repr__(self):    # makes it easier to debug our application
        return f'User {self.username}'


    