from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import glob
import os
import click

@click.command()
@click.argument('input_dir', type=click.Path(), default=".")#, help='Path to the directory containing PDF files. Default is current directory.')
@click.argument('output_file_name', type=click.Path(), default="search_results.txt")#, help='Path to the directory to save output text file. Default is current directory.')
@click.argument('pattern', type=click.STRING, default=None)#, help='string or pattern to seach for in the PDF files')

def main(input_dir, output_file_name, pattern):
    
    # Get all PDF files
    pdf_files = glob.glob(os.path.join(input_dir, "*.pdf"))
    with open(f"./output/{output_file_name}", "w") as f:
        f.write(f"Found {len(pdf_files)} PDF files. \n")

        for file in pdf_files:
            
            f.write(f"Processing file: {file} \n")
            filename = os.path.splitext(os.path.basename(file))[0]
            images = convert_from_path(file)  # Add poppler_path=... if needed
            
            for i, image in enumerate(images):
                
                image_filename = f"{filename} page {i + 1}"
                page_string = pytesseract.image_to_string(image)
                if pattern in page_string:
                    f.write(f"    Pattern '{pattern}' found in {image_filename}.\n")

if __name__ == "__main__":
    main()