# Text Summarization (Notebook + LangChain)

A notebook-driven project for summarizing text content using LangChain and OpenAI. It includes utilities for loading and preprocessing text or PDFs and generating concise summaries.

## Overview

- Load and preprocess text/PDF content (packages include `unstructured`, `PyPDF2`, `pdfminer`, `pdf2image`)
- Generate summaries using LangChain with OpenAI models
- Run inside `summarization.ipynb` for step-by-step exploration

## Requirements

- Python 3.9+
- OpenAI API key (`OPENAI_API_KEY`)
- Jupyter-compatible environment (VS Code, JupyterLab, or Notebook)

## Installation

```bash
# From repo root
cd "text summarization"

# (Optional) create and activate a virtual environment
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

## Configure API Key

Set your OpenAI key in the environment before running the notebook:

```powershell
$env:OPENAI_API_KEY = "YOUR_KEY_HERE"
```

Alternatively, add it to your environment manager or a `.env` loaded by your notebook.

## Run

- Open `summarization.ipynb` in your notebook environment
- Execute cells in order to load input data and produce a summary

## Input Sources

- Plain text content
- PDFs via `PyPDF2`/`pdfminer`; for scanned PDFs, `pdf2image` may be used to convert pages before OCR (not included by default)
- `unstructured` can help parse diverse document formats

## Tips

- For long content, split text into chunks with overlap and summarize iteratively
- Use map-reduce style summarization for large documents to avoid token limits
- Adjust model temperature and prompt instructions to control style and conciseness

## Troubleshooting

- Missing API key or auth errors: ensure `OPENAI_API_KEY` is set and valid
- PDF parsing issues: try alternative loaders (`PyPDF2`, `pdfminer`, `unstructured`) depending on PDF structure
- Token limits: chunk input and summarize progressively; reduce verbosity
- If using `pdf2image`, ensure poppler is installed on your system

## Dependencies

From `requirements.txt`:

- `langchain`, `openai`, `streamlit`, `tiktoken`, `unstructured`, `pdf2image`, `pdfminer`, `PyPDF2`

## License

Use OpenAI and any source documents according to their terms. Ensure you have rights to the content you summarize and comply with applicable policies.
