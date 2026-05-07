from flask import Flask
from config import Config
from infrastructure.database.database import db

from flask_cors import CORS

from application.controllers.controller import globalBp

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)
db.init_app(app)

# Registering blueprints
app.register_blueprint(globalBp)


# Création des tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()