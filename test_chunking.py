from src.document_loader import extract_pages_from_pdf
from src.text_chunker import split_pages

pdf_path = "data/sample_docs/sample.pdf"

# Extract pages
pages = extract_pages_from_pdf(pdf_path)

# Clean and split pages
chunks = split_pages(pages)

print("Total pages:", len(pages))
print("Total chunks:", len(chunks))

# Display all chunks with short previews
for i, chunk in enumerate(chunks, start=1):

    print("\n" + "=" * 60)
    print("CHUNK:", i)
    print("PAGE:", chunk["page"])
    print("CHARACTERS:", len(chunk["text"]))
    print("PREVIEW:", chunk["text"][:150].replace("\n", " "))