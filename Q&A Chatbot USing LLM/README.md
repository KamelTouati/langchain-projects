# Q&A Chatbot Using LLM (LangChain + OpenAI + Streamlit)

A minimal Streamlit chatbot that sends a single question to an OpenAI completion model via LangChain and displays the answer.

## Overview

- Uses `langchain.llms.OpenAI` with `text-davinci-003`
- Simple Streamlit UI for entering a question and showing the response

## Requirements

- Python 3.9+
- OpenAI API key (`OPENAI_API_KEY`) available in your environment

## Installation

```bash
# From repo root
cd "Q&A chatbot using LLM"

# (Optional) create and activate a virtual environment
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

## Configure API Key

- Set `OPENAI_API_KEY` in your shell environment before running the app, for example:

```powershell
$env:OPENAI_API_KEY = "YOUR_KEY_HERE"
```

- Alternatively, create a `.env` file and load it by uncommenting the dotenv lines in `app.py`:
  - `langchain-projects\Q&A chatbot using LLM\app.py:4-7`

## Run the App

```bash
streamlit run app.py
```

The app launches a local server and opens in your browser.

## Usage

- Enter your question in the input field
- Click `Ask the question`
- The model answer is displayed under “The Response is”

## Configuration

- Page config and header: `langchain-projects\Q&A chatbot using LLM\app.py:21-24`
- Model setup (`text-davinci-003`, `temperature=0.5`): `langchain-projects\Q&A chatbot using LLM\app.py:15`
- Response call flow: `langchain-projects\Q&A chatbot using LLM\app.py:14-17,25-35`

## Project Structure

```
Q&A chatbot using LLM/
├─ app.py
├─ requirements.txt
└─ langchain.ipynb
```

`langchain.ipynb` contains exploratory notes/demos (optional).

## Troubleshooting

- Missing API key or auth errors: ensure `OPENAI_API_KEY` is set in your environment
- Model availability: `text-davinci-003` is a legacy completion model; consider switching to a chat model if your account no longer supports it
- Streamlit not found: confirm `pip install -r requirements.txt` ran successfully

## Dependencies

From `requirements.txt`:

- `langchain`, `openai`, `python-dotenv`, `streamlit`
- `huggingface_hub` is listed but not used directly in `app.py`

## License

Use OpenAI APIs according to their terms. Ensure content complies with applicable policies.