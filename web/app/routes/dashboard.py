from flask import (
    Blueprint,
    render_template,
)

dashboard_app = Blueprint("dashboard", __name__)


@dashboard_app.get("/")
def index():
    return render_template("pages/dashboard/index.html")
