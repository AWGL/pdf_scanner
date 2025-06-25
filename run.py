# usage: python run.py [input_dir] [pattern]
# This script converts all PDF files in a specified directory to PNG images.
# Make sure to adjust the directory paths as needed.
# Ensure you have the required libraries installed:
# conda create --name pdf_stringfinder pdf2image pillow pytesseract click
# ensure you have poppler installed on your system using the command: sudo apt install poppler-utils

from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import glob
import os
import click

@click.command()
@click.argument('input_dir', type=click.Path(), default=".")#, help='Path to the directory containing PDF files. Default is current directory.')
@click.argument('pattern', type=click.STRING, default=None)#, help='string or pattern to seach for in the PDF files')

def main(input_dir, pattern):
    # Get all PDF files
    pdf_files = glob.glob(os.path.join(input_dir, "*.pdf"))
    print(f"Found {len(pdf_files)} PDF files.")

    for file in pdf_files:
        
        print(f"Processing file: {file}")
        filename = os.path.splitext(os.path.basename(file))[0]
        images = convert_from_path(file)  # Add poppler_path=... if needed
        
        for i, image in enumerate(images):
            
            image_filename = f"{filename} page {i + 1}"
            page_string = pytesseract.image_to_string(image)
            if pattern in page_string:
                print(f"Pattern '{pattern}' found in {image_filename}.")

if __name__ == "__main__":
    main()