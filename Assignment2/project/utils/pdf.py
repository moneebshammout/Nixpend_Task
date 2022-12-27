from PIL import Image
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas


def createPDF(img: Image):
    """Create Pdf file from image.

    Args:
        img (Image): Image to be painted.

    Returns:
        Buffer: The byte object of the pdf.
    """

    buffer = BytesIO()

    # Create a PDF canvas
    canvas = Canvas(buffer, pagesize=A4)

    # Draw the QR code on the canvas
    canvas.drawImage(img, x=10, y=10, width=100, height=100)

    # Save the PDF
    canvas.save()

    # Seek to the beginning of the BytesIO object
    buffer.seek(0)
    return buffer
