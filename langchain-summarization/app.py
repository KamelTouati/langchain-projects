import validators
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain

st.set_page_config(
    page_title="Summarization and Useful Chain Types | Learn LangChain",
    page_icon="📄"
)

st.header('📄 Summarization and Useful Chain Types')

st.subheader('Learn LangChain | Demo Project #3')

st.success("This is a demo project related to the [Learn LangChain](https://learnlangchain.org/) mini-course.")

st.write('''
In the [previous tutorial](https://langchain-basic-qna.streamlit.app/) we built a Question&Answering
system over a custom PDF, and we used the RetrievalQA chain, one of the many built-in chains.
''')

st.code('''
qa_chain = RetrievalQA.from_chain_type(
	llm=ChatOpenAI(openai_api_key=openai_key, temperature = 0), 
	chain_type="stuff", 
	retriever=db.as_retriever()
)
''')

st.write('''
We could even prompt the LLM to provide a summary and it worked, but the RetrievalQA is not ideal
for that purpose. Plus, we passed a "stuff" parameter to the chain without paying much importance to
it. Instead, that parameter is very important and in this tutorial we will se how we can use it 
more appropriately, and how LangChain provides us specific hains for summarization, which is a common
and popular task.
''')

st.info("You need your own keys to run commercial LLM models.\
    The form will process your keys safely and never store them anywhere.", icon="🔒")

openai_key = st.text_input("OpenAI Api Key")

with st.form("summarization"):

	webpage_url = st.text_input("Insert a web page URL to summarize", placeholder="https://francescocarlucci.com/blog/codeable-code-vetting")

	chain_type = st.selectbox(
		'Chain Type',
		('stuff', 'map_reduce', 'refine')
	)

	execute = st.form_submit_button("🚀 Execute")

	if execute:

		if validators.url(webpage_url):

			loader = WebBaseLoader(webpage_url)

			docs = loader.load_and_split()

			llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.2)

			chain = load_summarize_chain(llm, chain_type=chain_type)

			response = chain.run(docs)

			st.write(response)

		else:

			st.write('Please, insert a valid URL.')

st.write('''
The above for executes the `load_summarize_chain(llm, chain_type=chain_type)` function based
on the chain selected in the form. Let's dive into each one of them:
''')

st.subheader('The Stuff Chain')

st.write('''
The stuff chain is one of the simplest and most popular one, because it simply "stuffs" all 
the documents together and passes them the the LLM within the payload. It's very effective,
but has limitations because you can easly hit the token limit on models like OpenAI GPT-3.5
that is limited to 4096 tokens.
`load_summarize_chain()` uses `StuffDocumentsChain` under the hood when the "stuff" chain is
selected.
''')

st.subheader('The Map Reduce Chain')

st.write('''
If we try to summarize a very long document with the stuff chain, the process will fail and
the LLM will return a "token limit" error. To get around this limitation, LangChain provides
many tools, and one of these is the "map_reduce" chain. Basically, it will split the document
into chunks, create summaries of each chunk parallelizing the requests to the LLM, and then 
combine the results into a single summary.
`load_summarize_chain()` uses `ReduceDocumentsChain` under the hood when the "map_reduce" chain
is selected.
''')

st.subheader('The Refine Chain')

st.write('''
Another way to work with big documents and maybe obtain more exact results, is the "refine"
chain. In this case, LangChain will always work with documents chinks, but perform sequential
calls to the LLM and refining the result over the whole process. It can be more previse, but also
slower as the requests are not run in parallel.
`load_summarize_chain()` uses `RefineDocumentsChain` under the hood when the "refine" chain
is selected.
''')

st.subheader('Takeaways')

st.write('''
LangChain can be consider an high level abstraction layer, meaning that it provides simplicity
but sometimes can be hard to understand what is happening under the hood. You can build AI apps
very fast, but on the other hand, as a developer, you want to understand what's happening and 
gaining more control over your code. If this is the case, you can always explore the
[API](https://api.python.langchain.com/en/latest/api_reference.html)  documentation, deep dive
into the code and familiarize with the logic.

You'll see that many chains we are using (ReduceDocumentsChain, RefineDocumentsChain, etc..)
implement the basic LLMChain, the first chain we learnt about. 

Keep in mind that sometimes you can achieve good results using different types of components
and chains, but is always a good practice to use the most appropriate one to maximixe results
and efficiency.
''')

with st.expander("Exercise Tips"):
    st.write('''
    - Browse [the code on GitHub](https://github.com/francescocarlucci/langchain-summarization/blob/main/app.py) and make sure you understand it.
    - Fork the repository to customize the code.
    - Try to add more chain types (eg. map_rerank) to the select field and see how the behavior changes.
    - If you wanna deep dive into the chains, you can remove "load_summarize_chain" and implement the whole chain manually.
    ''')

st.divider()
