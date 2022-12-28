from flask import Blueprint, request
from ..service.user import getQRCodePDF

users_bp = Blueprint("user", __name__)


@users_bp.route("/user", methods=["POST"])
def handler():
    """Submit user data rout

    Returns:
        PDF: pdf containing QRcode.
    """
    data = request.form
    return getQRCodePDF(data)
