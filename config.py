import os
from dotenv import load_dotenv


# Charge les variables d'environnement depuis le fichier .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SMTP_HOST = os.getenv('SMTP_HOST')
    SMTP_PORT = os.getenv('SMTP_PORT')
    SMTP_USER = os.getenv('SMTP_USER')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
    ADMIN_MAIL = os.getenv('ADMIN_MAIL')

    def __init__(self):
        if self.SQLALCHEMY_DATABASE_URI is None:
            #log.warn(CONFIG, "DATABASE_URL is not set in .env file")
            print("DATABASE_URL is not set in .env file")
