from src.vectors_store import search_chunks

question = " Give a summary of Information security, cybersecurity and privacy protection — Information security management systems — Requirements ."
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