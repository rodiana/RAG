import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.youtube_loader import fetch_transcript, extract_video_id, save_transcript
from src.text_splitter import split_text
from src.embedder import create_vectorstore
from src.retriever import load_retriever
from src.qa_chain import build_qa_chain


from config.setings import CHUNK_SIZE, CHUNK_OVERLAP, TRANSCRIPT_DIR, VECTORSTORE_DIR

st.title("📺 YouTube RAG Assistant")

url = st.text_input("Paste a YouTube video URL or ID")
ask_button = st.button("Prepare Video")

if ask_button and url:
    video_id = extract_video_id(url)
    transcript = fetch_transcript(video_id)
    save_transcript(video_id, transcript, output_dir=TRANSCRIPT_DIR)
    chunks = split_text(transcript,chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)
    vectorstore_path = f"{VECTORSTORE_DIR}/{video_id}"
    create_vectorstore(chunks, save_path=vectorstore_path)
    st.success("Transcript processed and vector store created!")

    retriever = load_retriever(vectorstore_path)
    qa_chain = build_qa_chain(retriever)

    st.session_state.qa = qa_chain

if "qa" in st.session_state:
    question = st.text_input("Ask a question")
    if st.button("Submit") and question:
        response = st.session_state.qa.invoke({"query": question})
        st.markdown(f"**A:** {response['result']}")
