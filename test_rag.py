from src.vectors_store import search_chunks
from src.llm import generate_answer

question = " give summary of Information security, cybersecurity and privacy protection — Information security management systems — Requirements in 10 sentence "

results = search_chunks(question)

context = ""

for result in results:

    source = result["metadata"]["source"]
    page = result["metadata"]["page"]
    text = result["text"]

    context += f"""
    Source: {source}
    Page: {page}
    Content: {text}

    """

answer = generate_answer(question, context)

print("\nQuestion:", question)
print("\nAnswer:", answer)