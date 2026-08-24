"""Streamlit entry point for the Intelligent Document Query System."""

from html import escape

import streamlit as st
from dotenv import load_dotenv

from htmlTemplates import bot_template, css, user_template
from idqs.config import Settings
from idqs.documents import extract_pdf_pages, split_documents
from idqs.rag import build_conversation_chain, build_vectorstore


def initialise_session() -> None:
    st.session_state.setdefault("conversation", None)
    st.session_state.setdefault("chat_history", [])


def render_history() -> None:
    for index, message in enumerate(st.session_state.chat_history):
        template = user_template if index % 2 == 0 else bot_template
        safe_message = escape(message.content).replace("\n", "<br>")
        st.write(template.replace("{{MSG}}", safe_message), unsafe_allow_html=True)


def answer_question(question: str) -> None:
    chain = st.session_state.conversation
    if chain is None:
        st.warning("Upload and process at least one readable PDF before asking a question.")
        return
    with st.spinner("Finding relevant passages and preparing an answer..."):
        response = chain.invoke({"question": question})
    st.session_state.chat_history = response["chat_history"]


def process_uploads(pdf_files: list[object], settings: Settings) -> None:
    pages, errors = extract_pdf_pages(pdf_files)
    for error in errors:
        st.warning(f"Could not read {error}")
    if not pages:
        st.error("No extractable text was found in the uploaded PDFs.")
        return
    chunks = split_documents(pages, settings)
    vectorstore = build_vectorstore(chunks, settings)
    st.session_state.conversation = build_conversation_chain(vectorstore, settings)
    st.session_state.chat_history = []
    st.success(f"Indexed {len(chunks)} chunks from {len(pages)} readable pages.")


def main() -> None:
    load_dotenv()
    settings = Settings()
    st.set_page_config(page_title="IDQS | Document Q&A", page_icon="📚")
    st.write(css, unsafe_allow_html=True)
    initialise_session()
    st.header("Intelligent Document Query System 📚")
    st.caption("Upload PDFs, process them once, then ask grounded follow-up questions.")
    question = st.text_input("Ask a question about your documents")
    if question:
        answer_question(question)
    render_history()
    with st.sidebar:
        st.subheader("Document collection")
        pdf_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)
        if st.button("Process documents", type="primary"):
            if not pdf_files:
                st.warning("Choose at least one PDF first.")
            else:
                with st.spinner("Extracting pages, chunking text, and building the index..."):
                    try:
                        process_uploads(pdf_files, settings)
                    except ValueError as error:
                        st.error(str(error))
                    except Exception as error:
                        st.error(f"Processing failed: {error}")


if __name__ == "__main__":
    main()
