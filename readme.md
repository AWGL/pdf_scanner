### PDF_scanner

* converts all PDF files in a specified directory to pillow image objects
* extracts text from the images using tesseract
* searches the text for a given pattern
* prints the filename and page number to a text file with a given filename if the pattern is found

**Usage:**

`python run.py [OPTIONS] [INPUT_DIR] [OUTPUT_FILE_NAME] PATTERN`

    Search for a REGEX PATTERN in all PDF files in INPUT_DIR and write results
    to OUTPUT_FILE_NAME.
    
    Options:
    -i, --ignore-case  Perform case-insensitive regex matching.
    -f, --fuzzy        Enable fuzzy matching (up to 2 errors).
    --help             Show this message and exit.


**Installation:**

`conda create --name pdf_scanner pdf2image pillow pytesseract click regex`

`conda activate pdf_scanner`

Ensure you have poppler installed on your system using the command: 

`sudo apt install poppler-utils`

---

See example output "search_shimano.txt" in ./output

Test PDFs can be found in ./test_pdfs