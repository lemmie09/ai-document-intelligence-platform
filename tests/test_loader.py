from src.ingestion.pdf_loader import PDFLoader

loader = PDFLoader()

text = loader.load("/Users/lemmiecarvalho/Downloads/reference paper/all papers/paper3.pdf")

print(text[:500])