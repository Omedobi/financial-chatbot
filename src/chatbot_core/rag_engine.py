from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
from llama_index.core.node_parser import SentenceSplitter
import os

class RAGChatbot:
    def __init__(self, data_dir: str, api_key: str):
        os.environ["GROQ_API_KEY"] = api_key

        self.documents = SimpleDirectoryReader(data_dir).load_data()
        self.splitter = SentenceSplitter(chunk_size=512, chunk_overlap=50)
        self.nodes = self.splitter.get_nodes_from_documents(self.documents)

        self.index = VectorStoreIndex(self.nodes, embed_model=HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5"))
        self.query_engine = RetrieverQueryEngine.from_args(
            self.index.as_retriever(similarity_top_k=5),
            llm=Groq(model="llama3-70b-8192", api_key=api_key),
        )

    def query(self, question: str) -> str:
        response = self.query_engine.query(question)
        return str(response)
