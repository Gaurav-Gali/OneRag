import pymupdf

def extract_text(pdf_path:str):
    doc = pymupdf.open(pdf_path)

    for page in doc:
        text = page.get_text("text")
        print(text)

