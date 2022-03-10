from app import create_app,db
from flask_script import Manager,Server
from app.models import User, Pitches, Comments
from flask_migrate import Migrate, MigrateCommand

# create app instance
app = create_app('development')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Pitches=Pitches, Comments = Comments)



if __name__ == '__main__':
    manager.run()
    db.create_all()

