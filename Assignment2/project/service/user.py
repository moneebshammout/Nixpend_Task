from flask import send_file
from ..utils import qr_code, pdf


def getQRCodePDF(data: dict):
    """Generates QRcode pdf based on user data.

    Returns:
        send_file: Sends pdf file to client.
    """
    name = data["fullName"]
    email = data["email"]
    phone = data["phone"]
    try:
        qr_code_path = qr_code.imageQrcode(f"{name} {email} {phone}")
        pdf_path = pdf.createPDF(qr_code_path)
        return send_file(f"../{pdf_path}", as_attachment=True, download_name=pdf_path)
    except:
        return "There was an issue generating pdf file"
