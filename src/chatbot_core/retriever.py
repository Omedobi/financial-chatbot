from llama_index.core import VectorStoreIndex
from llama_index.core.query_engine import RetrieverQueryEngine

class Retriever:
    def __init__(self, nodes, embed_model):
        self.index = VectorStoreIndex(nodes, embed_model=embed_model)

    def get_engine(self, llm, top_k=5):
        return RetrieverQueryEngine.from_args(self.index.as_retriever(similarity_top_k=top_k), llm=llm)

