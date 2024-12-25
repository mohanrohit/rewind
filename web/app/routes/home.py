import os
import requests

from flask import (
    Blueprint,
    request,
    render_template,
)

home_app = Blueprint("home", __name__)


@home_app.get("/")
def index():
    return render_template("pages/home/index.html")
