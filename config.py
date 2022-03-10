import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'
    SECRET_KEY = '\xff\\1\x95$\xb4E\xa1\xe8\xe2\xc42\x8f\x06\x1f\x13\xc6\xb8\xc8)V\x18G('
    UPLOADED_PHOTOS_DEST ='app/static/photos'


    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'dannjoro433@gmail.com'
    MAIL_PASSWORD = 'kahora12'
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}
