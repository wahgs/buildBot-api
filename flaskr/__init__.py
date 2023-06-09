from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='create.env'
    )

    from .api import endpoints
    app.register_blueprint(endpoints, url_prefix='/api/')

    return app
