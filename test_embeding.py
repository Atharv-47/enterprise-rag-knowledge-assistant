from sentence_transformers import SentenceTransformer

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample sentences
texts = [
    "Employees get 20 days of annual leave.",
    "Employees are entitled to 20 vacation days.",
    "The company provides medical insurance."
]

# Convert sentences into embeddings
embeddings = model.encode(texts)

# Display results
print("Shape:", embeddings.shape)

print("\nFirst sentence embedding:")
print(embeddings[0])