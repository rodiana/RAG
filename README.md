# 🎬 YouTube RAG Assistant

An app that lets you ask questions about any YouTube video using **Retrieval-Augmented Generation (RAG)**. Built entirely with **open-source technologies**, it runs locally—no cloud APIs, no subscriptions, and no hidden components.

This project was designed as a portfolio showcase to demonstrate practical usage of:
- **LangChain** for orchestration and text splitting
- **Hugging Face Sentence Transformers** for embeddings
- **FAISS** for vector storage and retrieval
- **Ollama** running **Mistral** as a local LLM
- **Streamlit** as a lightweight and interactive UI

---

## 🧠 Key Concepts

| Concept | Description |
|--------|-------------|
| RAG (Retrieval-Augmented Generation) | Combines external knowledge (YouTube transcript) with LLM generation |
| Text Splitting | Breaks the transcript into overlapping chunks using LangChain to improve embedding and retrieval accuracy. |
| Embedding | Converts text into vectors to enable semantic search |
| Vector Store | Stores and retrieves chunks relevant to your query |
| Local LLM | Uses `mistral` model via `ollama`, no internet or API key needed |

---

## 🛠 Tech Stack

- **LangChain** – chaining logic, text splitting
- **Hugging Face (all-MiniLM-L6-v2)** – fast, free embeddings
- **FAISS** – vector similarity search
- **Ollama** – runs `mistral` locally
- **YouTube Transcript API** – fetches transcript from public videos
- **Streamlit** – interactive browser UI
- **Python 3.10+**

> 🚫 100% Open Source — no OpenAI keys, no paywalls, no trackers

---

## 📁 Project Structure
```
youtube-rag-assistant/
├── main.py # CLI entry point (for testing)
├── ui/app.py # Streamlit UI
├── config/settings.py # Global settings (chunk size, model names)
├── data/ # Stores transcripts and FAISS vectorstores
│ ├── transcripts/
│ └── vectorstore/
├── src/ # Core logic modules
│ ├── youtube_loader.py # Transcript fetcher
│ ├── text_splitter.py # Chunking logic
│ ├── embedder.py # Embedding + FAISS builder
│ ├── retriever.py # Loads retriever
│ └── qa_chain.py # LLM + RAG chain setup
```
---

## ▶️ How to Run
```bash
🧱 1. Clone the repository
git clone https://github.com/your-username/youtube-rag-assistant.git
cd youtube-rag-assistant

🐍 2. Create and activate a virtual environment
conda create -n rag python=3.10 -y
conda activate rag

📦 3. Install dependencies
pip install -r requirements.txt
Make sure ollama is installed and the mistral model is pulled:
ollama run mistral

🌐 4. Launch the app
streamlit run ui/app.py
Then open your browser at: http://localhost:8501
```

## 🧪 Example Workflow
Paste a YouTube video link (wich allows transcript)

The transcript is fetched and split into chunks

Chunks are embedded using Hugging Face model

Stored and indexed with FAISS vectorstore

Ask questions → the app retrieves relevant chunks and sends them to the Mistral LLM running locally via Ollama

## 📝 Educational Note
This codebase contains multiple print() statements intentionally left for debugging and educational purposes.
These help you see what’s happening step-by-step behind the scenes (e.g. chunk counts, vectorstore paths, retrieved chunks).

Feel free to clean or extend as needed for your own applications.