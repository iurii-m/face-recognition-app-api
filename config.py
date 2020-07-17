
class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'
    SQLALCHEMY_DATABASE_URI = 'postgres://nwjgnmowyjhzwm:84f92b1235116e7a38d36d5ac80def2c055145da510234cdaced7ad83a0a6020@ec2-54-246-85-151.eu-west-1.compute.amazonaws.com:5432/d651ls57l2uga'


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgres://nwjgnmowyjhzwm:84f92b1235116e7a38d36d5ac80def2c055145da510234cdaced7ad83a0a6020@ec2-54-246-85-151.eu-west-1.compute.amazonaws.com:5432/d651ls57l2uga'
    JWT_SECRET_KEY = 'hhgaghhgsdhdhdd'


app_config = {
    'development': Development,
    'production': Production,
}