### PDF_scanner

* converts all PDF files in a specified directory to pillow image objects
* extracts text from the images using tesseract
* searches the text for a given string pattern
* prints the filename and page number to a text file with a given filename if the pattern is found

usage: `python run.py [input_dir] [output_dir] [pattern]`

Make sure to adjust the directory paths as needed.

**Installation:**

`conda create --name pdf_scanner pdf2image pillow pytesseract click

conda activate pdf_scanner`

ensure you have poppler installed on your system using the command: 

`sudo apt install poppler-utils`

---

Note that the pattern is case-sensitive

See example output "search_shimano.txt" in ./output

Test PDFs can be found in ./test_pdfs