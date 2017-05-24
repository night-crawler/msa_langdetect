import os


class BaseConfig:
    CONFIG_FILE = os.path.abspath(__file__)
    CONFIG_DIR = os.path.dirname(CONFIG_FILE)
    BASE_DIR = os.path.abspath(os.path.join(CONFIG_DIR, '..'))

    DEBUG = False
    TESTING = False
    HOST = 'localhost'
    PORT = 21021


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True


config = {
    'default': 'msa_langdetect.config.DevelopmentConfig',
    'dev': 'msa_langdetect.config.DevelopmentConfig',
    'prod': 'msa_langdetect.config.ProductionConfig',
    'test': 'msa_langdetect.config.TestingConfig',
}


def configure_app(app, config_name='default'):
    config_name = os.getenv('msa_langdetect_CONFIG_NAME', None) or config_name

    app.config.from_object(config[config_name])
    app.config.from_envvar('msa_langdetect', silent=True)
