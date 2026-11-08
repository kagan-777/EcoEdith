import shutil
import os


def clear_chroma_db():
    """
    Delete the existing ChromaDB before creating a new one.
    """

    chroma_path = "chroma_db"

    if os.path.exists(chroma_path):
        shutil.rmtree(chroma_path)

    os.makedirs(chroma_path, exist_ok=True)