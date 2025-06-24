import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from config.setings import EMBEDDING_MODEL


def create_vectorstore(chunks: list[str], save_path: str = "data/vectorstore"):
    """
    Creates and saves a FAISS vectorstore with embedded chunks.
    """
    embedder = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectorstore = FAISS.from_texts(chunks, embedding=embedder)
    
    os.makedirs(save_path, exist_ok=True)
    vectorstore.save_local(save_path)
    print(f"Saving vectorstore to {save_path}...")
    return vectorstore
