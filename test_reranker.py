from sentence_transformers import CrossEncoder

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

from src.vectors_store import search_chunks

questions = [
    # Relevant questions
    "What are the requirements of an information security management system?",
    "How does an organization determine the scope of its ISMS?",
    "What is the purpose of an information security policy?",
    "What are the responsibilities of top management?",
    "What is the role of risk assessment in an ISMS?",
    
    "Which company provides the information security certification for an organization?",

    # Unrelated questions
    "Who won the FIFA World Cup in 2022?",
    "How do I cook vegetable biryani?",
    "What is the capital of Japan?",
    "Explain Python dictionaries.",
    "How does a combustion engine work?"
]

for question in questions:

    results = search_chunks(question)

    print("\nQuestion:", question)

    if not results or results[0]["relevance_score"] <= 0:

        print("I couldn't find relevant information in the uploaded documents.")

    else:

        print("Top relevance score:", results[0]["relevance_score"])

        for result in results:

            print("\nPage:", result["metadata"]["page"])
            print("Score:", result["relevance_score"])
            print("Content:", result["text"][:200])
            print("-" * 40)