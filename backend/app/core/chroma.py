import os
import chromadb

CHROMA_PATH = os.getenv(
    "CHROMA_PATH",
    "chroma_db"
)

os.makedirs(
    CHROMA_PATH,
    exist_ok=True
)

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = client.get_or_create_collection(
    name="memora"
)