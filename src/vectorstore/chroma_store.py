import chromadb
from chromadb import PersistentClient


class ChromaStore:

    def __init__(self):
        self.client = PersistentClient(path="./chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="research_papers"
        )

    def add_documents(self, chunks, embeddings):

        ids = [f"chunk_{i}" for i in range(len(chunks))]

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=[embedding.tolist() for embedding in embeddings]
        )

    def search(self, embedding, n_results=3):

        return self.collection.query(
            query_embeddings=[embedding.tolist()],
            n_results=n_results
        )