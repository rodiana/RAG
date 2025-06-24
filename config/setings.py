# config/settings.py

# Model configs
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "mistral"

# Text splitting
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Paths
TRANSCRIPT_DIR = "data/transcripts"
VECTORSTORE_DIR = "data/vectorstore"
