import qrcode
from PIL import Image


def initQRCode():
    """Create qrcode instance.

    Returns:
        qrcode: qrcode instance
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    return qr


def imageQrcode(text: str):
    """Creates an image qrcode from text

    Args:
        text (str): Text to be encoded

    Returns:
        img: Qrcode image.
    """
    qr = initQRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    return img
