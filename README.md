 
````markdown
# 📚 Intelligent Document Query System (IDQS)

### Chat with Multiple PDFs using Retrieval-Augmented Generation

An AI-powered document intelligence system that allows users to upload multiple PDF documents, ask natural-language questions, maintain conversational context, and generate document-grounded responses using a Retrieval-Augmented Generation (RAG) pipeline.

---

## 🚀 Features

- 📄 Upload and process multiple PDF documents
- 🔎 Semantic search across uploaded documents
- 🤖 Retrieval-Augmented Generation (RAG)
- 💬 Context-aware conversational Q&A
- 📚 Query up to 5 PDFs simultaneously
- 📝 Multi-document summarization
- ⚡ Interactive Streamlit interface
- 🧠 HuggingFace embeddings
- 🗂️ FAISS vector similarity search
- 🏠 Local LLM inference
- 💾 Conversation memory
- 🔧 Modular document processing and retrieval pipeline
- 🚫 No paid external LLM API required

---

# 🏗️ System Architecture

The application follows a complete:

**Document Ingestion → Chunking → Embedding → Indexing → Retrieval → Generation**

architecture.

```text
                         ┌─────────────────────────┐
                         │          USER           │
                         │                         │
                         │  Upload PDFs            │
                         │  Ask Questions          │
                         │  Follow-up Questions    │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │       STREAMLIT UI      │
                         │                         │
                         │  File Upload            │
                         │  Chat Interface         │
                         │  Conversation History   │
                         └────────────┬────────────┘
                                      │
                                      ▼
                    ┌──────────────────────────────────┐
                    │       DOCUMENT INGESTION         │
                    │                                  │
                    │  PDF Loading                     │
                    │  Text Extraction                 │
                    │  Document Preprocessing          │
                    └────────────────┬─────────────────┘
                                     │
                                     ▼
                    ┌──────────────────────────────────┐
                    │          TEXT CHUNKING             │
                    │                                  │
                    │     CharacterTextSplitter        │
                    │                                  │
                    │  Large Documents → Chunks        │
                    └────────────────┬─────────────────┘
                                     │
                                     ▼
                    ┌──────────────────────────────────┐
                    │      HUGGINGFACE EMBEDDINGS       │
                    │                                  │
                    │   Text Chunk → Vector            │
                    │                                  │
                    │ [0.12, -0.34, 0.87, ...]         │
                    └────────────────┬─────────────────┘
                                     │
                                     ▼
                    ┌──────────────────────────────────┐
                    │          FAISS VECTOR STORE       │
                    │                                  │
                    │   Store Embeddings               │
                    │   Similarity Search              │
                    └────────────────┬─────────────────┘
                                     │
                                     │
                    ┌────────────────┴─────────────────┐
                    │                                  │
                    │         USER QUESTION            │
                    │                                  │
                    └────────────────┬─────────────────┘
                                     │
                                     ▼
                    ┌──────────────────────────────────┐
                    │        QUERY EMBEDDING            │
                    │                                  │
                    │      Question → Vector           │
                    └────────────────┬─────────────────┘
                                     │
                                     ▼
                    ┌──────────────────────────────────┐
                    │       FAISS SIMILARITY SEARCH     │
                    │                                  │
                    │   Retrieve Relevant Chunks       │
                    └────────────────┬─────────────────┘
                                     │
                                     ▼
                    ┌──────────────────────────────────┐
                    │        RETRIEVED CONTEXT          │
                    │                                  │
                    │   Relevant PDF Information       │
                    └────────────────┬─────────────────┘
                                     │
                                     ▼
                    ┌──────────────────────────────────┐
                    │         LANGCHAIN RAG             │
                    │                                  │
                    │ Question + Context + History    │
                    └────────────────┬─────────────────┘
                                     │
                                     ▼
                    ┌──────────────────────────────────┐
                    │           LOCAL LLM               │
                    │                                  │
                    │        flan-t5-base              │
                    │                                  │
                    │       Generate Answer            │
                    └────────────────┬─────────────────┘
                                     │
                                     ▼
                         ┌─────────────────────────┐
                         │      FINAL RESPONSE     │
                         │                         │
                         │  Context-aware Answer   │
                         └─────────────────────────┘
````

---

# 🔄 RAG Pipeline

The complete RAG workflow is:

```text
PDF Documents
      │
      ▼
