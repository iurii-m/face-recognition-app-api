from flask import Flask

from models import db
from config import app_config

# importa a blueprint
from views.views import person_api as person_blueprint

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    Example endpoint
    """
    return 'Congratulations! Your first endpoint is workin'


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    application = Flask(__name__)

    # app.run(host='0.0.0.0',port=5000)

    application.config.from_object(app_config[env_name])

    db.init_app(application)  # add this line

    # Register the blueprint
    # For example: http://127.0.0.1:5000/api/all/  --> All people
    application.register_blueprint(person_blueprint, url_prefix='/api/')

    @application.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """

        return 'Congratulations! Your first endpoint is workin'

    return application
