import chromadb
from sentence_transformers import SentenceTransformer
import numpy as np
# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create a persistent ChromaDB database
client = chromadb.PersistentClient(
    path="data/chroma_db"
)

# Create or access a collection
collection = client.get_or_create_collection(
    name="enterprise_documents"
)
def cosine_similarity(a, b):

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )
def mmr_selection(
    query_embedding,
    candidate_embeddings,
    top_k=5,
    lambda_param=0.7
):

    selected = []
    remaining = list(range(len(candidate_embeddings)))

    while remaining and len(selected) < top_k:

        best_score = float("-inf")
        best_index = None

        for index in remaining:

            relevance = cosine_similarity(
                query_embedding,
                candidate_embeddings[index]
            )

            if not selected:
                diversity_penalty = 0

            else:
                diversity_penalty = max(
                    cosine_similarity(
                        candidate_embeddings[index],
                        candidate_embeddings[selected_index]
                    )
                    for selected_index in selected
                )

            mmr_score = (
                lambda_param * relevance
                - (1 - lambda_param) * diversity_penalty
            )

            if mmr_score > best_score:
                best_score = mmr_score
                best_index = index

        selected.append(best_index)
        remaining.remove(best_index)

    return selected

def store_chunks(chunks, source):

    documents = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(documents).tolist()

    ids = [
        f"{source}_{i}"
        for i in range(len(chunks))
    ]

    metadatas = [
    {
        "source": source,
        "page": chunk["page"],
        "chunk_index": i
    }
    for i, chunk in enumerate(chunks)
]
    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Successfully stored {len(chunks)} chunks.")

def search_chunks(question, n_results=5):

    query_embedding = model.encode(question)

    candidate_k = min(10, collection.count())

    if candidate_k == 0:
        return []

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=candidate_k,
        include=["documents", "metadatas", "distances", "embeddings"]
    )

    candidate_embeddings = results["embeddings"][0]

    selected_indices = mmr_selection(
    query_embedding,
    candidate_embeddings,
    top_k=min(n_results, candidate_k),
    
)

    retrieved_chunks = []

    for i in selected_indices:

        retrieved_chunks.append({
            "text": results["documents"][0][i],
            "distance": results["distances"][0][i],
            "metadata": results["metadatas"][0][i]
        })

    return retrieved_chunks

