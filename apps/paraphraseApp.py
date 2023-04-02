import streamlit as st
from paraphraser import text_paraphrase

def app():
    st.title('Paraphraser')
    st.write('Please provide the news to be paraphrased')
    user_input = st.text_area('Enter news','')
    output = text_paraphrase(user_input)
    st.write("Paraphrased Text: ")
    st.write(output)