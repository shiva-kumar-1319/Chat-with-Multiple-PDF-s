"""PDF ingestion and chunking services."""

from collections.abc import Iterable

from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
from PyPDF2 import PdfReader

from idqs.config import Settings


def extract_pdf_pages(pdf_files: Iterable[object]) -> tuple[list[Document], list[str]]:
    """Extract non-empty pages and retain source/page provenance."""
    documents: list[Document] = []
    errors: list[str] = []
    for uploaded_file in pdf_files:
        filename = getattr(uploaded_file, "name", "unnamed.pdf")
        try:
            reader = PdfReader(uploaded_file)
            for page_number, page in enumerate(reader.pages, start=1):
                text = page.extract_text() or ""
                if text.strip():
                    documents.append(Document(page_content=text, metadata={"source": filename, "page": page_number}))
        except Exception as error:
            errors.append(f"{filename}: {error}")
    return documents, errors


def split_documents(documents: list[Document], settings: Settings) -> list[Document]:
    """Create overlapping chunks without losing original page metadata."""
    splitter = CharacterTextSplitter(separator="\n", chunk_size=settings.chunk_size,
                                    chunk_overlap=settings.chunk_overlap, length_function=len)
    return splitter.split_documents(documents)
