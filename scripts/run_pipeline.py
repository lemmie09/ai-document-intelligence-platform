from src.pipeline.document_pipeline import DocumentPipeline

pipeline = DocumentPipeline()

count = pipeline.process_document(
    "/Users/lemmiecarvalho/Downloads/reference paper/all papers/paper3.pdf"
)

print(f"\nStored {count} chunks in ChromaDB")