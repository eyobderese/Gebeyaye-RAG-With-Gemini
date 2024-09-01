import PyPDF2
import os


def load_data():
    script_dir = os.path.dirname(__file__)
    pdf_path = '../context_Document/document.pdf'
    pdf_path = os.path.join(script_dir, '../context_Document/document.pdf')

    text = ""

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            # Extract text from each page
            page_text = page.extract_text() or ""
            # Append text to the main text variable, removing extra new lines and spaces
            text += page_text.replace('\n', ' ').strip() + " "

    # Optional: Remove extra spaces and newlines
    text = ' '.join(text.split())
    return text


def chunk_text(text, chunk_size=1000):
    chunks = []
    for i in range(0, len(text), chunk_size-100):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    return chunks
