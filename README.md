# LangChain Projects — Repository Overview

A curated collection of small LangChain/LLM demos and utilities. Each subproject is self‑contained with its own `README.md` or notebook and focuses on a single capability (chat, retrieval, summarization, SQL, PDFs, audio, code generation, etc.).

## Quick Start

- Use per‑project `README.md` files for setup and run instructions
- Common prerequisites: Python 3.9+, virtual environments, API keys where required
- Typical run command for apps: `streamlit run app.py` inside the project folder

## Project Index

- `blog generation/` — Streamlit app generating short blogs via local Llama 2 (`ctransformers`)
- `calories health/` — Gemini Vision nutrition analyzer from food images; optional SQL demo
- `chat multiple documents/` — Chat over multiple PDFs with FAISS + Gemini
- `conversational Q&A chatbot/` — ChatOpenAI conversational demo with simple memory
- `invoice data extractor/` — Extract structured JSON from invoices using LangChain parsers
- `langchain audio to text/` — Whisper transcription with optional post‑processing via chat models
- `langchain basic qa/` — RetrievalQA over a single PDF using in‑memory doc store
- `langchain summarization/` — Web page summarization using `stuff`, `map_reduce`, `refine` chains
- `LLM generic app/` — Notebook pipeline: PDFs → OpenAI embeddings → Pinecone → QA
- `news research tool project/` — RockyBot: URLs → FAISS index → QA with sources
- `project codebasics Q&A/` — CSV FAQs → FAISS + Instructor embeddings → PaLM Q&A
- `Q&A chatbot using LLM/` — Minimal single‑turn Q&A with OpenAI completions
- `sqldb tshirts/` — MySQL inventory Q&A via SQLDatabaseChain and few‑shot prompts
- `text summarization/` — Notebook‑based summarization for text/PDFs
- `wordpress code assistant/` — Generate WordPress PHP code with QA cross‑check

## How This Index Was Built

- The file `project_structure.text` enumerates the repository’s current layout and was used to compile this overview: `langchain-projects\project_structure.text:1-110`

## Notes

- API keys: many apps require keys (OpenAI, Google Generative AI, etc.). See individual project READMEs
- OS specifics: some projects include Windows‑specific dependencies (e.g., `python-magic-bin` for `unstructured`)
- Notebooks: open with Jupyter/VS Code; run cells sequentially

## License

Each app uses third‑party APIs and models subject to their terms. Ensure you have rights to any data you process and comply with applicable licenses and policies.