import os
from dotenv import load_dotenv


# Charge les variables d'environnement depuis le fichier .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    MAIL_SENDERS_KEY = os.getenv('MAIL_SENDERS_KEY')
    SMTP_USER = os.getenv('SMTP_USER')
    ADMIN_MAIL = os.getenv('ADMIN_MAIL')

    def __init__(self):
        if self.SQLALCHEMY_DATABASE_URI is None:
            #log.warn(CONFIG, "DATABASE_URL is not set in .env file")
            print("DATABASE_URL is not set in .env file")
