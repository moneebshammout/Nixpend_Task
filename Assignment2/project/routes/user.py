from flask import Blueprint, request, send_file
from ..service.user import getQRCodePDF

users_bp = Blueprint("user", __name__)


@users_bp.route("/user", methods=["POST"])
def handler():
    """Submit user data rout

    Returns:
        PDF: pdf containing QRcode.
    """
    data = request.form
    buffer = getQRCodePDF(data)
    send_file(buffer, as_attachment=True, attachment_filename="qr_code.pdf")
    return "pdf generated", 200
