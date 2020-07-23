
class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'
    SQLALCHEMY_DATABASE_URI = 'postgres://jhcczpalikdmre:9c13f335038b70092acfb67e5ae100cc94f990400d60be83d7166c272a141cf2@ec2-54-247-94-127.eu-west-1.compute.amazonaws.com:5432/d9qqpi5k7s7ek2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgres://jhcczpalikdmre:9c13f335038b70092acfb67e5ae100cc94f990400d60be83d7166c272a141cf2@ec2-54-247-94-127.eu-west-1.compute.amazonaws.com:5432/d9qqpi5k7s7ek2'
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'development': Development,
    'production': Production,
}