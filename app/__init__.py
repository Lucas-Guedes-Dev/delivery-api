from flask import Flask

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    with app.app_context():
        from . import routes
        return app
