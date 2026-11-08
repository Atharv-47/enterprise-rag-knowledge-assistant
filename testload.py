from src.document_loader import extract_text_from_pdf
from src.text_chunker import split_text

pdf_path = "data/sample_docs/sample.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = split_text(text)

print("Total chunks:", len(chunks))

print("\nFirst chunk:\n")
print(chunks[0])