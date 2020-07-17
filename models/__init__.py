from flask_sqlalchemy import SQLAlchemy

# initialize our db
db = SQLAlchemy()

from models.models import PersonModel, PersonSchema
