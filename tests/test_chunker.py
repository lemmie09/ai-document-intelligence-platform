from src.processing.text_chunker import TextChunker

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

chunker = TextChunker(chunk_size=5, overlap=2)

chunks = chunker.chunk(text)

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}: {chunk}")