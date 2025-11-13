# LangChain Basic QA (OpenAI + DocArray + Streamlit)

A Streamlit app that answers questions over a single PDF document using OpenAI embeddings and a simple in-memory vector store. Great for short documents, email threads, and contracts.

## Overview

- Upload a PDF and embed its pages with `OpenAIEmbeddings`
- Store vectors in `DocArrayInMemorySearch`
- Query via `RetrievalQA` using `ChatOpenAI`
- Clean Streamlit UI with form-based execution

## Requirements

- Python 3.9+
- OpenAI API key (`OPENAI_API_KEY`) — entered in the app UI

## Installation

```bash
# From repo root
cd "langchain basic qa"

# (Optional) create and activate a virtual environment
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```

The app launches a local server and opens in your browser.

## Usage

- Paste your OpenAI API key in the `OpenAI Api Key` field
- Upload a PDF document
- Enter a question and click `🚀 Run Query`
- The app retrieves relevant content and returns an answer

Sample queries:

- Create a very short summary of the document
- List highlights in a bullet list
- Check mentions of a specific name
- Analyze tone or dissatisfaction indicators

## Configuration

- Page config and headers: `langchain-projects\langchain basic qa\app.py:10-20`
- Security notice: `langchain-projects\langchain basic qa\app.py:32-34`
- API key and file upload: `langchain-projects\langchain basic qa\app.py:35-38`
- Form, query input, and submit: `langchain-projects\langchain basic qa\app.py:39-52`
- PDF load via `PyPDFLoader` and page split: `langchain-projects\langchain basic qa\app.py:63-67`
- Embeddings and vector store: `langchain-projects\langchain basic qa\app.py:68-71`
- LLM and `RetrievalQA` chain: `langchain-projects\langchain basic qa\app.py:72-76`
- Result display and cleanup: `langchain-projects\langchain basic qa\app.py:78-81`
- Known limits section: `langchain-projects\langchain basic qa\app.py:94-104`
- Theme and privacy: `langchain-projects\langchain basic qa\.streamlit\config.toml:1-5`

## Project Structure

```
langchain basic qa/
├─ app.py
├─ requirements.txt
├─ .gitignore
└─ .streamlit/
   └─ config.toml
```

## Troubleshooting

- Invalid API key or auth errors: ensure your key is active and pasted correctly
- Empty or poor answers: short/clean PDFs work best; scanned PDFs may need OCR
- Large document limits: this in-memory approach is suited to small/medium documents
- Consider a dedicated vector DB and text splitting for larger corpora

## Dependencies

From `requirements.txt`:

- `docarray`, `langchain`, `langchain-community`, `openai`, `pypdf`, `streamlit`, `tiktoken`

## License

Use OpenAI APIs according to their terms. Ensure you have rights to the PDFs you process and comply with applicable policies.