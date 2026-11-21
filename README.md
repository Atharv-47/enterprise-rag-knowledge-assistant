# Enterprise RAG Knowledge Assistant

An AI-powered document question-answering system that uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from PDF documents and generate context-grounded answers with source references.

**Project Status:** In Development

## Overview

Enterprise RAG Knowledge Assistant is designed to help users retrieve and understand information from PDF documents through natural-language queries.

Rather than relying solely on an LLM's internal knowledge, the system retrieves relevant document passages using semantic search, applies Maximum Marginal Relevance (MMR) to improve retrieval diversity, and uses a Cross-Encoder to rerank the selected passages.

The retrieved content is then supplied to Google's Gemini model as context for answer generation.

The project also explores relevance-based abstention to reduce unsupported responses when retrieved information is insufficient.

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
          Embedding Generation
        (Sentence Transformers)
                   |
                   v
             ChromaDB
          Persistent Storage
                   |
                   v
              User Query
                   |
                   v
          Query Embedding
                   |
                   v
           Vector Retrieval
          (Top 30 Candidates)
                   |
                   v
          MMR-based Selection
                   |
                   v
        Cross-Encoder Reranking
                   |
                   v
        Relevance Assessment
                   |
                   v
          Context Construction
          (Source References)
                   |
                   v
        Gemini Answer Generation
                   |
                   v
       Grounded Answer with Sources
```

## Implemented Features

- **PDF Text Extraction:** Extracts text from PDF documents using PyMuPDF while retaining page-level information.
- **Text Preprocessing:** Normalizes whitespace and removes excessive blank lines before chunking.
- **Recursive Text Chunking:** Uses LangChain's RecursiveCharacterTextSplitter with configurable chunk size and overlap.
- **Local Embeddings:** Generates document and query embeddings using Sentence Transformers (`all-MiniLM-L6-v2`).
- **Persistent Vector Storage:** Stores document chunks, embeddings, and metadata in ChromaDB.
- **Semantic Retrieval:** Retrieves candidate passages based on vector similarity.
- **Maximum Marginal Relevance (MMR):** Selects diverse passages from the retrieved candidates to reduce redundancy.
- **Cross-Encoder Reranking:** Reorders selected passages using `cross-encoder/ms-marco-MiniLM-L-6-v2` based on query-passage relevance.
- **LLM Integration:** Uses Google's Gemini API to generate answers from retrieved document context.
- **Context Construction:** Combines retrieved passages and their metadata into a structured context for answer generation.
- **Source References:** Maintains document filenames and page numbers and generates source identifiers for context citations.
- **Experimental Abstention:** Evaluates reranking relevance scores to identify questions that may not be sufficiently supported by retrieved passages.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| PDF Processing | PyMuPDF |
| Text Chunking | LangChain Text Splitters |
| Embedding Model | Sentence Transformers |
| Embedding Model Name | all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| Retrieval Optimization | Maximum Marginal Relevance (MMR) |
| Reranking | Cross-Encoder |
| Reranking Model | ms-marco-MiniLM-L-6-v2 |
| Answer Generation | Google Gemini API |
| Environment Configuration | python-dotenv |

## Project Structure

```text
enterprise-rag-knowledge-assistant/
│
├── data/
│   ├── sample_docs/             # Sample PDF documents
│   └── chroma_db/               # Persistent vector storage
│
├── src/
│   ├── document_loader.py       # PDF text extraction
│   ├── text_chunker.py          # Text preprocessing and chunking
│   ├── vectors_store.py         # Embeddings, retrieval, MMR and reranking
│   └── llm.py                   # Gemini integration
│
├── .env                         # API credentials (not committed)
├── .gitignore
├── requirements.txt
├── README.md
│
├── test_vectorsstore.py         # Document ingestion and indexing
├── test_chunking.py             # Chunking tests
├── test_reranker.py             # Reranking and relevance tests
├── test_answerability.py        # Answerability experiments
└── test_rag.py                  # End-to-end RAG pipeline
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Atharv-47/enterprise-rag-knowledge-assistant.git

cd enterprise-rag-knowledge-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Obtain an API key through [Google AI Studio](https://aistudio.google.com/).

**Security:** Never commit the `.env` file or expose API credentials publicly.

### 5. Add PDF Documents

Place a text-based PDF inside:

```text
data/sample_docs/
```

Update the PDF path in `test_vectorsstore.py` if necessary.

### 6. Process and Index Documents

```bash
python test_vectorsstore.py
```

This performs the document ingestion workflow:

1. Extracts text from the PDF.
2. Splits the extracted text into chunks.
3. Generates embeddings for the chunks.
4. Stores the chunks, embeddings, and metadata in ChromaDB.

### 7. Test Retrieval

```bash
python test_retrieval.py
```

### 8. Test Reranking and Relevance

```bash
python test_reranker.py
```

This evaluates retrieved passages using the Cross-Encoder and tests relevance behaviour without requiring a Gemini API call.

### 9. Run the Complete RAG Pipeline

```bash
python test_rag.py
```

This executes retrieval, reranking, context construction, and Gemini-based answer generation.

**Note:** Gemini answer generation requires a valid API key and available API quota.

## Current Limitations

- PDF processing currently extracts text; scanned PDFs and OCR are not supported.
- Multiple-document ingestion and document management require further development and testing.
- Retrieval quality and MMR selection require more comprehensive evaluation.
- The relevance-based abstention threshold is experimental and requires calibration.
- Citation formatting is implemented through source references in the prompt, but citation accuracy requires further verification.
- Gemini API availability and usage depend on model access and project quotas.
- A user-facing Streamlit interface has not yet been implemented.

## Planned Improvements

1. **Retrieval Optimization:** Improve retrieval quality through systematic evaluation and tuning of chunking, candidate selection, and reranking.
2. **Prompt Injection Protection:** Introduce safeguards against malicious instructions in user queries and untrusted document content.
3. **Semantic Caching:** Cache responses for semantically similar queries to reduce repeated LLM calls and improve response latency.
4. **Error Handling and Logging:** Improve exception handling and introduce structured logging for document processing, retrieval, and API operations.
5. **Retrieval Evaluation:** Evaluate retrieval performance using metrics such as Precision@K, Recall@K, and Mean Reciprocal Rank (MRR).
6. **Answer Evaluation:** Assess generated answers for relevance, faithfulness, correctness, and citation accuracy.
7. **Streamlit Interface:** Build an interactive interface for PDF uploads, natural-language queries, generated answers, and source references.
8. **Deployment:** Prepare the application for reproducible setup and deployment.

## Project Goal

The objective is to build a practical, document-grounded question-answering system that combines semantic search, retrieval diversification, neural reranking, and LLM-based generation.

The project focuses on improving the relevance, reliability, and traceability of generated answers while reducing dependence on unsupported LLM responses.