from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(text: str, chunk_size=500, chunk_overlap=50) -> list[str]:
    """
    Splits long text into smaller overlapping chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "],
    )
    print(f"Splitted transcript into {len(splitter.split_text(text))} chunks!")
    return splitter.split_text(text)
