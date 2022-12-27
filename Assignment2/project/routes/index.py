from flask import Blueprint, render_template


home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def handler():
    """
    Base route contains the form

    """
    return render_template("index.html")
