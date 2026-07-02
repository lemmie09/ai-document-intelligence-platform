from src.embeddings.embedding_model import EmbeddingModel

model = EmbeddingModel()

vector = model.embed("Machine Learning is amazing")

print(type(vector))
print(len(vector))
print(vector[:10])