This script converts all PDF files in a specified directory to PNG images.

usage: python run.py [input_dir] [pattern]

Make sure to adjust the directory paths as needed.

Installation:

conda create --name pdf_stringfinder pdf2image pillow pytesseract click

ensure you have poppler installed on your system using the command: 

sudo apt install poppler-utils