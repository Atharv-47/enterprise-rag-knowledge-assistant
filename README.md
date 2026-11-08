# Enterprise RAG Knowledge Assistant

An AI-powered document question-answering system that uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from PDF documents and generate context-grounded answers with source references.

**Project Status:** In Development

## Overview

Enterprise RAG Knowledge Assistant is designed to help users query information stored in PDF documents using natural language.

Instead of relying entirely on an LLM's internal knowledge, the system retrieves relevant document passages, reranks them based on query relevance, and supplies them as context to a Gemini model.

The system also includes an abstention mechanism to reject questions when the retrieved passages appear insufficiently relevant.

## Architecture

```text
             PDF Documents
                   |
                   v
          PDF Text Extraction
               (PyMuPDF)
                   |
                   v
             Text Chunking
       (LangChain Text Splitters)
                   |
                   v
              Embeddings
        (Sentence Transformers)
                   |
                   v
             ChromaDB
          Vector Database
                   |
                   v
             User Query
                   |
                   v
             Vector Search
                   |
                   v
             MMR Selection
                   |
                   v
          Cross-Encoder Reranking
                   |
                   v
          Relevance / Abstention
                   |
                   v
           Retrieved Context
                   |
                   v
          Gemini Answer Generation
                   |
                   v
          Answer with Source References
```

## Implemented Features

- **PDF Text Extraction:** Extracts text from PDF documents using PyMuPDF while preserving page numbers.
- **Text Chunking:** Splits extracted text into manageable chunks using LangChain's RecursiveCharacterTextSplitter.
- **Local Embeddings:** Generates document and query embeddings using Sentence Transformers (`all-MiniLM-L6-v2`).
- **Vector Database:** Stores document chunks, embeddings, and metadata in persistent ChromaDB storage.
- **Semantic Retrieval:** Retrieves candidate passages based on query similarity.
- **Maximum Marginal Relevance (MMR):** Selects diverse passages to reduce redundant retrieval.
- **Cross-Encoder Reranking:** Reorders retrieved passages using `cross-encoder/ms-marco-MiniLM-L-6-v2`.
- **Abstention Mechanism:** Rejects questions when the highest reranking score is at or below a provisional threshold of zero.
- **LLM Integration:** Uses Google's Gemini API to generate answers from retrieved document context.
- **Source Metadata:** Preserves document filenames and page numbers and generates unique source references.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| PDF Processing | PyMuPDF |
| Text Chunking | LangChain Text Splitters |
| Embeddings | Sentence Transformers |
| Vector Database | ChromaDB |
| Retrieval Optimization | MMR |
| Reranking | Cross-Encoder |
| Answer Generation | Google Gemini API |
| Environment Variables | python-dotenv |

## Project Structure

```text
enterprise-rag-knowledge-assistant/
│
├── data/
│   ├── sample_docs/
│   └── chroma_db/             # Generated locally
│
├── src/
│   ├── document_loader.py
│   ├── text_chunker.py
│   ├── vectors_store.py
│   └── llm.py
│
├── .env                       # API key (not committed)
├── .gitignore
├── requirements.txt
├── README.md
│
├── testload.py
├── test_embeding.py
├── test_gemni.py
├── test_vectorsstore.py
├── test_retrieval.py
├── test_reranker.py
└── test_rag.py
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Atharv-47/enterprise-rag-knowledge-assistant.git
cd enterprise-rag-knowledge-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Obtain an API key through Google AI Studio.

**Important:** Never commit your `.env` file or expose your API key publicly.

### 5. Add a PDF document

Place a text-based PDF inside:

```text
data/sample_docs/
```

Update the PDF path in `test_vectorsstore.py` if necessary.

### 6. Process and store the document

```bash
python test_vectorsstore.py
```

This extracts the document text, creates chunks, generates embeddings, and stores them in ChromaDB.

### 7. Test retrieval

```bash
python test_retrieval.py
```

### 8. Test reranking and abstention

```bash
python test_reranker.py
```

This test does not require a Gemini API call.

### 9. Run the complete RAG pipeline

```bash
python test_rag.py
```

This retrieves relevant context and sends it to Gemini for answer generation.

## Current Limitations

- Current PDF processing extracts text; scanned image-based PDFs and OCR are not yet supported.
- Multiple-document ingestion and document management are still under development.
- The abstention threshold is experimental and has only been tested on a small set of questions.
- Sentence-level citation accuracy and generated citation formatting still require verification.
- Gemini API usage is subject to model and project quotas.
- A user-facing Streamlit interface has not yet been implemented.

## Future Improvements

1. Multiple PDF ingestion and document management.
2. Semantic caching to reduce repeated processing and API calls.
3. Prompt-injection guardrails for untrusted document content.
4. Streamlit interface for uploading PDFs and asking questions.
5. More comprehensive retrieval, reranking, abstention, and citation evaluation.
6. Architecture documentation and final testing.

## Project Goal

The goal is to develop a practical document-grounded question-answering system that combines semantic retrieval, reranking, relevance filtering, and LLM-based response generation.

---

