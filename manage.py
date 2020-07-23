from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from models import db

# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade

env_name = 'development'

app = create_app(env_name)

migrate = Migrate(app=app, db=db, compare_type=True)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
