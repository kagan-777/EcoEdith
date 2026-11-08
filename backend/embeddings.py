def get_embedding_model():
    try:
        from langchain_huggingface import HuggingFaceEmbeddings
    except ImportError as exc:
        raise ImportError(
            "The langchain-huggingface package is required for backend.embeddings. "
            "Install it with pip install langchain-huggingface"
        ) from exc

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model