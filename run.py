# usage: python run.py
# This script converts all PDF files in a specified directory to PNG images.
# Make sure to adjust the directory paths as needed.
# Ensure you have the required libraries installed:
# conda create --name pdf2image pdf2image pillow 
# ensure you have poppler installed on your system using the command: sudo apt install poppler-utils

# parser.add_argument('filename') 

from pdf2image import convert_from_path
from PIL import Image
from tesseract
import glob
import os

file_pattern = "*.pdf"
directory_path = os.path.expanduser("~/Documents/shimano/")
output_path = os.path.expanduser("~/Documents/shimano/images/")

# Ensure output path exists
os.makedirs(output_path, exist_ok=True)

# Get all PDF files
pdf_files = glob.glob(os.path.join(directory_path, file_pattern))
print(f"Found {len(pdf_files)} PDF files.")

for file_path in pdf_files:
    
    print(f"Processing file: {file_path}")
    filename = os.path.splitext(os.path.basename(file_path))[0]
    images = convert_from_path(file_path)  # Add poppler_path=... if needed
    
    for i, image in enumerate(images):
        
        image_filename = f"{filename}_page_{i + 1}.png"
        image_path = os.path.join(output_path, image_filename)
        image.save(image_path, "PNG")
        print(f"Saved: {image_path}")