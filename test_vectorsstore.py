from src.document_loader import extract_pages_from_pdf
from src.text_chunker import split_pages
from src.vectors_store import store_chunks

pdf_path = "data/sample_docs/sample.pdf"

# Extract individual PDF pages
pages = extract_pages_from_pdf(pdf_path)

# Split pages into chunks
chunks = split_pages(pages)


# Store chunks and metadata
store_chunks(
    chunks,
    source="sample.pdf"
)
from src.vectors_store import collection

