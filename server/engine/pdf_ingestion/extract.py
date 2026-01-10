from . import (
    extract_text,
)


def extract(pdf_path:str, extract_type:str="text"):
    if extract_type == "text":
        print("Extracting text")
    elif extract_type == "image":
        print("Extracting image")
    elif extract_type == "table":
        print("Extracting table")
    else:
        raise Exception("Invalid extract type")