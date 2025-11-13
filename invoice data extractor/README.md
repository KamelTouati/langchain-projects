# Invoice Data Extractor (LangChain + OpenAI + Streamlit)

A Streamlit app that extracts structured fields from PDF invoices using LangChain document loaders, a chat prompt, and structured output parsing. Returns a clean JSON object with key invoice details.

## Overview

- Upload a PDF invoice and parse text with `PyPDFLoader`
- Prompt an OpenAI chat model to extract fields
- Enforce a JSON schema with `StructuredOutputParser`
- Render the resulting JSON in the UI

## Requirements

- Python 3.9+
- OpenAI API key (`OPENAI_API_KEY`) — entered in the app UI

## Installation

```bash
# From repo root
cd "invoice data extractor"

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
- Upload a PDF invoice
- The app extracts text, asks the model to produce JSON, and displays the parsed result

## Extracted Fields

- `number`: invoice number
- `date`: issued date (mm-dd-yyyy)
- `company`: company name
- `address`: full company address (address, city (state), country)
- `service`: purchased service description
- `total`: grand total amount (number)

## Configuration

- Page setup and headers: `langchain-projects\invoice data extractor\app.py:10-20`
- Security notice: `langchain-projects\invoice data extractor\app.py:29-31`
- API key input and PDF upload: `langchain-projects\invoice data extractor\app.py:32-35`
- PDF text loading via `PyPDFLoader`: `langchain-projects\invoice data extractor\app.py:44-47`
- Response schema and parser: `langchain-projects\invoice data extractor\app.py:49-60`
- Prompt template and format instructions: `langchain-projects\invoice data extractor\app.py:62-86`
- Chat model invocation and parsing: `langchain-projects\invoice data extractor\app.py:87-97`
- Cleanup of temp file: `langchain-projects\invoice data extractor\app.py:99-100`

Theme and telemetry configuration:

- Streamlit theme: `langchain-projects\invoice data extractor\.streamlit\config.toml:1-3`
- Disable usage stats: `langchain-projects\invoice data extractor\.streamlit\config.toml:4-5`

## Project Structure

```
invoice data extractor/
├─ app.py
├─ requirements.txt
├─ .gitignore
└─ .streamlit/
   └─ config.toml
```

## Troubleshooting

- Invalid API key or auth errors: confirm the key is active and correctly pasted
- PDF text extraction issues: some PDFs have limited text; scanned PDFs may require OCR
- Rate limiting or model errors: retry later or reduce usage
- If parsing fails, verify fields and prompt formatting; adjust temperature or schema descriptions

## Dependencies

From `requirements.txt`:

- `langchain`, `langchain-community`, `openai`, `pypdf`, `streamlit`, `tiktoken`

## License

Use OpenAI APIs according to their terms. Ensure you have rights to the PDF invoices you process and comply with applicable policies.