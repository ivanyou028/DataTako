# Import necessary libraries and modules
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import openai
from pandasai.middlewares.streamlit import StreamlitMiddleware

# Get API key
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Set page configuration and title for Streamlit
st.set_page_config(page_title="DataTako", page_icon="🐙", layout="wide")

csv_files = []

with st.sidebar:
    # Add header with title and description
    st.markdown(
        '<p style="display:inline-block;font-size:40px;font-weight:bold;">🐙DataTako </p>'
        ' <p style="display:inline-block;font-size:16px;">🐙DataTako is a tool that uses AI-powered '
        'natural language processing to analyze and provide insights on CSV data. Users can '
        'upload CSV files, view the data, and have interactive conversations with the AI model '
        'to obtain valuable information and answers related to the uploaded data <br><br></p>',
        unsafe_allow_html=True
    )
    csv_files = st.file_uploader("Upload your CSV file", type=['csv'], accept_multiple_files=True)

llm = OpenAI(api_token=OPENAI_API_KEY)
pandas_ai = PandasAI(llm, middlewares=[StreamlitMiddleware()], custom_whitelisted_dependencies=["scikit-learn"])

def chat_with_csv(dfs, prompt):
    result = pandas_ai.run(dfs, prompt=prompt, is_conversational_answer=False, show_code=True)
    print(result)
    return result

if not len(csv_files):
    st.spinner("Waiting for input CSV")
else:
    st.toast("CSV Uploaded Successfully", icon='🎉')
    dataframes = [pd.read_csv(file) for file in csv_files]

    tabs = st.tabs([file.name for file in csv_files])
    for i in range(len(tabs)):
        tabs[i].dataframe(dataframes[i])

    input_text = st.text_area("Enter your query")
    if st.button("Chat with CSV"):
        if not input_text:
            st.error('Please provide a question', icon="🚨")
        else:
            result = chat_with_csv(dataframes, input_text)
            st.success(result)
            expander = st.expander("See Code")
            expander.code(pandas_ai.last_code_executed)
        if pandas_ai.last_error:
            st.error(pandas_ai.last_error)
        
# Hide Streamlit header, footer, and menu
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

# Apply CSS code to hide header, footer, and menu
st.markdown(hide_st_style, unsafe_allow_html=True)
