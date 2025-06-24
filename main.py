import os
import sys
from src.youtube_loader import extract_video_id, fetch_transcript, save_transcript
from src.text_splitter import split_text
from src.embedder import create_vectorstore
from src.retriever import load_retriever
from src.qa_chain import build_qa_chain

from config.setings import CHUNK_SIZE, CHUNK_OVERLAP, TRANSCRIPT_DIR, VECTORSTORE_DIR


if __name__ == "__main__":
    url_or_id = input("YouTube video URL or ID: ")
    video_id = extract_video_id(url_or_id)
    # transcript_path = f"{TRANSCRIPT_DIR}/{video_id}.txt"
    vectorstore_path = f"{VECTORSTORE_DIR}/{video_id}"

    # Build vectorstore if it doesn't exist
    if not os.path.exists(vectorstore_path):
        print("Vectorstore not found. Building it now...")

        print("Fetching transcript...")
        transcript = fetch_transcript(video_id)
        save_transcript(video_id, transcript, output_dir=TRANSCRIPT_DIR)

        print("Splitting transcript...")
        chunks = split_text(transcript,chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)

        print("Creating and saving vectorstore...")
        create_vectorstore(chunks, save_path=vectorstore_path)
    else:
        print("Vectorstore already exists. Skipping rebuild.")

    # Load retriever and chain
    retriever = load_retriever(vectorstore_path)
    qa_chain = build_qa_chain(retriever)

    # Start interactive Q&A
    print("\nAsk a question about the video! (type 'exit' to quit)\n")
    while True:
        query = input("Q: ")
        if query.lower() in ["exit", "quit"]:
            break
        response = qa_chain.invoke({"query": query})
        print(f"A: {response['result']}\n")
