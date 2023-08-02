import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Dataset explorer",
    layout="wide",
    initial_sidebar_state="collapsed"
)
 
# Add Title
st.title("Dataset Explorer")

# add sidebar 
st.sidebar.title('Settings')
uploaded_file = st.sidebar.file_uploader('CSV file loader')

# Import your data
df = pd.DataFrame()

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
 
# Generate the HTML using Pygwalker
pyg_html = pyg.walk(df, return_html=True)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)