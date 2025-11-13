# LangChain Summarization (Web Loader + Chain Types + Streamlit)

A Streamlit app that summarizes web pages using LangChain’s built-in summarize chains. Enter a URL, choose a chain type (`stuff`, `map_reduce`, `refine`), and get a concise summary powered by OpenAI chat models.

## Overview

- Loads and splits web content via `WebBaseLoader`
- Summarizes using `load_summarize_chain` with selectable chain types
- Uses `ChatOpenAI` to generate the summary
- Simple Streamlit UI with URL validation and chain selection

## Requirements

- Python 3.9+
- OpenAI API key (`OPENAI_API_KEY`) — entered in the app UI

## Installation

```bash
# From repo root
cd "langchain summarization"

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
- Enter a valid webpage URL
- Select a chain type: `stuff`, `map_reduce`, or `refine`
- Click `🚀 Execute` to generate the summary

## Chain Types

- `stuff`: Concatenates all documents and sends them in one pass. Fast and simple; limited by model token constraints.
- `map_reduce`: Splits into chunks, summarizes each in parallel, then reduces to a final summary. Handles longer content better.
- `refine`: Iteratively improves the summary across chunks with sequential LLM calls. Often more precise, but slower.

## Configuration

- Page config and headers: `langchain-projects\langchain summarization\app.py:7-16`
- Security notice: `langchain-projects\langchain summarization\app.py:39-41`
- API key and form: `langchain-projects\langchain summarization\app.py:42-54`
- URL validation: `langchain-projects\langchain summarization\app.py:57-58`
- Web loader and splitting: `langchain-projects\langchain summarization\app.py:59-62`
- Chat model and chain: `langchain-projects\langchain summarization\app.py:63-66`
- Summary execution and display: `langchain-projects\langchain summarization\app.py:67-73`
- Chain explanations and takeaways: `langchain-projects\langchain summarization\app.py:75-131`
- Theme and privacy: `langchain-projects\langchain summarization\.streamlit\config.toml:1-5`

## Project Structure

```
langchain summarization/
├─ app.py
├─ requirements.txt
├─ .gitignore
└─ .streamlit/
   └─ config.toml
```

## Troubleshooting

- Invalid URL: ensure the address is correct; the app validates via `validators`.
- Token limits with `stuff`: switch to `map_reduce` or `refine` for long pages.
- Slow responses with `refine`: it runs sequentially; choose `map_reduce` for speed.
- Auth errors: confirm your OpenAI key is active and correctly pasted.

## Dependencies

From `requirements.txt`:

- `bs4`, `langchain`, `langchain-community`, `openai`, `streamlit`, `tiktoken`, `validators`

## License

Use OpenAI APIs according to their terms. Ensure you have rights to the web content you summarize and comply with applicable policies.