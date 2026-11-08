import os
import zipfile
import xml.etree.ElementTree as ET
from types import SimpleNamespace
import streamlit as st
from backend.user_db import save_user_full_text


def _make_document(page_content, page=0):
    return SimpleNamespace(
        page_content=page_content,
        metadata={"page": page}
    )


def _save_full_text(documents, username=None):
    """Save full text to user's data directory."""
    if username is None:
        username = st.session_state.get("username", "default")
    
    full_text = "\n\n".join(
        doc.page_content for doc in documents
    )

    save_user_full_text(username, full_text)
    print(f"✅ Full file text saved for user {username}")


def _load_text_file(file_path):
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    return [_make_document(content)]


def _load_docx_file(file_path):
    try:
        import docx
    except ImportError:
        docx = None

    if docx is not None:
        document = docx.Document(file_path)
        content = "\n\n".join(
            paragraph.text for paragraph in document.paragraphs
        )
        return [_make_document(content)]

    with zipfile.ZipFile(file_path) as zip_file:
        xml_content = zip_file.read("word/document.xml")
        root = ET.fromstring(xml_content)
        namespaces = {
            "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
        }

        paragraphs = []
        for paragraph in root.findall(".//w:p", namespaces):
            texts = [
                node.text or ""
                for node in paragraph.findall(".//w:t", namespaces)
            ]
            if texts:
                paragraphs.append("".join(texts))

        content = "\n\n".join(paragraphs)
    return [_make_document(content)]


def _load_pdf_file(file_path):
    try:
        from langchain_community.document_loaders import PyPDFLoader
    except ImportError as exc:
        raise ImportError(
            "The langchain-community package is required to load PDF documents. "
            "Install it with pip install langchain-community"
        ) from exc

    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents


def load_pdf(file_path, username=None):
    """Load PDF, TXT, or DOCX file and save to user's data directory."""
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        documents = _load_pdf_file(file_path)
    elif ext == ".txt":
        documents = _load_text_file(file_path)
    elif ext == ".docx":
        documents = _load_docx_file(file_path)
    else:
        raise ValueError(
            f"Unsupported file type: {ext}. Supported types are .pdf, .txt, .docx."
        )

    if not documents:
        raise ValueError("No content could be extracted from the uploaded file.")

    _save_full_text(documents, username)
    return documents
