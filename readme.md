This script :
-converts all PDF files in a specified directory to pillow image objects
-extracts text from the images using tesseract
-searches the text for a given string pattern
-prints the filename and page number to the terminal if the pattern is found

usage: python run.py [input_dir] [pattern]

Make sure to adjust the directory paths as needed.

Installation:

conda create --name pdf_stringfinder pdf2image pillow pytesseract click

ensure you have poppler installed on your system using the command: 

sudo apt install poppler-utils