
from src.vectors_store import search_chunks
from src.llm import generate_answer

questions = [
    "What are the requirements for establishing an ISMS?"]
    

#  Retrieve and rerank relevant chunks
for question in questions:
    results = search_chunks(question)
    for i, result in enumerate(results, start=1):
        print(f"\n--- Retrieved Chunk {i} ---")
        print("Page:", result["metadata"]["page"])
        print("Score:", result["relevance_score"])
        print("Text:", result["text"][:300])

    #  Check relevance before calling Gemini
    if not results:
        print("\nI couldn't find relevant information in the uploaded documents.")
        continue

    #  Build context and collect unique citations
    context = ""

    citations = []
    seen = set()

    for result in results:

        source = result["metadata"]["source"]
        page = result["metadata"]["page"]
        text = result["text"]

        citation = (source, page)

        if citation not in seen:
            citations.append(citation)
            seen.add(citation)

        citation_id = citations.index(citation) + 1

        context += f"""
    [Source ID: {citation_id}]
    Source: {source}
    Page: {page}
    Content: {text}
    """

    #  Display source references
    print("\nSources:")

    for i, (source, page) in enumerate(citations, start=1):

        print(f"[{i}] {source}, Page {page}")

    # Generate answer using Gemini
    answer = generate_answer(question, context)

    print("\nQuestion:", question)
    print("\nAnswer:", answer)
