import streamlit as st
from subjectivityFinder import subjectivity

def app():
    st.title('Subjectivity Finder')
    st.write('Please provide the news for which subjectivity needs to be found')
    user_input = st.text_area('Enter news','')
    output = subjectivity(user_input)
    st.write("Subjectivity of the Text: ")
    st.write(output)