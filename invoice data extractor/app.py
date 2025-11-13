import os
import tempfile
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.document_loaders import PyPDFLoader
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

st.set_page_config(
    page_title="Invoice Data Extractor | Learn LangChain",
    page_icon="🧾"
)

st.header('🧾 Invoice Data Extractor')

st.subheader('Learn LangChain | Demo Project #1')

st.success("This is a demo project related to the [Learn LangChain](https://learnlangchain.org/) mini-course.")

st.write('''
In this project we will use LangChain document loaders, prompts and parsers to develop an AI virtual
assistant trained to extract data from our PDF invoices and return them in JSON.

In a real-world use case, these data can be further processed and stored in an Excel file, sent
to our accounting software via API and handled according to out data pipeline needs.
''')

st.info("You need your own keys to run commercial LLM models.\
    The form will process your keys safely and never store them anywhere.", icon="🔒")

openai_key = st.text_input("OpenAI Api Key")

invoice_file = st.file_uploader("Upload a PDF invoice", type=["pdf"])

if invoice_file is not None:

    with st.spinner('Processing your request...'):

        with tempfile.NamedTemporaryFile(delete=False) as temporary_file:

            temporary_file.write(invoice_file.read())

        loader = PyPDFLoader(temporary_file.name)

        text_invoice = loader.load()

        # format the response schema
        number = ResponseSchema(name="number", description="What's the invoice number? Answer null if unclear.")
        date = ResponseSchema(name="date", description="What's the issued date of the invoice? Format it as mm-dd-yyyy, answer null if unclear.")
        company = ResponseSchema(name="company", description="What's the name of the company who issued the invoice? Answer null if unclear.")
        address = ResponseSchema(name="address", description="What's the full address of the company who issued the invoice? Format it as address, city (state), country, answer null if unclear.")
        service = ResponseSchema(name="service", description="What is the service purchased with this invoice? Answer null if unclear.")
        total = ResponseSchema(name="total", description="What's the grand total amount of the invoice? Format is as a number, answer null if unclear.")

        response_schemas = [number, date, company, address, service, total]

        output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

        format_instructions = output_parser.get_format_instructions()

        template = """\
        This document is an invoice, extract the following information:

        number: What's the invoice number? Answer null if unclear.
        date: What's the issued date of the invoice? Format it as mm-dd-yyyy, answer null if unclear.
        company: What's the name of the company who issued the invoice? Answer null if unclear.
        address: What's the full address of the company who issued the invoice? Format it as address, city (state), country, answer null if unclear.
        service: What is the service purchased with this invoice? Answer null if unclear.
        total: What's the grand total amount of the invoice? Format is as a number, answer null if unclear.

        Format the output as JSON with the following keys:
        number
        date
        company
        address
        service
        total

        text: {text}

        {format_instructions}
        """

        prompt_template = ChatPromptTemplate.from_template(template=template)

        chat = ChatOpenAI(openai_api_key=openai_key, temperature=0)

        format_template = prompt_template.format_messages(text=text_invoice, format_instructions=format_instructions)

        response = chat(format_template)

        json_invoice = output_parser.parse(response.content)

        st.write('Here is your JSON invoice:')

        st.json(json_invoice)

        # clean-up the temporary file
        os.remove(temporary_file.name)

with st.expander("Exercise Tips"):
    st.write('''
    - Browse [the code on GitHub](https://github.com/francescocarlucci/invoice-data-extractor/blob/main/app.py) and make sure you understand it.
    - Fork the repository to customize the code.
    - Try to add new elements to parse and add them to the final JSON invoice. Maybe the VAT number? Or the taxes?
    - Improve this code and see if you can use a chain to better orchestrate the prompt and the parser. LLMChain should be ideal for this.
    ''')
    
st.divider()
