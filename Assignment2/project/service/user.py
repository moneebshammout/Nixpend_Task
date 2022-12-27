from ..utils import qr_code, pdf


def getQRCodePDF(data: dict):
    """Generates QRcode pdf based on user data.

    Returns:
        buffer: PDF bytes object.
    """
    name = data["fullName"]
    email = data["email"]
    phone = data["phone"]
    image = qr_code.imageQrcode(f"{name} {email} {phone}")
    buffer = pdf.createPDF(image)

    return buffer
