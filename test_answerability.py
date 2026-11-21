from src.vectors_store import search_chunks
from src.vectors_store import collection
questions = [
    "What are the requirements for establishing an ISMS?",
    "Which company provides information security certification?",
    "Who won the FIFA World Cup in 2022?"
]

for question in questions:

    print("\n" + "=" * 70)
    print("QUESTION:", question)

    results = search_chunks(question)
    print("Collection count:", collection.count())
    print("Retrieved count:", len(results))

    if not results:
        print("No results found.")
        continue

    print("\nTOP RETRIEVED CHUNKS:")

    for i, result in enumerate(results, start=1):
        print(f"\nChunk {i}")
        print("Page:", result["metadata"]["page"])
        print("Relevance score:", result["relevance_score"])
        print("Text:", result["text"][:300])