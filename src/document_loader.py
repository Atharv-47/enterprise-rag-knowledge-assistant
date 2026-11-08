import pymupdf


def extract_pages_from_pdf(pdf_path):

    doc = pymupdf.open(pdf_path)

    pages = []

    for page_number, page in enumerate(doc, start=1):

        page_text = page.get_text()

        if page_text.strip():
            pages.append({
                "page": page_number,
                "text": page_text
            })

    doc.close()

    return pages


# Keep the original function for existing tests
def extract_text_from_pdf(pdf_path):

    pages = extract_pages_from_pdf(pdf_path)

    return "\n".join(page["text"] for page in pages)