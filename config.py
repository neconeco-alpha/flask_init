import os

#全環境で共通の設定
class CommonConfig(object):
    #ステータス
    ERROR = "error"
    WAIT = "wait"

class BaseConfig(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True


config = {
  "development": "config.DevelopmentConfig",
  "testing": "config.TestingConfig",
  "default": "config.DevelopmentConfig"
}

def configure_app(app):
  config_name = os.getenv('FLASK_CONFIGURATION', 'default')
  app.config.from_object(config[config_name])
