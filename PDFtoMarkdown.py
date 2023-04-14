import fitz  # PyMuPDF library

def pdf_to_markdown(pdf_path):
    md_text = ""  # Markdown text
    pdf_doc = fitz.open(pdf_path)

    for page_idx in range(pdf_doc.page_count):
        page = pdf_doc.load_page(page_idx)
        page_text = page.get_text("text")  # Extract text from page

        # Remove trailing whitespaces and add new line
        page_text = page_text.rstrip() + "\n\n"

        md_text += page_text

    pdf_doc.close()
    return md_text

# Prompt user for PDF file name
pdf_path = input("Enter the name of the PDF file: ")

# Generate markdown text
markdown_text = pdf_to_markdown(pdf_path)

# Prompt user for output file name
output_file_name = input("Enter the name of the output file (without extension): ")
output_file_name += ".txt"  # Add .txt extension to the file name

# Save markdown text to output file
with open(output_file_name, "w", encoding="utf-8") as f:p
    f.write(markdown_text)

print(f"Markdown text has been saved to {output_file_name}")







