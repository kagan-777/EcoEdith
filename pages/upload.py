import streamlit as st
import os

from backend.loader import load_pdf
from backend.splitter import split_documents
from backend.vectorstore import create_vector_store
from backend.utils import clear_chroma_db

st.title("📄 Upload Learning Materials")
st.write("Upload your study materials below.")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:

    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✅ {uploaded_file.name} uploaded successfully!")

    # Clear old ChromaDB
    #clear_chroma_db()

    # Load document
    documents = load_pdf(file_path)

    # Split into chunks
    chunks = split_documents(documents)

    st.success(f"✅ Total Chunks Created: {len(chunks)}")

    # Store in ChromaDB
    create_vector_store(chunks)

    st.success("✅ Document stored successfully in ChromaDB!")

    # Show chunks
    st.subheader("📄 Chunks")

    for i, chunk in enumerate(chunks):
        with st.expander(f"Chunk {i+1}"):

            page = chunk.metadata.get("page", "Unknown")

            st.write(f"📄 Page: {page + 1}")

            st.write(chunk.page_content)