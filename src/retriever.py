import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def load_retriever(vectorstore_path: str):
    """
    Loads a FAISS vectorstore from disk and returns a retriever.
    """
    if not os.path.exists(vectorstore_path):
        raise FileNotFoundError(f"Vectorstore path '{vectorstore_path}' not found.")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(vectorstore_path, embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever()
    return retriever