Text Extraction
      │
      ▼
Text Chunking
      │
      ▼
HuggingFace Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Similarity Search
      │
      ▼
Relevant Document Chunks
      │
      ▼
LangChain Retrieval Chain
      │
      ▼
Local LLM
      │
      ▼
Generated Response
```

---

# 🧠 How the System Works

## 1. Upload PDF Documents

Users upload multiple PDF files through the Streamlit interface.

```text
PDF 1 ─┐
PDF 2 ─┤
PDF 3 ─┼──→ Document Processing Pipeline
PDF 4 ─┤
PDF 5 ─┘
```

The application processes the documents and prepares them for semantic retrieval.

---

## 2. Extract Text

Text is extracted from the uploaded PDF documents.

The extracted content is converted into documents that can be processed by LangChain.

Each document can contain:

* Text content
* Source information
* Page metadata
* Document metadata

---

## 3. Split Documents into Chunks

Large documents are divided into smaller chunks using a `CharacterTextSplitter` strategy.

```text
Large PDF
    │
    ├── Chunk 1
    ├── Chunk 2
    ├── Chunk 3
    ├── Chunk 4
    └── Chunk N
```

Chunking allows the retrieval system to search smaller and more meaningful pieces of information instead of processing an entire PDF at once.

---

## 4. Generate Embeddings

Each document chunk is converted into a numerical vector using HuggingFace embeddings.

```text
Text Chunk
     │
     ▼
Embedding Model
     │
     ▼
Vector Representation
     │
     ▼
[0.21, -0.45, 0.78, ...]
```

The vector represents the semantic meaning of the text.

---

## 5. Build FAISS Vector Index

The generated embeddings are stored inside a FAISS vector store.

FAISS enables efficient similarity-based retrieval.

```text
Document Chunks
      │
      ▼
Embeddings
      │
      ▼
FAISS Index
      │
      ▼
Similarity Search
```

---

## 6. User Asks a Question

Example:

```text
"What is the main conclusion of this research paper?"
```

The question is converted into an embedding using the same embedding process.

---

## 7. Retrieve Relevant Context

The question embedding is compared against document embeddings.

```text
User Question
      │
      ▼
Question Embedding
      │
      ▼
FAISS Similarity Search
      │
      ▼
Top Relevant Chunks
```

The most relevant document chunks are selected as context.

---

## 8. LangChain Retrieval

LangChain connects the retrieval process with the language model.

The final input contains:

```text
User Question
       +
Retrieved Document Context
       +
Conversation History
```

---

## 9. Generate Final Response

The local language model generates the final answer using the retrieved document context.

```text
Question
    +
Relevant Context
    +
Conversation History
          │
          ▼
       Local LLM
          │
          ▼
    Final Response
```

This allows the application to answer questions based on the uploaded documents rather than relying only on general model knowledge.

---

# 💬 Conversational Q&A

The application supports contextual follow-up questions.

Example:

```text
User:
What is the main objective of this paper?

AI:
The main objective of the paper is...

User:
What methodology did they use?

AI:
The methodology described in the paper...
```

Conversation memory allows the system to understand follow-up questions based on previous interactions.

---

# 📚 Multi-PDF Querying

One of the major capabilities of IDQS is querying multiple documents within the same session.

```text
Research Paper A
Research Paper B
Research Paper C
Research Paper D
Research Paper E
        │
        ▼
     IDQS RAG
        │
        ▼
"What are the common findings?"
        │
        ▼
Cross-document Answer
```

This is useful when comparing:

* Research papers
* Technical documents
* Academic notes
* Reports
* Study material
* Business documents
* Documentation

---

# 📝 Document Summarization

The system also supports document summarization.

Instead of manually reading multiple long documents:

```text
Multiple PDFs
      │
      ▼
Document Processing
      │
      ▼
Relevant Content
      │
      ▼
Summarization
      │
      ▼
