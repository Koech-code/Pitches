import os

class Config:
    '''
    Parent configuration class 
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production configuration child class  
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    pass

    DEBUG = True

config_options={
    'development' :DevConfig,
    'production' :ProdConfig
}
    
