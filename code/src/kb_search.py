from datasets import load_dataset
import streamlit as st
from dotenv import load_dotenv
import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.llms import OpenAI

# load environment variables 
load_dotenv()

# Load Banking Knowledge Base dataset
@st.cache_data
def load_kb():
    dataset = load_dataset("banking77", 
                           split="train")  # Banking-related dataset
    docs = [item["text"] for item in dataset]   

    return docs

# AI Agent for KB Search using LangChain
def search_kb(query):

    open_api_key = os.getenv("OPENAI_API_KEY")
    embeddings = OpenAIEmbeddings(open_api_key = open_api_key)  # Load OpenAI embeddings
    vectorstore = FAISS.load_local("./faiss_index"
                                   , embeddings,
                                   allow_dangerous_deserialization=True)  # Load FAISS index
    docs = vectorstore.similarity_search(query, k=3)
    retrieved_texts = "\n".join([doc.page_content for doc in docs])

    # 
    llm = OpenAI(model="gpt-3.5-turbo", 
                 open_api_key=open_api_key)  # Use GPT model of choice
    
    response = llm.predict(f"Based on the following knowledge base, answer the query:\n\n{retrieved_texts}\n\nQuery: {query}")

    return response

