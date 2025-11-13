# Conversational Q&A Chatbot (LangChain + OpenAI + Streamlit)

A minimal Streamlit chatbot that maintains conversation history with LangChain and responds using OpenAI's chat models.

## Overview

- Conversation state stored in `st.session_state`
- Persona set by an initial system message (comedian assistant)
- Responses generated via `ChatOpenAI` from LangChain
- Simple Streamlit UI for input and display

## Requirements

- Python 3.9+
- OpenAI API key (`OPENAI_API_KEY`)

## Installation

```bash
# From repo root
cd "conversational Q&A chatbot"

# (Optional) create and activate a virtual environment
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in `conversational Q&A chatbot/` and add your OpenAI key:

```
OPENAI_API_KEY=YOUR_KEY_HERE
```

## Run the App

```bash
streamlit run app.py
```

The app launches a local server and opens in your browser.

## Usage

- Enter a message in the input field
- Click `Ask the question`
- The model replies and the conversation history is persisted across turns

## Configuration

- Environment load: `langchain-projects\conversational Q&A chatbot\app.py:11-14`
- Chat model init: `ChatOpenAI(temperature=0.5)`: `langchain-projects\conversational Q&A chatbot\app.py:15`
- Conversation memory (`flowmessages`) with system prompt: `langchain-projects\conversational Q&A chatbot\app.py:17-21`
- Response flow in `get_chatmodel_response`: `langchain-projects\conversational Q&A chatbot\app.py:24-29`
- Streamlit UI: `langchain-projects\conversational Q&A chatbot\app.py:8-10,31-40`

## Project Structure

```
conversational Q&A chatbot/
├─ app.py
├─ requirements.txt
└─ langchain.ipynb
```

- `langchain.ipynb` contains exploratory notes/demos (optional).

## Troubleshooting

- Missing API key: ensure `.env` contains `OPENAI_API_KEY` and your shell session can read it.
- Rate limits or auth errors: verify the OpenAI account status and key permissions.
- Streamlit not found: confirm `pip install -r requirements.txt` ran successfully.

## Dependencies

From `requirements.txt`:

- `langchain`, `openai`, `python-dotenv`, `streamlit`
- `huggingface_hub` is listed but not required by `app.py` directly.

## License

Use OpenAI APIs according to their terms. Ensure chat content complies with relevant policies.