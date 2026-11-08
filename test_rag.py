
from src.vectors_store import search_chunks
from src.llm import generate_answer

question = "Give a summary of Information security, cybersecurity and privacy protection — Information security management systems — Requirements in exactly 10 sentences."

#  Retrieve and rerank relevant chunks
results = search_chunks(question)

#  Check relevance before calling Gemini
if not results or results[0]["relevance_score"] <= 0:

    print("\nI couldn't find relevant information in the uploaded documents.")
    exit()

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
