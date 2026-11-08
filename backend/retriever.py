import streamlit as st
from backend.embeddings import get_embedding_model
from backend.user_db import get_user_chroma_path


def get_retriever(username=None):
    """Get retriever for user's vector database."""
    try:
        from langchain_chroma import Chroma
    except ImportError as exc:
        raise ImportError(
            "The langchain-chroma package is required for backend.retriever. "
            "Install it with pip install langchain-chroma"
        ) from exc

    if username is None:
        username = st.session_state.get("username", "default")

    embedding_model = get_embedding_model()
    
    # Get user-specific chroma path
    chroma_path = get_user_chroma_path(username)

    vector_db = Chroma(
        persist_directory=chroma_path,
        embedding_function=embedding_model
    )

    retriever = vector_db.as_retriever(
        search_kwargs={"k": 5}
    )

    return retriever