import PyPDF2
from PyPDF2 import PdfReader
import re
import fitz

# Open the PDF file in read-binary mode

def getText(filename):
    doc = fitz.open(filename)
    text = ""
    for page in doc:
        text+=page.get_text()
    return text

