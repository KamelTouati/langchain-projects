import os
import tempfile
import streamlit as st
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import DocArrayInMemorySearch

st.set_page_config(
    page_title="Basic QA Over Custom Data | Learn LangChain",
    page_icon="🤖"
)

st.header('🤖 Basic QA Over Custom Data')

st.subheader('Learn LangChain | Demo Project #2')

st.success("This is a demo project related to the [Learn LangChain](https://learnlangchain.org/) mini-course.")

st.write('''
Interacting with custom content is one of the most popular and powerful usage of LLMs and AI systems,
thanks to the vast amount of application opportunities.

Imagine having a virtual assistant capable of instantly summarizing documents for you, going over long
email threads and only extracting the most relevant and useful information, monitoring your team
communication and early detecting any problem out there. Or maybe you wanna go over a contract
and check for hiccups or contradictions? These and many more things are possible using LangChain,
and this is what we built in this tutorial.
''')

st.info("You need your own keys to run commercial LLM models.\
    The form will process your keys safely and never store them anywhere.", icon="🔒")

openai_key = st.text_input("OpenAI Api Key")

pdf_file = st.file_uploader("Upload a PDF document", type=["pdf"])

with st.form("basic_qa"):

    query = st.text_input("Ask anything related to your content:")

    st.write('''
    Here is a few ideas to try:
    - Please, create a very short summary of the document.
    - List all the highlights in a convenient bullet list.
    - My name is xxxx, am I mentioned in the conversation? If so, please list all the parts where I am mentioned.
    - What is the tone of the writing? Can you detect discontent, dissatisfaction, xxxxx?
    ''')

    execute = st.form_submit_button("🚀 Run Query")

    if execute:

        if pdf_file is not None:

            with st.spinner('Processing your request...'):

                with tempfile.NamedTemporaryFile(delete=False) as temporary_file:

                    temporary_file.write(pdf_file.read())

                pdf_loader = PyPDFLoader(temporary_file.name)

                # the PDF loader already splits the doc into pages
                pages = pdf_loader.load()

                embeddings = OpenAIEmbeddings(openai_api_key=openai_key)

                db = DocArrayInMemorySearch.from_documents(pages, embeddings)

                llm = ChatOpenAI(openai_api_key=openai_key, temperature=0)

                qa_chain = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=db.as_retriever())

                response = qa_chain.run(query)

                st.write(response)

                # clean-up the temporary file
                os.remove(temporary_file.name)

        else:
            st.write('Please provide a PDF file.')

with st.expander("Exercise Tips"):
    st.write('''
    - Browse [the code on GitHub](https://github.com/francescocarlucci/langchain-basic-qa/blob/main/app.py) and make sure you understand it.
    - Fork the repository to customize the code.
    - Tired of the OpenAI LLM? Try to plug in another model from the many others supported by LangChain.
    - Wanna work with other file formats? You can use txt, md, csv and even HTML usgin other [document loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/).
    ''')

st.subheader('Known limits:')

st.write('''
This is a simplified imlementation of a proper QA system. It works well with short documents,
email threads, blog posts, contracts, but it will fail if you provide big documents like books
and big databases. For simplicity, the PDF is loaded as vector using an in-memory storage
(DocArrayInMemorySearch), but in other tutorials we will see how to handle big documents or
even multiple files using proper vector databases, indexing and text-splitting. But remember,
sizing an application for his purpose is also an important skill, to avoid over-complicating
system and wasting processing and financial resources.
''')

st.divider()

