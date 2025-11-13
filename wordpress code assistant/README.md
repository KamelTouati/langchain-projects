# WordPress Code Assistant (LangChain + OpenAI + Streamlit)

A Streamlit app that generates WordPress PHP code for common tasks by guiding an LLM with structured prompts, and optionally runs a QA cross-check to validate the generated code.

## Overview

- Select a sample WordPress task or provide a custom task
- Generate PHP code and optionally reveal the thinking process
- Run a QA cross-check chain to validate suitability against the requested task
- Built with LangChain `LLMChain` and `ChatPromptTemplate` using OpenAI chat models

## Requirements

- Python 3.9+
- OpenAI API key (`OPENAI_API_KEY`) — entered directly in the UI

## Installation

```bash
# From repo root
cd "wordpress code assistant"

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

- Paste your OpenAI API key
- Choose a model (`gpt-3.5-turbo` or `gpt-4`, if eligible)
- Pick a sample task or select `Custom` and write your own
- Check “Display the full thinking process” to show chain reasoning
- Check “Execute an additional chain to cross-check the code provided” to run a QA validation
- Click `🚀 Generate Code` to produce PHP code blocks

## Configuration

- Page config and headers: `langchain-projects\wordpress code assistant\app.py:7-16`
- Intro and task expander details: `langchain-projects\wordpress code assistant\app.py:18-45`
- API key input: `langchain-projects\wordpress code assistant\app.py:56`
- Model selection: `langchain-projects\wordpress code assistant\app.py:58-65`
- Task selection and custom input: `langchain-projects\wordpress code assistant\app.py:67-83`
- Execution, code prompt, and generation: `langchain-projects\wordpress code assistant\app.py:89-123`
- Thinking process toggle: `langchain-projects\wordpress code assistant\app.py:123-129`
- QA cross-check chain: `langchain-projects\wordpress code assistant\app.py:130-146`
- Notes and tips sections: `langchain-projects\wordpress code assistant\app.py:147-165`
- Theme and privacy: `langchain-projects\wordpress code assistant\.streamlit\config.toml:1-5`

## Project Structure

```
wordpress code assistant/
├─ app.py
├─ requirements.txt
├─ .gitignore
└─ .streamlit/
   └─ config.toml
```

## Troubleshooting

- Missing API key or auth errors: ensure your `OPENAI_API_KEY` is active and pasted correctly
- GPT‑4 access: only available if your OpenAI account is eligible
- PHP code extraction: the app extracts fenced ```php blocks; ensure the model outputs proper formatting
- Vague tasks: provide specific requirements to reduce hallucinations; use the QA cross-check feature

## Dependencies

From `requirements.txt`:

- `langchain`, `langchain-community`, `openai`, `streamlit`

## License

Use OpenAI APIs according to their terms. Ensure you have rights to any WordPress code or assets you generate and comply with applicable policies.