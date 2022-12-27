from flask import Flask, url_for, request, redirect
from .routes import users_bp, home_bp


def _errorRout(app: Flask):
    """Handles Undefined routes"""

    @app.errorhandler(404)
    def page_not_found(error):
        return "Sorry, the page you are looking for could not be found.", 404


def _initializeRoutes(app: Flask):
    """Initializes all routes in flask app.

    Args:
        app (Flask): Flask app
    """
    app.register_blueprint(users_bp)
    app.register_blueprint(home_bp)
    _errorRout(app)


def createApp():
    """Creates Flask app.


    Returns:
       app (Flask): Flask app
    """
    app = Flask(
        __name__,
    )
    _initializeRoutes(app)

    return app
