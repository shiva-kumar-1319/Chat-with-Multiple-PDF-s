"""Retrieval and generation chain construction."""

from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from idqs.config import Settings


def build_vectorstore(chunks: list[Document], settings: Settings) -> FAISS:
    """Embed chunks and create an in-memory FAISS similarity index."""
    embeddings = HuggingFaceEmbeddings(model_name=settings.embedding_model)
    return FAISS.from_documents(documents=chunks, embedding=embeddings)


def build_conversation_chain(vectorstore: FAISS, settings: Settings):
    """Create a chain that retrieves evidence before generating an answer."""
    if not settings.huggingface_token:
        raise ValueError("HUGGINGFACEHUB_API_TOKEN is not configured.")
    llm = HuggingFaceHub(repo_id=settings.llm_repository,
                         huggingfacehub_api_token=settings.huggingface_token,
                         model_kwargs={"temperature": 0.5, "max_length": 512})
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": settings.retriever_k}),
        memory=memory,
    )
