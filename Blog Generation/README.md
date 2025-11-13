# Blog Generation (Llama 2 + Streamlit)

A simple Streamlit app that generates short blog posts using a local Llama 2 model via `ctransformers` and `langchain`.

## Overview

- UI built with `streamlit`
- Text generation powered by a local GGML Llama 2 model through `ctransformers`
- Prompting handled with `langchain` `PromptTemplate`

## Requirements

- Python 3.8+
- A compatible GGML Llama 2 model file (example used in this app: `llama-2-7b-chat.ggmlv3.q8_0.bin`)
- CPU with AVX support recommended for `ctransformers`

## Installation

```bash
# From the repo root
cd "blog generation"

# (Optional) create and activate a virtual environment
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

## Model Setup

Place your model file under `models/` and ensure the filename matches the path referenced in the app:

- Expected path in the code: `models/llama-2-7b-chat.ggmlv3.q8_0.bin`
- You can use any compatible GGML model; update the path if you choose a different file.

> Note: Obtain a legally licensed Llama 2 model in GGML format from a trusted source. Respect the model license terms.

## Run the App

```bash
streamlit run app.py
```

The app starts a local server and opens your default browser.

## Usage

- Enter a blog topic in the text field
- Set the approximate number of words
- Choose the writing style: `Researchers`, `Data Scientist`, or `Common People`
- Click `Generate` to produce the blog text

## Configuration

Adjust generation parameters in `app.py`:

- Model file path: `models/llama-2-7b-chat.ggmlv3.q8_0.bin`
- `max_new_tokens` and `temperature` in the `config` dict
- Prompt template controls style, topic, and length

## Project Structure

```
blog generation/
├─ app.py
├─ requirements.txt
└─ models/
   └─ llama-2-7b-chat.ggmlv3.q8_0.bin  # not included; add your own
```

## Troubleshooting

- If the app fails to load the model, verify the file path and format (GGML).
- Slow generation on CPU is expected; reduce `max_new_tokens` or use a smaller model.
- Ensure `ctransformers` installed correctly; some environments require Visual C++ Build Tools on Windows.

## License

This project wraps a locally stored Llama 2 model. Make sure you comply with the model's license and any usage restrictions.