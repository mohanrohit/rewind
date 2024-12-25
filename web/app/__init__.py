from dotenv import load_dotenv
load_dotenv()

from flask import Flask

import jinja_partials

def create_app(config_name="development"):
    app = Flask(__name__, static_folder="../public")

    initialize_config(app, config_name)
    initialize_context(app)
    initialize_extensions(app)
    initialize_routes(app)
    initialize_assets(app)

    return app


def initialize_context(app: Flask):
    # set up other variables that will be available in templates
    @app.context_processor
    def inject_app_context():
        return { "app": app }


def initialize_config(app: Flask, config_name="development"):
    if config_name in ["development", "testing", "production"]:
        app.config.from_object(f"config.{config_name}")
    else:
        app.config.from_object("config.development")


def initialize_extensions(app: Flask):
    # Jinja partials
    jinja_partials.register_extensions(app)


def initialize_routes(app: Flask):
    from app import routes

    routes.initialize(app)


def initialize_assets(app: Flask):
    from app import assets

    assets.initialize(app)
