# AtliQ T-Shirts SQL Q&A (MySQL + PaLM + LangChain)

A Streamlit app that answers questions about a MySQL t‑shirts inventory using LangChain’s SQL chain with few‑shot prompting and semantic example selection. It generates SQL, executes it against the database, and returns a grounded answer.

## Overview

- MySQL schema and seed data provided in `database/db_creation_atliq_t_shirts.sql`
- Few‑shot examples stored in a Chroma vector store to guide query generation
- SQL generation and execution via `SQLDatabaseChain`
- Answers produced by Google PaLM (`GooglePalm`) with a MySQL‑specific prompt

## Requirements

- Python 3.9+
- MySQL Server running locally
- Google PaLM API key (`GOOGLE_API_KEY`) in `.env`

## Installation

```bash
# From repo root
cd "sqldb tshirts"

# (Optional) create and activate a virtual environment
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### Database Setup (MySQL)

1) Start MySQL locally and create the schema with the provided script:

- `langchain-projects\sqldb tshirts\database\db_creation_atliq_t_shirts.sql`

You can run it via MySQL Workbench or CLI:

```sql
SOURCE path\to\db_creation_atliq_t_shirts.sql;
```

This creates `atliq_tshirts`, tables `t_shirts` and `discounts`, seeds 100 randomized records, and inserts 10 discount rows.

### Environment

Create `.env` in `sqldb tshirts/` with:

```
GOOGLE_API_KEY=YOUR_PALM_KEY
```

## Run

```bash
streamlit run main.py
```

## Usage

- Type a natural‑language question (e.g., “How many t‑shirts do we have left for Nike in XS size and white color?”)
- The app selects relevant few‑shot examples, generates a MySQL query, executes it, and returns the answer

## Configuration

- App UI and chain invocation: `langchain-projects\sqldb tshirts\main.py:4-13`
- DB connection (credentials, host, db name): `langchain-projects\sqldb tshirts\langchain_helper.py:19-25`
- PaLM LLM setup: `langchain-projects\sqldb tshirts\langchain_helper.py:26`
- Embeddings model for example selector: `sentence-transformers/all-MiniLM-L6-v2`: `langchain-projects\sqldb tshirts\langchain_helper.py:28-34`
- MySQL guidance prompt and output format: `langchain-projects\sqldb tshirts\langchain_helper.py:35-49`
- Few‑shot examples: `langchain-projects\sqldb tshirts\few_shots.py:1-34`
- Chain construction (`SQLDatabaseChain` with custom prompt): `langchain-projects\sqldb tshirts\langchain_helper.py:56-64`

## Project Structure

```
sqldb tshirts/
├─ main.py
├─ langchain_helper.py
├─ few_shots.py
├─ requirements.txt
├─ .env
└─ database/
   └─ db_creation_atliq_t_shirts.sql
```

## Troubleshooting

- MySQL connection failed: verify server is running and credentials match; update user/password/host in `langchain_helper.py`
- Missing embeddings: ensure `sentence-transformers` installed (included in `requirements.txt`)
- PaLM auth errors: confirm `GOOGLE_API_KEY` in `.env` and account access
- SQL errors: the chain uses a strict MySQL prompt (backticks, `LIMIT`, valid columns). Check schema and data were created successfully

## Dependencies

From `requirements.txt`:

- `langchain`, `langchain_experimental`, `streamlit`, `tiktoken`, `faiss-cpu`, `mysql-connector-python`, `pymysql`, `sentence-transformers`, `chromadb`, `python-dotenv`, `protobuf`

## License

Use Google PaLM and MySQL according to their terms. Ensure you have rights to any data used and comply with applicable policies.