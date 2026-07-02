from src.embeddings.embedding_model import EmbeddingModel
from src.vectorstore.chroma_store import ChromaStore
from src.llm.ollama_client import OllamaClient

model = EmbeddingModel()
store = ChromaStore()
llm = OllamaClient()

question = input("Ask a question: ")

query_embedding = model.embed(question)

results = store.search(query_embedding, n_results=5)

print("\nRetrieved Chunks:\n")

documents = results["documents"][0]
distances = results["distances"][0]

for i, (doc, distance) in enumerate(zip(documents, distances), start=1):
    print("=" * 70)
    print(f"Chunk {i}")
    print(f"Similarity Score: {distance:.4f}")
    print()
    print(doc[:400])
    print()

context = "\n\n".join(documents)
answer = llm.ask(question, context)

print("\nAnswer:\n")
print(answer)