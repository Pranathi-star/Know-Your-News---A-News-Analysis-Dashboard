import streamlit as st
import spacy
import spacy_transformers
from spacytextblob.spacytextblob import SpacyTextBlob

@st.cache_data
def subjectivity(text):
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob')
    doc = nlp(text)
    if doc._.subjectivity > 0.5:
        return "Highly Opinionated sentence"
    elif doc._.subjectivity < 0.5:
        return "Less Opinionated sentence"
    else:
        return "Neutral sentence"