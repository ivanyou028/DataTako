# Import necessary libraries and modules
import streamlit as st
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import openai
from pandasai.middlewares.streamlit import StreamlitMiddleware
from util import load_df

# Get API key
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

# Set page configuration and title for Streamlit
st.set_page_config(page_title="DataTako", page_icon="🐙", layout="wide")

data_files = []

def chat_with_data(dfs, prompt, pandas_ai):
    result = pandas_ai.run(dfs[0] if len(dfs) == 1 else dfs, prompt=prompt, is_conversational_answer=False, show_code=True)
    print(result)
    return result

with st.sidebar:
    # Add header with title and description
    st.markdown(
        '<p style="display:inline-block;font-size:40px;font-weight:bold;">🐙DataTako </p>'
        ' <p style="display:inline-block;font-size:16px;">🐙DataTako is a tool that uses AI-powered '
        'natural language processing to analyze and provide insights on structured data. You can '
        'upload files, view the data, and have interactive conversations with the AI model '
        'to understand the data. </p>',
        unsafe_allow_html=True
    )
    st.divider()
    if not OPENAI_API_KEY:
        OPENAI_API_KEY = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password", placeholder="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    data_files = st.file_uploader("Upload your data file", type=['csv', 'xlsx', 'json', 'txt'], accept_multiple_files=True)

if not len(data_files):
    pass
else:
    st.toast("File Uploaded Successfully", icon='🎉')
    dataframes = [load_df(file) for file in data_files]

    tabs = st.tabs([file.name for file in data_files])
    for i in range(len(tabs)):
        tabs[i].dataframe(dataframes[i])

    input_text = st.text_area("Enter your query")
    if st.button("Chat with your data"):
        if not input_text:
            st.error('Please provide a question', icon="🚨")
        else:
            openai.api_key = OPENAI_API_KEY
            llm = OpenAI(api_token=OPENAI_API_KEY)
            pandas_ai = PandasAI(llm, middlewares=[StreamlitMiddleware()], custom_whitelisted_dependencies=["scikit-learn"])
            result = chat_with_data(dataframes, input_text, pandas_ai)
            st.success(result)
            expander = st.expander("See Code")
            expander.code(pandas_ai.last_code_executed)
        if pandas_ai.last_error:
            st.error(pandas_ai.last_error)
        
# Hide Streamlit header, footer, and menu
hide_st_style = """
    <style>
    footer {visibility: hidden;}
    </style>
"""

# Apply CSS code to hide header, footer, and menu
st.markdown(hide_st_style, unsafe_allow_html=True)
