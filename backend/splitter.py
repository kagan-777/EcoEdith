def split_documents(documents):
    """
    Split documents into smaller chunks.
    """

    try:
        from langchain_text_splitters import RecursiveCharacterTextSplitter
    except ImportError as exc:
        raise ImportError(
            "The langchain-text-splitters package is required for backend.splitter. "
            "Install it with pip install langchain-text-splitters"
        ) from exc

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    return chunks