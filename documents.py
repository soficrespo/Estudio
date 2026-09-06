from pypdf import PdfReader
from docx import Document 

def extractTextPDF(file_path):
    reader = PdfReader(file_path)
    completeText =""
    for page in reader.pages:
        completeText += page.extract_text() + "\n"
    return completeText

def extractTextDocx(file_path):
    document = Document(file_path)
    completeText = ""
    for paragraph in document.paragraphs:
        completeText += paragraph.text + "\n"
    return completeText

def extractText(file_path):
    if file_path.endswith(".pdf"):
        return extractTextPDF(file_path)
    elif file_path.endswith(".docx"):
        return extractTextDocx(file_path)
    else:
        raise ValueError("Solo se acepta PDF o DOCX.")