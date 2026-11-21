
import re
from langchain_text_splitters import RecursiveCharacterTextSplitter


def clean_text(text):

    # Normalize multiple spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Normalize excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    return text.strip()


def split_pages(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )

    all_chunks = []

    for page in pages:

        cleaned_text = clean_text(page["text"])

        page_chunks = splitter.split_text(cleaned_text)

        for chunk in page_chunks:

            all_chunks.append({
                "text": chunk,
                "page": page["page"]
            })

    return all_chunks
