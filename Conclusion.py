import re
import PyPDF2

# Open the PDF file in binary mode
with open('Carbonated.pdf', 'rb') as pdf_file:

    # Create a PyPDF2 reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Iterate through each page
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.get_page_number(page_num)

        # Extract the page text
        page_text = page.extractText()

        # Use regular expressions to find the conclusion heading
        match = re.search(r'\nConclusion\n', page_text)

        # If the conclusion heading is found, print it and break out of the loop
        if match:
            print(match.group(0))
            break