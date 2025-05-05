from llama_index.embeddings.huggingface import HuggingFaceEmbedding

class Embedder:
    def __init__(self, model_name="BAAI/bge-small-en-v1.5"):
        self.model = HuggingFaceEmbedding(model_name=model_name)

    def encode(self, text: str):
        return self.model.get_text_embedding(text)