Key Insights
```

Users can quickly extract important information from large documents.

---

# 🛠️ Tech Stack

| Category             | Technology               |
| -------------------- | ------------------------ |
| Programming Language | Python                   |
| Frontend / UI        | Streamlit                |
| RAG Framework        | LangChain                |
| Vector Search        | FAISS                    |
| Embeddings           | HuggingFace              |
| Language Model       | flan-t5-base             |
| Document Processing  | LangChain PDF Loaders    |
| Text Splitting       | CharacterTextSplitter    |
| Conversation Memory  | ConversationBufferMemory |
| ML Framework         | PyTorch                  |
| Package Manager      | pip                      |
| Version Control      | Git / GitHub             |

---

# 💻 Environment Setup

## Prerequisites

Before running the project, install:

* Python 3.9+
* Git
* pip
* Virtual Environment
* Minimum 8 GB RAM recommended for local model inference

---

## Check Python

```bash
python --version
```

Example:

```text
Python 3.10.x
```

---

## Check pip

```bash
pip --version
```

---

## Check Git

```bash
git --version
```

---

# 📥 Installation

## Step 1 — Clone the Repository

```bash
git clone https://github.com/shiva-kumar-1319/Chat-with-Multiple-PDFs.git
```

Move into the project directory:

```bash
cd Chat-with-Multiple-PDFs
```

---

# 🐍 Step 2 — Create Virtual Environment

A virtual environment keeps project dependencies isolated from the system Python installation.

## Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

After activation, your terminal should show:

```text
(venv)
```

---

## Linux / macOS

Create environment:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# 📦 Step 3 — Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# 📚 Step 4 — Install Project Dependencies

If the repository contains `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Manual Installation

If `requirements.txt` is not available, install the core dependencies:

```bash
pip install streamlit
pip install langchain
pip install langchain-community
pip install faiss-cpu
pip install transformers
pip install sentence-transformers
pip install pypdf
pip install torch
```

---

# ⚙️ Environment Configuration

If environment variables are required, create a `.env` file in the project root.

```text
Chat-with-Multiple-PDFs/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── ...
```

Example:

```env
MODEL_NAME=google/flan-t5-base
```

### Important

Do not commit API keys, passwords, tokens, or other secrets to GitHub.

Add the following to `.gitignore`:

```gitignore
venv/
.env
__pycache__/
*.pyc
```

---

# ▶️ Run the Application

After activating the virtual environment:

```bash
streamlit run app.py
```

You should see:

```text
Local URL: http://localhost:8501
```

Open the URL in your browser.

---

# 🖥️ Application Workflow

```text
1. Start Streamlit
        ↓
2. Upload PDFs
        ↓
3. Extract PDF text
        ↓
4. Split text into chunks
        ↓
5. Generate embeddings
        ↓
6. Create FAISS index
        ↓
7. Ask a question
        ↓
8. Retrieve relevant chunks
        ↓
9. Pass context to LLM
        ↓
10. Generate response
        ↓
11. Continue conversation
```

---

# 📂 Project Structure

```text
Chat-with-Multiple-PDFs/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── sample_pdfs/
│
├── utils/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── retrieval.py
│
└── assets/
    └── screenshots/
```

> Update the structure above if your actual repository uses different filenames or folders.

---

# 🧪 Testing & Validation

The system was validated using approximately 20–30 test queries across multiple document types.

Testing focused on:

```text
✓ Basic factual questions
✓ Semantic questions
✓ Multi-PDF questions
✓ Follow-up questions
✓ Conversation context
✓ Document summarization
✓ Different document structures
✓ Retrieval relevance
```

---

# 📊 Example Workflow

### Uploaded Documents

```text
paper_1.pdf
paper_2.pdf
paper_3.pdf
```

### User Question

```text
What are the common findings across these papers?
```

### Internal Processing

```text
Question
   │
   ▼
Question Embedding
   │
   ▼
FAISS Similarity Search
   │
   ▼
Relevant Chunks
   │
   ├── paper_1.pdf
   ├── paper_2.pdf
   └── paper_3.pdf
   │
   ▼
LangChain Retrieval Chain
   │
   ▼
Local LLM
   │
   ▼
Final Answer
```

