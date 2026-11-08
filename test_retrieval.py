from src.vectors_store import search_chunks

question = "Who won the FIFA World Cup in 2022? ."
results = search_chunks(question)

if not results:
    print("No results found.")

else:
    for result in results:

        print("\nDistance:", result["distance"])
        print("Source:", result["metadata"]["source"])
        print("Content:", result["text"])
        print("-" * 50)
        print("Page:", result["metadata"]["page"])