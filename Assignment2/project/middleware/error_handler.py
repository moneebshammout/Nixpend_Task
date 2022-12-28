from flask import jsonify


def error_middleware(app):
    """Middleware for handling errors.

    Args:
        app (Flask): Flask app.
    """

    def middleware(error):
        app.logger.error(error)
        return jsonify({"error occurred": str(error)}), 500

    return middleware
