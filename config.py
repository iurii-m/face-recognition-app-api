
class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'
    SQLALCHEMY_DATABASE_URI = 'postgres://bcjvkxzttihwua:5ec611f4077ad84d4a4cfc63fcf84e7dfbcc2ed644ebea903f1d963edf89f469@ec2-54-217-213-79.eu-west-1.compute.amazonaws.com:5432/d8pltdd2quqsdh'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgres://bcjvkxzttihwua:5ec611f4077ad84d4a4cfc63fcf84e7dfbcc2ed644ebea903f1d963edf89f469@ec2-54-217-213-79.eu-west-1.compute.amazonaws.com:5432/d8pltdd2quqsdh'
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'development': Development,
    'production': Production,
}