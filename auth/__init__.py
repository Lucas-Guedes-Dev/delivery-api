from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import routes, models
        return app
