class Config:
    """ General configuration parent class """

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?language=en&category={}&q={}&apiKey={}'


class ProdConfig(Config):
    """
    Production configuration class
    Args:
        Config: The parent configuration class with General Configuration settings
    """
    pass


class DevConfig(Config):
    """
    Development confiiguration class
    Args:
        Config: The parent Configuration class with General Configuration settings
    """

    DEBUG = True
