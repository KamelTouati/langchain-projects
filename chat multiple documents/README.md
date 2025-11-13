# Chat Multiple Documents (Gemini + FAISS + Streamlit)

A Streamlit app to chat over multiple PDF documents. It builds a local FAISS index of PDF text using Google Generative AI embeddings and answers questions with Gemini (`gemini-pro`).

## Overview

- Upload one or more PDFs and process them into chunks
- Create a local FAISS vector index with `GoogleGenerativeAIEmbeddings`
- Ask questions; relevant chunks are retrieved and answered by `gemini-pro`
- UI built with `streamlit` and environment managed with `python-dotenv`

## Requirements

- Python 3.9+
- A valid `GOOGLE_API_KEY` for Google Generative AI

## Installation

```bash
# From repo root
cd "chat multiple documents"

# (Optional) create and activate a virtual environment
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in `chat multiple documents/` and add your key:

```
GOOGLE_API_KEY=YOUR_KEY_HERE
```

## Run the App

```bash
streamlit run chatpdf1.py
```

The app launches a local server in your browser.

## Usage

1) In the sidebar, upload one or more PDFs and click `Submit & Process`
2) Wait for processing to complete; a local `faiss_index/` directory is created
3) Enter a question in the main input field
4) The app retrieves relevant chunks from FAISS and answers using Gemini

## Configuration

- API key loading: `langchain-projects\chat multiple documents\chatpdf1.py:13-15`
- Text chunking: `RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)`: `langchain-projects\chat multiple documents\chatpdf1.py:33-35`
- Embeddings model: `models/embedding-001` used in FAISS store: `langchain-projects\chat multiple documents\chatpdf1.py:39-41,66-69`
- QA model: `gemini-pro` with temperature `0.3`: `langchain-projects\chat multiple documents\chatpdf1.py:55-59`
- Prompt template ensures grounded answers: `langchain-projects\chat multiple documents\chatpdf1.py:46-53`

## Project Structure

```
chat multiple documents/
├─ chatpdf1.py
└─ requirements.txt
```

FAISS index is saved to `faiss_index/` in the working directory after processing.

## Troubleshooting

- Invalid or missing API key: verify `.env` contains `GOOGLE_API_KEY` and your shell reads it.
- FAISS index not found: click `Submit & Process` after uploading PDFs to build `faiss_index/` before asking questions.
- Version issues loading FAISS: ensure `faiss-cpu` and `langchain` versions are compatible. Recreate the index if needed.
- Empty answers: confirm PDFs contain extractable text; scanned PDFs may need OCR.

## Dependencies

From `requirements.txt`:

- `streamlit`, `google-generativeai`, `python-dotenv`, `langchain`, `PyPDF2`, `faiss-cpu`, `langchain_google_genai`
- Optional/unused in core flow: `chromadb`

## License

Use Google Generative AI according to its terms. Ensure you have rights to the PDFs you process.