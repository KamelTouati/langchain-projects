# Codebasics Q&A (FAISS + Instructor Embeddings + Google PaLM)

A Streamlit app that builds a local FAISS index from a CSV of FAQs and answers questions using Google PaLM. Uses `HuggingFaceInstructEmbeddings` to embed rows from `codebasics_faqs.csv` and retrieves relevant context to ground responses.

## Overview

- Click `Create Knowledgebase` to embed `codebasics_faqs.csv` and save a local FAISS index
- Ask a question; the app retrieves matching rows and answers using a custom prompt with Google PaLM
- Retrieval is grounded via a score-threshold retriever to reduce hallucinations

## Requirements

- Python 3.9+
- Google PaLM API key (`GOOGLE_API_KEY`) in `.env`
- Additional packages commonly required by instructor embeddings:
  - `sentence-transformers`
  - `InstructorEmbedding`

Dependencies pinned in `requirements.txt` include `langchain`, `streamlit`, `faiss-cpu`, `tiktoken`, and `python-dotenv`.

## Installation

```bash
# From repo root
cd "project codebasics Q&A"

# (Optional) create and activate a virtual environment
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# If embeddings raise import errors, install these as well:
pip install sentence-transformers InstructorEmbedding
```

Create a `.env` file in `project codebasics Q&A/` and add your key:

```
GOOGLE_API_KEY=YOUR_KEY_HERE
```

## Data

- `codebasics_faqs.csv` with a `prompt` column used as the source text
- A prebuilt FAISS index may exist under `faiss_index/` and will be reused

## Run

```bash
streamlit run main.py
```

## Usage

- Click `Create Knowledgebase` to load the CSV, embed rows, and save the FAISS index
- Type your question in the input box
- The app displays the answer grounded on retrieved CSV content

## Configuration

- Streamlit UI and actions: `langchain-projects\project codebasics Q&A\main.py:4-13`
- Answer display: `langchain-projects\project codebasics Q&A\main.py:15-16`
- FAISS index path: `langchain-projects\project codebasics Q&A\langchain_helper.py:16`
- CSV loader and source column: `langchain-projects\project codebasics Q&A\langchain_helper.py:20-21`
- Embeddings model: `HuggingFaceInstructEmbeddings("hkunlp/instructor-large")`: `langchain-projects\project codebasics Q&A\langchain_helper.py:15`
- PaLM LLM setup and temperature: `langchain-projects\project codebasics Q&A\langchain_helper.py:13`
- Retriever with score threshold: `langchain-projects\project codebasics Q&A\langchain_helper.py:36`
- Custom prompt template: `langchain-projects\project codebasics Q&A\langchain_helper.py:38-48`
- RetrievalQA chain configuration: `langchain-projects\project codebasics Q&A\langchain_helper.py:50-56`

## Project Structure

```
project codebasics Q&A/
├─ main.py
├─ langchain_helper.py
├─ requirements.txt
├─ .env
├─ codebasics_faqs.csv
└─ faiss_index/
   ├─ index.faiss
   └─ index.pkl
```

## Troubleshooting

- Missing embeddings libraries: install `sentence-transformers` and `InstructorEmbedding`
- Large model download: `hkunlp/instructor-large` downloads at first run; ensure stable internet and disk space
- PaLM auth errors: verify `GOOGLE_API_KEY` in `.env` and that the account has access
- Index not found: click `Create Knowledgebase` to build `faiss_index/`
- Empty answers: check the `prompt` column in the CSV has relevant content; lower `score_threshold` if retrieval is too strict

## License

Use Google PaLM and any dataset according to their terms. Ensure you have rights to the CSV data and comply with applicable policies.