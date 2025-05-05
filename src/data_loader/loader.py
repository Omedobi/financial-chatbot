import fitz
import docx
import pandas as pd

def load_pdf_as_text(path: str) -> str:
    doc = fitz.open(path)
    return "\n".join([page.get_text() for page in doc])


def load_txt(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_docx(path: str) -> str:
    doc = docx.Document(path)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
