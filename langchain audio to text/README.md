# LangChain Audio to Text (Whisper + Streamlit)

A Streamlit app that transcribes voice memos to text using OpenAI Whisper and optionally post-processes the transcript with a custom prompt via LangChain chat models.

## Overview

- Upload multiple audio files (`m4a`, `mp3`) and transcribe each with Whisper
- Outputs raw transcript or runs a post-processing prompt with `ChatOpenAI`
- Uses a simple custom audio loader that returns a LangChain `Document`
- Clean Streamlit UI, with optional model selection (`gpt-3.5-turbo`, `gpt-4`)

## Requirements

- Python 3.9+
- OpenAI API key (`OPENAI_API_KEY`) — entered directly in the app UI

## Installation

```bash
# From repo root
cd "langchain audio to text"

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
- Upload one or more voice memos (`m4a`, `mp3`)
- Optionally enable post-processing and provide a custom prompt
- Click `🖊️ Process Voice Memos` to transcribe and process

## Post-Processing

- Enable the checkbox to run a custom prompt that transforms the transcript (e.g., change tone, translate, summarize, structure into chapters)
- Select a chat model (`gpt-3.5-turbo` or `gpt-4` as available to your account)
- Provide a prompt; recommended to start with "Given the following transcript..."

## Configuration

- Page config and headers: `langchain-projects\langchain audio to text\app.py:10-13,27-31`
- API key input: `langchain-projects\langchain audio to text\app.py:51`
- File upload and options: `langchain-projects\langchain audio to text\app.py:53-56`
- Custom audio loader calling Whisper: `langchain-projects\langchain audio to text\app.py:15-25`
- Processing form and execution: `langchain-projects\langchain audio to text\app.py:57-79`
- Temporary file handling: `langchain-projects\langchain audio to text\app.py:87-93,117-118`
- Post-processing chain (`ChatOpenAI` + `LLMChain`): `langchain-projects\langchain audio to text\app.py:97-115`
- Theme and privacy: `langchain-projects\langchain audio to text\.streamlit\config.toml:1-5`

## Project Structure

```
langchain audio to text/
├─ app.py
├─ requirements.txt
├─ .gitignore
└─ .streamlit/
   └─ config.toml
```

## Troubleshooting

- Invalid API key or auth errors: ensure your key is active and pasted correctly
- GPT‑4 access: only available if your account is eligible
- Audio format issues: use `m4a` or `mp3`; large or corrupted files may fail
- OpenAI Python SDK version: this app uses `openai.Audio.transcribe` with `model="whisper-1"`; if using a newer SDK, adjust to the current transcription method
- Rate limits or server errors: retry later or reduce request volume

## Dependencies

From `requirements.txt`:

- `langchain`, `langchain-community`, `openai`, `streamlit`

## License

Use OpenAI APIs according to their terms. Ensure you have rights to the audio you process and comply with applicable policies.