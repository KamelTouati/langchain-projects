import re
import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

st.set_page_config(
    page_title="WordPress Code Assistant | Learn LangChain",
    page_icon="🤓"
)

st.header('🤓 WordPress Code Assistant')

st.subheader('Learn LangChain | Demo Project #4')

st.success("This is a demo project related to the [Learn LangChain](https://learnlangchain.org/) mini-course.")

st.write('''
In this project we will use some core LangChain components (Chains, PromptTemplates), to achieve
a powerful outcome: a WordPress code assistant capable to handle real development tasks.
It's inspired by an AI-assisted code technique I use in my own development projects.
''')

st.write('''
The whole approach is based on the Divide and Conquer algorithm: solve a problem by dividing it
into smaller sub-problems, solving the sub-problems and combining the solutions to succesfully
complete the initial task. Let's see an example related to WordPress with a medium complexity:
''')

with st.expander("Send a daily welcome message in BuddyPress to newly registered users"):
    st.write('''
    The main task can be broken in the following sub-tasks:
    - When a new user activates his account in BuddyBoss, add a custom user metadata containing
    the key "to_welcome".
    - Write a function to send a private BuddyBoss message to a specific user by ID,the message content
    should be customizable as a variable. Name the function "wca_send_private_message".
    - Create a WordPress user query that retrieves all the user Ids with the "to_welcome" usermeta,
    runs a send_private_message($user_id) function to each user and deletes the "to_welcome" metadata.
    Wrap it in a function called bulk_welcome_users().
    - add a daily cron event which invokes bulk_welcome_users() using WP cron.

    Try to pass each command to the LLM as Custom prompt below, and the code provided should
    be suitable to implement a system that sends a daily welcome message in BuddyPress to
    newly registered users.
    ''')

st.info("You need your own keys to run commercial LLM models.\
    The form will process your keys safely and never store them anywhere.", icon="🔒")

st.write('''
With this form, you can ask your WordPress Code Assistant to perform some demo tasks for you,
or select custom and provide a customized one. With the checkboxes you can run a "control"
chain or display the full thinking process of the LLM.
''')

openai_key = st.text_input("OpenAI Api Key", help="You need an account on OpenAI to generate a key: https://openai.com/blog/openai-api")

model = st.selectbox(
	'Select a model',
	(
		'gpt-3.5-turbo',
		'gpt-4'
	),
	help="Make sure your account is elegible for GPT4 before using it"
)

task = st.selectbox(
	'Select a sample WordPress task',
	(
		'Store Contact Form 7 submissions as WordPress custom post types',
		'Append a text signature to all Gravity Forms email notifications',
		'Add a custom text field to WooCommerce products in backend',
		'After a WooCommerce order is created, send the order data to a 3rd party via API',
		'Create a function to filter the WP search result and only include posts containing the metakey "indexable"',
		'Custom'
	)
)

with st.form("code_assistant"):

	custom_task = st.text_input("Write your custom task (available if Selected Task is Custom)", disabled=(task != "Custom"))

	thinking = st.checkbox('Display the full thinking process')

	cross_check = st.checkbox('Execute an additional chain to cross-check the code provided')

	execute = st.form_submit_button("🚀 Generate Code")

	if execute:

		with st.spinner('Generating code for you...'):

			llm = ChatOpenAI(openai_api_key=openai_key, temperature=0, model_name=model)

			code_prompt = ChatPromptTemplate.from_template('''
			You are a Senior WordPress developer. Your job is to help me writing the best code
			to achieve the following: {task}
			Please make sure to enclose the PHP code in <?php ... ?> and describe your thinking
			proccess in detail.
			''')

			code_chain = LLMChain(llm=llm, prompt=code_prompt)

			if task == "Custom":
				task = custom_task

			code_response = code_chain.run(task)

			# NOTE possible improvement usgin langchain.output_parsers.regex.RegexParser
			#code_matches = re.findall(r'<\?php.*?\?>', code_response, re.DOTALL)
			code_matches = re.findall(r'```php(.*?)```', code_response, re.DOTALL)

			full_code = []
			
			for code in code_matches:

				if len(code) > 20:

					st.code(code, language="php")

					full_code.append(code)

			if thinking:

				st.subheader('Thinking process:')

				st.write(code_response)


			if cross_check and full_code:

				check_prompt = ChatPromptTemplate.from_template('''
				You are a Senior QA Tester. Your job is to make sure that the collowing code:
				{code} is suitable to achieve the following task: {task}
				If the code is good and suitable, just answer "SUCCESS, the code is good for this task".
				If the code is not good for any reason, answer "ERROR" and explain why in detail.
				''')

				check_chain = LLMChain(llm=llm, prompt=check_prompt)

				check_response = check_chain.run({"code":' '.join(full_code), "task":task})

				st.subheader('QA on provided code')

				st.write(check_response)

with st.expander("Exercise Tips"):
    st.write('''
    This demo is probably the most interesting one to expand and improve:
    - Browse [the code on GitHub](https://github.com/francescocarlucci/wordpress-code-assistant/blob/main/app.py) and make sure you understand it.
    - Fork the repository to customize the code.
    - If you are creating code or WordPress plugin giving multiple prompts, adding memory to the LLM can be a huge improvement. Try it!
    - Brave improvement: add another step to the chain and try to use a LLM to handle the initial task breakdown.
    ''')

st.subheader('A note on the cross-check chain')

st.write('''
While is true that most of the times the check will pass if we have a well writen and specific prompt
task, this feature is very helpful to handle LLM hallucinations and bad code in response to poorly
written prompts. Plus, you can try to plug in a different LLM to test the code making the whole system
more reliable.
''')

st.divider()
