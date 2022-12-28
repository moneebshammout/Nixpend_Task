from flask import Flask, abort
from .routes import users_bp, home_bp
from .middleware import error_middleware


def _errorRout(app: Flask):
    """Handles Undefined routes"""

    @app.errorhandler(404)
    def page_not_found(error):
        abort(404, "Page not found")


def _initializeRoutes(app: Flask):
    """Initializes all routes in flask app.

    Args:
        app (Flask): Flask app
    """
    app.register_blueprint(users_bp)
    app.register_blueprint(home_bp)
    _errorRout(app)


def _initializeMiddlewares(app: Flask):
    app.errorhandler(Exception)(error_middleware(app))


def createApp():
    """Creates Flask app.


    Returns:
       app (Flask): Flask app
    """
    app = Flask(
        __name__,
    )
    _initializeMiddlewares(app)
    _initializeRoutes(app)

    return app
