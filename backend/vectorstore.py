import streamlit as st
from backend.embeddings import get_embedding_model
from backend.user_db import get_user_chroma_path


def create_vector_store(chunks, username=None):
    """Create vector store for user's documents."""
    print("Total chunks:", len(chunks))

    if username is None:
        username = st.session_state.get("username", "default")

    embedding_model = get_embedding_model()

    try:
        from langchain_chroma import Chroma
    except ImportError as exc:
        raise ImportError(
            "The langchain-chroma package is required for backend.vectorstore. "
            "Install it with pip install langchain-chroma"
        ) from exc

    # Test embedding
    test = embedding_model.embed_query("Hello world")
    print("Embedding length:", len(test))

    # Get user-specific chroma path
    chroma_path = get_user_chroma_path(username)

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=chroma_path
    )

    return vector_db