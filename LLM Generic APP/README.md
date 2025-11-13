# LLM Generic App (PDF → Embeddings → Pinecone → QA)

A notebook-driven demo that loads PDFs, chunks content, creates OpenAI embeddings, stores them in a Pinecone vector index, and answers questions by retrieving relevant chunks and prompting an LLM.

## Overview

- Load all PDFs from `documents/` and prepare text
- Chunk content with `RecursiveCharacterTextSplitter`
- Create embeddings using OpenAI
- Store vectors in Pinecone and run similarity search
- Answer questions via a QA chain using an OpenAI LLM

## Requirements

- Python 3.9+
- OpenAI API key (`OPENAI_API_KEY`)
- Pinecone API key (`PINECONE_API_KEY`) and environment (`PINECONE_ENV`)
- Jupyter-compatible environment (VS Code, JupyterLab, or Notebook)

## Installation

```bash
# From repo root
cd "LLM generic app"

# (Optional) create and activate a virtual environment
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in `LLM generic app/` and add your keys:

```
OPENAI_API_KEY=YOUR_OPENAI_KEY
PINECONE_API_KEY=YOUR_PINECONE_KEY
PINECONE_ENV=YOUR_PINECONE_ENV
```

## Data

- Place PDFs in `documents/`
- A sample file is provided: `documents/budget_speech.pdf`

## Run

- Open `test.ipynb` in your notebook environment
- Run cells in order to load documents, build the index, and issue queries

## Workflow Details

- Load PDFs: `langchain-projects\LLM generic app\test.ipynb:66-71`
- Chunk text: `langchain-projects\LLM generic app\test.ipynb:100-106`
- Initialize embeddings (OpenAI): `langchain-projects\LLM generic app\test.ipynb:146-149`
- (Optional) Pinecone init snippet: `langchain-projects\LLM generic app\test.ipynb:179-185`
- Create Pinecone index from documents: `langchain-projects\LLM generic app\test.ipynb:193`
- Similarity search function: `langchain-projects\LLM generic app\test.ipynb:202-206`
- QA chain setup (`text-davinci-003`, stuff): `langchain-projects\LLM generic app\test.ipynb:224-226`
- Retrieve answers: `langchain-projects\LLM generic app\test.ipynb:234-239`
- Example query: `langchain-projects\LLM generic app\test.ipynb:257-260`

## Notes

- Ensure Pinecone is initialized and `index_name` is set before calling `Pinecone.from_documents(...)`
- Consider using modern chat models (e.g., `gpt-3.5-turbo`) for QA to reduce cost and improve latency
- For larger documents, tune `chunk_size` and `chunk_overlap` and consider pre-processing with `unstructured`

## Troubleshooting

- Jupyter `IProgress` warning: install `ipywidgets` for progress bars
- Pinecone auth or environment errors: verify `PINECONE_API_KEY` and `PINECONE_ENV`
- OpenAI auth errors: verify `OPENAI_API_KEY`
- Empty results: confirm the index was created and documents were embedded successfully

## Dependencies

From `requirements.txt`:

- `unstructured`, `tiktoken`, `pinecone-client`, `pypdf`, `openai`, `langchain`, `pandas`, `numpy`, `python-dotenv`

## License

Use OpenAI and Pinecone according to their terms. Ensure you have rights to the PDFs you process and comply with applicable policies.