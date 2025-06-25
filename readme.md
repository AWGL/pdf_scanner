This script :

* converts all PDF files in a specified directory to pillow image objects
* extracts text from the images using tesseract
* searches the text for a given string pattern
* prints the filename and page number to the terminal if the pattern is found

usage: python run.py [input_dir] [pattern]

Make sure to adjust the directory paths as needed.

Installation:

conda create --name pdf_stringfinder pdf2image pillow pytesseract click

ensure you have poppler installed on your system using the command: 

sudo apt install poppler-utils

Note that the pattern is case-sensitive
See example output below:

![Screenshot from 2025-06-25 17-01-51](https://github.com/user-attachments/assets/64b45d78-c775-4a86-b5ed-74f24dbe9c01)

Test PDFs can be found in the test_pdfs folder
