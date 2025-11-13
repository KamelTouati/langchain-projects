# RockyBot: News Research Tool (URLs → FAISS → QA)

A Streamlit app that loads news articles from URLs, chunks the content, builds an OpenAI-embeddings FAISS index, and answers questions with cited sources.

## Overview

- Enter up to three URLs in the sidebar
- Load pages via `UnstructuredURLLoader`
- Split text with `RecursiveCharacterTextSplitter`
- Embed with `OpenAIEmbeddings` and save FAISS index to `faiss_store_openai.pkl`
- Ask questions; answers returned by `RetrievalQAWithSourcesChain` with source citations

## Requirements

- Python 3.9+
- OpenAI API key (`OPENAI_API_KEY`) in `.env`
- Windows users: `python-magic-bin` included to satisfy `libmagic` dependency for `unstructured`

## Installation

```bash
# From repo root
cd "news research tool project"

# (Optional) create and activate a virtual environment
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in `news research tool project/` and add:

```
OPENAI_API_KEY=YOUR_KEY_HERE
```

## Run

```bash
streamlit run main.py
```

## Usage

- In the sidebar, paste up to three article URLs
- Click `Process URLs` to load, split, and embed content (builds `faiss_store_openai.pkl`)
- In the main input, type a question and press Enter
- The app shows the answer and lists the sources used

## Configuration

- Title and sidebar UI: `langchain-projects\news research tool project\main.py:15-23`
- Process button and FAISS index path: `langchain-projects\news research tool project\main.py:23-25`
- LLM setup (`OpenAI` temperature and tokens): `langchain-projects\news research tool project\main.py:27`
- URL loading: `langchain-projects\news research tool project\main.py:31-34`
- Text splitter (separators and chunk size): `langchain-projects\news research tool project\main.py:35-41`
- Embeddings + FAISS build and save: `langchain-projects\news research tool project\main.py:42-50`
- Question input and QA chain with sources: `langchain-projects\news research tool project\main.py:51-69`

## Project Structure

```
news research tool project/
├─ main.py
├─ requirements.txt
├─ .env
├─ faiss_store_openai.pkl  # created after processing URLs
├─ notebooks/
│  ├─ retrieval.ipynb
│  ├─ faiss_tutorial.ipynb
│  ├─ text_loaders_splitters.ipynb
│  └─ vector_index.pkl
└─ rockybot.jpg
```

## Troubleshooting

- No index found: click `Process URLs` after entering valid URLs to create `faiss_store_openai.pkl`
- `unstructured` errors on Windows: ensure `python-magic-bin` is installed; it is included in `requirements.txt`
- OpenAI auth issues: verify `OPENAI_API_KEY` in `.env` and that the key is active
- Low-quality answers: adjust `chunk_size` or provide richer sources; increase `max_tokens` in the LLM config if needed
- Rate limits: reduce frequency or switch to a lower temperature and shorter responses

## Dependencies

From `requirements.txt`:

- `langchain`, `python-dotenv`, `streamlit`, `unstructured`, `tiktoken`, `faiss-cpu`, `libmagic`, `python-magic`, `python-magic-bin`, `OpenAI`

## License

Use OpenAI and source content according to their terms. Ensure you have rights to access and process the URLs you load.