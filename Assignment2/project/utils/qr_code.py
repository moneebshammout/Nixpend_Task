from PIL import Image
from io import BytesIO
import pyqrcode


def imageQrcode(text: str):
    """Creates an image qrcode from text

    Args:
        text (str): Text to be encoded

    Returns:
        str: Qrcode image path.
    """
    qr_code = pyqrcode.create(text, version=27, mode="binary")
    qr_path = "qr_code.png"
    qr_code.png(
        qr_path,
        scale=1,
        module_color=[0, 0, 0, 128],
        background=[0xFF, 0xFF, 0xCC],
    )

    return qr_path
