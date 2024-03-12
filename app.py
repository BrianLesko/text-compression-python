# Brian Lesko
# 11/24/2023

import streamlit as st
from customize_gui import gui as gui 
gui = gui()

import Quartz # pip install pyobjc
from CoreFoundation import CFURLCreateFromFileSystemRepresentation


def extract_text_from_pdf(pdf_path):
    pdf_url = CFURLCreateFromFileSystemRepresentation(
        None, pdf_path.encode('utf-8'), len(pdf_path), False
    )
    pdf_doc = Quartz.PDFKit.PDFDocument.alloc().initWithURL_(pdf_url)

    if pdf_doc is None:
        print(f"Failed to load PDF file: {pdf_path}")
        return None

    extracted_text = ""
    for i in range(pdf_doc.pageCount()):
        page = pdf_doc.pageAtIndex_(i)
        if page is not None:
            extracted_text += page.string()

    return extracted_text

gui.setup(wide=True, text="Extract Text from PDF files. Enter the path to the file.")
st.title('Extract Text from PDF files')

# Usage
path = st.chat_input('Enter the path to the PDF file')
if path: 
    text = extract_text_from_pdf(path)
    if text:
        st.write(text)