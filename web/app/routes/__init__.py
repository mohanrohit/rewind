from flask import Flask

from .home import home_app
from .dashboard import dashboard_app


def initialize(app: Flask):
    app.register_blueprint(dashboard_app, url_prefix="/dashboard")

    app.register_blueprint(home_app)
