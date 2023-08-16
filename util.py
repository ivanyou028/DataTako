import os.path
from pathlib import Path
import pandas as pd
from tqdm import tqdm
from langchain.document_loaders import (
    TextLoader,
    UnstructuredPDFLoader,
    UnstructuredWordDocumentLoader,
)
from langchain.text_splitter import CharacterTextSplitter

def load_df(uploaded_file, suffix=None):
    if not suffix: suffix = uploaded_file.name.split(".")[-1] 
    if 'xlsx' == suffix:
        data = pd.read_excel(uploaded_file)
    elif 'csv' == suffix:
        data = pd.read_csv(uploaded_file)
    elif 'json' == suffix:
        data = pd.read_json(uploaded_file)
    elif 'txt' == suffix:
        data = TextLoader(str(uploaded_file)).load()
        text_splitter = CharacterTextSplitter(separator='\n', chunk_size=256, chunk_overlap=0)
        texts = text_splitter.split_documents(data)
        data = texts
    # elif suffix in ('.docx', '.doc'):
    #     data = UnstructuredWordDocumentLoader(str(data_path), mode='elements').load()
    # elif '.pdf' == suffix:
    #     data = UnstructuredPDFLoader(str(data_path), mode="elements").load()
    else:
        raise NotImplementedError
    return data