from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA

from config.setings import LLM_MODEL

def build_qa_chain(retriever):
    """
    Returns a RetrievalQA chain using the Mistral model via Ollama.
    """
    llm = OllamaLLM(model=LLM_MODEL)
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",  # simplest method: stuff all docs into prompt
        return_source_documents=True  # optional: return sources for debug
    )
    return chain
