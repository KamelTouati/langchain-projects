# Calories Health (Gemini Vision + Streamlit)

A Streamlit app that analyzes a food image with Google's Gemini Vision model and returns an itemized calorie breakdown and total calories. Includes an additional demo to convert natural-language questions to SQL and query a local SQLite database.

## Overview

- Uses `google-generativeai` Gemini models
- Image workflow: `gemini-pro-vision` estimates calories per item from the image
- UI built with `streamlit`
- Environment loaded with `python-dotenv`
- Optional SQL LLM demo in `sqlllm/`

## Requirements

- Python 3.9+
- A valid `GOOGLE_API_KEY` for Google Generative AI
- Image files: `jpg`, `jpeg`, or `png`

## Installation

```bash
# From repo root
cd "calories health"

# (Optional) create and activate a virtual environment
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in `calories health/` and add your key:

```
GOOGLE_API_KEY=YOUR_KEY_HERE
```

## Run the App

```bash
streamlit run app.py
```

The app launches a local server and opens in your browser.

## Usage

- Enter an instruction in the "Input Prompt" field (optional, provides extra context)
- Upload a food image (`jpg`, `jpeg`, `png`)
- Click `Tell me about the image`
- The app displays an itemized list and total calories

## Configuration

- `GOOGLE_API_KEY` read from environment: `langchain-projects\calories health\app.py:18-20`
- Model: `gemini-pro-vision` used in `get_gemini_response`: `langchain-projects\calories health\app.py:24`
- Image preprocessing in `input_image_setup`: `langchain-projects\calories health\app.py:29-43`
- Default nutrition prompt: `input_prompt`: `langchain-projects\calories health\app.py:61-70`

## Project Structure

```
calories health/
├─ app.py
├─ requirements.txt
└─ sqlllm/
   ├─ requirements.txt
   ├─ sql.py
   └─ sqlite.py
```

## SQL LLM Demo (Optional)

Translate English questions into SQL and run them against a local SQLite database.

1) Initialize the demo database:

```bash
python sqlllm/sqlite.py
```

This creates `test.db` with a `STUDENT` table: `langchain-projects\calories health\sqlllm\sqlite.py:12-20`.

2) Run the Streamlit SQL app:

```bash
streamlit run sqlllm/sql.py
```

- The app generates SQL with `gemini-pro` (`langchain-projects\calories health\sqlllm\sql.py:19`) from natural-language questions and displays results.
- SQL execution via `read_sql_query`: `langchain-projects\calories health\sqlllm\sql.py:26-33`.

## Troubleshooting

- Missing or invalid API key: ensure `.env` contains `GOOGLE_API_KEY` and your shell session can read it.
- Image not rendering: verify supported formats and that the file isn’t corrupted.
- Streamlit not found: confirm `pip install -r requirements.txt` ran without errors.
- SQLite demo errors: run `sqlllm/sqlite.py` first to create `test.db`.

## Dependencies

Key packages (see `requirements.txt` for full list):

- `streamlit`, `google-generativeai`, `python-dotenv`
- Optional: `langchain`, `chromadb`, `faiss-cpu`, `PyPDF2`, `pdf2image`

## License

Use Google Generative AI in accordance with its terms. Ensure you have rights to any images you analyze and comply with applicable policies.