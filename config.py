import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = '9a26301b6d9a4146830585e0ffb8da70'
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?language=en&category={}&q={}&apiKey={}'


class ProdConfig(Config):
    '''
    Pruduction configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
