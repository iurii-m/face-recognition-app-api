
class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:root@localhost:5432/FaceRecognition'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:root@localhost:5432/FaceRecognition'
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'development': Development,
    'production': Production,
}