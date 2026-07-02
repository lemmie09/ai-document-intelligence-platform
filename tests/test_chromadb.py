from src.ingestion.pdf_loader import PDFLoader
from src.processing.text_chunker import TextChunker
from src.embeddings.embedding_model import EmbeddingModel
from src.vectorstore.chroma_store import ChromaStore

loader = PDFLoader()
text = loader.load(
    "/Users/lemmiecarvalho/Downloads/reference paper/all papers/paper3.pdf"
)

chunker = TextChunker(chunk_size=500, overlap=100)
chunks = chunker.chunk(text)

model = EmbeddingModel()

embeddings = [model.embed(chunk) for chunk in chunks]

store = ChromaStore()

store.add_documents(chunks, embeddings)

query = "What are solar flares?"

query_embedding = model.embed(query)

results = store.search(query_embedding)

print(results["documents"][0])