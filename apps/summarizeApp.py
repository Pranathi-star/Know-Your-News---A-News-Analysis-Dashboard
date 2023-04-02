import streamlit as st
from summarizer import text_summarize

def app():
    st.title('Summarizer')
    st.write('Please provide the news article to be summarized:')
    user_input = st.text_area('Enter text','')
    print(user_input)
    output = text_summarize(user_input)
    st.write("Text Summary: ")
    st.write(output)