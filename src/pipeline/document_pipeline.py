from src.ingestion.pdf_loader import PDFLoader
from src.processing.text_chunker import TextChunker
from src.embeddings.embedding_model import EmbeddingModel
from src.vectorstore.chroma_store import ChromaStore


class DocumentPipeline:

    def __init__(self):

        self.loader = PDFLoader()
        self.chunker = TextChunker(chunk_size=500, overlap=100)
        self.embedding_model = EmbeddingModel()
        self.vector_store = ChromaStore()

    def process_document(self, pdf_path):

        print("Loading PDF...")
        text = self.loader.load(pdf_path)

        print("Chunking document...")
        chunks = self.chunker.chunk(text)

        print("Generating embeddings...")
        embeddings = [
            self.embedding_model.embed(chunk)
            for chunk in chunks
        ]

        print("Saving to ChromaDB...")
        self.vector_store.add_documents(chunks, embeddings)

        print("Done!")

        return len(chunks)