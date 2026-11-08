from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_pages(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )

    all_chunks = []

    for page in pages:

        page_chunks = splitter.split_text(page["text"])

        for chunk in page_chunks:

            all_chunks.append({
                "text": chunk,
                "page": page["page"]
            })

    return all_chunks