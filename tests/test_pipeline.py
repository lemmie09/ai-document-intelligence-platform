from src.ingestion.pdf_loader import PDFLoader
from src.processing.text_chunker import TextChunker
from src.embeddings.embedding_model import EmbeddingModel

# Step 1: Load PDF
loader = PDFLoader()
text = loader.load(
    "/Users/lemmiecarvalho/Downloads/reference paper/all papers/paper3.pdf"
)

print(f"Document Length: {len(text)} characters")

# Step 2: Chunk the text
chunker = TextChunker(chunk_size=500, overlap=100)
chunks = chunker.chunk(text)

print(f"Total Chunks: {len(chunks)}")

# Step 3: Load embedding model
model = EmbeddingModel()

# Step 4: Create embeddings
embeddings = []

for chunk in chunks:
    embedding = model.embed(chunk)
    embeddings.append(embedding)

print(f"Generated {len(embeddings)} embeddings")

print(f"Each embedding has {len(embeddings[0])} dimensions")