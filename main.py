import streamlit as st
from multiapp import MultiApp
# import your app modules here
from apps import paraphraseApp, summarizeApp, fakeNewsApp, subjectivityApp

app = MultiApp()

st.markdown("""
# Know Your News

Know Your News Web Application provides three services - News Paraphrasing, News Summarizing and Fake News Detection.

""")

# Add all your application here
app.add_app("Paraphraser", paraphraseApp.app)
app.add_app("Summarizer", summarizeApp.app)
app.add_app("Fake News Detector", fakeNewsApp.app)
app.add_app("Subjectivity Finder", subjectivityApp.app)
# The main app
app.run()
