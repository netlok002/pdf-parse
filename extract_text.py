from pathlib import Path
import pdfplumber

def extract_text_from_pdf(file_path):
    full_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n"
    return full_text

if __name__ == "__main__":
    # Get the path to the directory where this script is located.
    base_path = Path(__file__).resolve().parent
    # Build the relative path to the PDF file located in the 'pdf-parse-pickup' folder.
    pdf_file = base_path / "pdf-parse-pickup" / "Sample-Completed-SBC.pdf" 
    
    extracted_text = extract_text_from_pdf(pdf_file)
    print("Extracted Text:")
    print(extracted_text)

with open ('extracted_text.tst', 'w', encoding='utf-8') as f:
    f.write(extracted_text)