---

# ⚡ Engineering Highlights

### Multi-Document Retrieval

Supports querying information across multiple PDF documents within a single session.

### Semantic Search

Uses dense vector embeddings to retrieve conceptually relevant information rather than relying only on exact keyword matching.

### RAG Architecture

Retrieves relevant document context before generating an answer.

### Conversational Memory

Maintains previous conversation context to support follow-up questions.

### Local Model Inference

Runs inference locally, reducing dependency on paid external LLM APIs.

### Modular Architecture

The system separates:

```text
Document Loading
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
Vector Indexing
      ↓
Similarity Retrieval
      ↓
Context Construction
      ↓
LLM Generation
```

---

# 🔍 Why RAG?

A traditional language model may not know the contents of a user's private PDF.

RAG solves this by retrieving relevant information directly from the uploaded documents.

### Traditional LLM

```text
Question
   ↓
LLM
   ↓
General Knowledge
   ↓
Answer
```

### IDQS RAG

```text
Question
   ↓
Retriever
   ↓
Relevant PDF Context
   ↓
LLM
   ↓
Document-Grounded Answer
```

---

# 🎯 Use Cases

IDQS can be used for:

* 📚 Academic research
* 📑 Research paper analysis
* 🧑‍🎓 Study material
* 📖 Books and notes
* 💼 Business reports
* 📊 Technical documentation
* 📝 Project documentation
* 🔬 Scientific literature

---

# 🧠 Key Technical Concepts Demonstrated

```text
Python
   ↓
PDF Processing
   ↓
NLP
   ↓
Text Chunking
   ↓
Embeddings
   ↓
Vector Search
   ↓
FAISS
   ↓
RAG
   ↓
LangChain
   ↓
LLM
   ↓
Conversational AI
```

---

# 🚀 Future Improvements

* [ ] Page-level source citations
* [ ] Hybrid keyword + vector search
* [ ] Retrieval reranking
* [ ] OCR support for scanned PDFs
* [ ] Persistent vector database
* [ ] Streaming LLM responses
* [ ] Authentication and user accounts
* [ ] Cloud deployment
* [ ] Advanced document comparison
* [ ] Automated retrieval evaluation
* [ ] DOCX and TXT support
* [ ] Larger instruction-tuned local models
* [ ] Better hallucination detection
* [ ] Retrieval evaluation metrics

---

# 📌 Why This Project Is Different

The project demonstrates more than simply connecting an LLM to a PDF.

It implements an end-to-end document intelligence pipeline:

```text
                DOCUMENT INTELLIGENCE SYSTEM

                    PDF Documents
                         │
                         ▼
                 Document Processing
                         │
                         ▼
                    Chunking
                         │
                         ▼
                    Embeddings
                         │
                         ▼
                   FAISS Index
                         │
                         ▼
                   Retrieval
                         │
                         ▼
                 Context Building
                         │
                         ▼
                    LangChain
                         │
                         ▼
                     Local LLM
                         │
                         ▼
                 Contextual Answer
```

The project therefore demonstrates practical experience with:

* Generative AI
* Retrieval-Augmented Generation
* Natural Language Processing
* Vector databases
* Semantic search
* LLM integration
* Document intelligence
* Conversational AI
* Python application development

---

# 👨‍💻 Author

## Shiva Kumar

AI & Machine Learning Engineering Student

Interested in:

```text
Artificial Intelligence
Machine Learning
Generative AI
RAG Systems
LLM Applications
Backend Engineering
Data Structures & Algorithms
Scalable Software Systems
```

---

# 🔗 Connect With Me

**GitHub:**
[https://github.com/shiva-kumar-1319](https://github.com/shiva-kumar-1319)

**LinkedIn:**
[https://www.linkedin.com/in/shiva-kumar-kavali-b200342a7/](https://www.linkedin.com/in/shiva-kumar-kavali-b200342a7/)

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository
🍴 Fork the repository
🐛 Report issues
💡 Suggest improvements

---

# 📜 License

This project is intended for educational and research purposes.

```
```
