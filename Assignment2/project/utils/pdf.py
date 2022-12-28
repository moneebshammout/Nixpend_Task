from fpdf import FPDF


def createPDF(path: str):
    """Create Pdf file from image.

    Args:
        path (str): Image path.

    Returns:
        str: path to pdf file.
    """

    pdf = FPDF()
    pdf.add_page()
    pdf.image(path, x=30, y=100, w=150, h=150)
    pdf_path = "qr_code.pdf"
    pdf.output(pdf_path, "F")
    return pdf_path
