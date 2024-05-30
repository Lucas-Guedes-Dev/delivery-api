from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from auth.routes import auth_bp

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp, url_prefix='/auth')

    # TODO *** não apague isso, é para debugar melhor a aplicalção quando preciso ***
    # with app.app_context():
    #     print_routes(app)

    app.run(host="192.168.0.211", port=5050, debug=True)

# TODO *** use esse metodo para debugar as endpoints que estão registrados ***
# def print_routes(app):
#     for rule in app.url_map.iter_rules():
#         methods = ','.join(sorted(rule.methods))
#         print(f'{rule.endpoint}: {rule.rule} [{methods}]')

if __name__ == '__main__':
    create_app()
