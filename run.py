import os
import glob
import regex as re  # enhanced regex with fuzzy matching support
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import click
from datetime import datetime

def log(message, file):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    file.write(f"{timestamp} {message}\n")

@click.command()
@click.argument('input_dir', type=click.Path(exists=True, file_okay=False), default='.')
@click.argument('output_file_name', type=str, default='search_results.txt')
@click.argument('pattern', type=str, required=True)
@click.option('--ignore-case', '-i', is_flag=True, help='Perform case-insensitive regex matching.')
@click.option('--fuzzy', '-f', is_flag=True, help='Enable fuzzy matching (up to 2 errors).')
def main(input_dir, output_file_name, pattern, ignore_case, fuzzy):
    """
    Search for a REGEX PATTERN in all PDF files in INPUT_DIR and write results to OUTPUT_FILE_NAME.
    """
    flags = re.IGNORECASE if ignore_case else 0

    # If fuzzy, append fuzzy matching syntax to pattern
    fuzzy_suffix = "{e<=2}" if fuzzy else ""
    try:
        regex = re.compile(f"({pattern}){fuzzy_suffix}", flags)
    except re.error as e:
        click.echo(f"Invalid regular expression: {e}")
        return

    output_dir = "./output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_file_name)

    pdf_files = glob.glob(os.path.join(input_dir, "*.pdf"))

    with open(output_path, "w") as f:
        log(f"Found {len(pdf_files)} PDF file(s) in '{input_dir}'.", f)
        log(f"Regex pattern: '{pattern}' (ignore case: {ignore_case}, fuzzy: {fuzzy})", f)

        for file in pdf_files:
            log(f"Processing file: {file}", f)
            try:
                filename = os.path.splitext(os.path.basename(file))[0]
                images = convert_from_path(file)
            except Exception as e:
                log(f"    Error converting {file} to images: {e}", f)
                continue

            for i, image in enumerate(images):
                image_name = f"{filename} page {i + 1}"
                try:
                    page_text = pytesseract.image_to_string(image)
                    matches = regex.findall(page_text)
                    if matches:
                        log(f"    Pattern found in {image_name} ({len(matches)} match(es)):", f)
                        for match in matches:
                            if isinstance(match, tuple):  # handle capturing groups
                                match = match[0]
                            f.write(f"        Match: {match}\n")
                except Exception as e:
                    log(f"    OCR failed on {image_name}: {e}", f)

if __name__ == "__main__":
    main()
