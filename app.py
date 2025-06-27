import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# app.py

import streamlit as st
from transformers import pipeline
from scripts.summarizer import summarize_text

# —— Page config and style ——
st.set_page_config(
    page_title="📝 AI Text Summarizer",
    page_icon="🤖",
    layout="centered"
)
st.markdown("""
<style>
.main {background-color: #f5f5f5;}
.stApp {max-width: 800px; margin: auto;}
</style>
""", unsafe_allow_html=True)

# —— Title and description ——
st.title("🤖 AI Text Summarizer")
st.write(
    "Paste any long article below, and let our AI give you a concise summary. "
    "Powered by Hugging Face’s BART model."
)

# —— Text input ——
user_input = st.text_area(
    "Enter your long text here:",
    height=250,
    placeholder="Type or paste your article..."
)

# —— Summarize button ——
if st.button("Generate Summary"):
    if not user_input.strip():
        st.error("⚠️ Please enter some text first.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarize_text(user_input)
        st.subheader("📝 Summary:")
        st.write(summary)

# —— Footer ——
st.markdown("---")
st.markdown("Built with ❤️ by Jai’s AI Internship Project")
