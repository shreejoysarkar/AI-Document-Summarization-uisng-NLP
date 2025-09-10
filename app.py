import streamlit as st
import time
from src.DocSummarizer.pipeline.prediction import PredictionPipeline
import PyPDF2
import docx
from PIL import Image

# Inject custom CSS for background image
# ...existing code...

st.markdown(
    """
    <style>
    body {
        background-image: url("https://i.pinimg.com/1200x/aa/68/b9/aa68b9419cb9c664559259f150ca6009.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stApp {
        background: transparent;
    }
    /* Solid light dark blue background for expanders */
    .stExpander {
        background: rgba(40, 60, 120, 0.85); /* light dark blue */
        border-radius: 16px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.12);
        padding: 16px;
    }
    /* Solid light dark blue background for text area */
    textarea {
        background: #2a3c78 !important; /* light dark blue */
        color: #fff !important;
        border-radius: 8px !important;
    }
    /* Solid light dark blue background for file uploader */
    .stFileUploader {
        background: #2a3c78 !important; /* light dark blue */
        color: #fff !important;
        border-radius: 8px !important;
        padding: 8px;
    }
    /* Change label color for better contrast */
    label, .stExpanderHeader {
        color: #fff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ...existing code...
st.set_page_config(page_title="AI Document Summarizer", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4F46E5;'>📄 AI Document Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4F46E5'>Upload a PDF/Word file or enter text to get a summary.</p>", unsafe_allow_html=True)

# Text input
with st.expander("Summarize Text", expanded=True):
    text_input = st.text_area("Enter text to summarize", height=200)
    if st.button("Summarize Text"):
        if text_input.strip():
            with st.spinner("Summarizing..."):
                obj = PredictionPipeline()
                summary = obj.predict(text_input)
            st.success("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text.")

# File upload
with st.expander("Summarize File", expanded=True):
    uploaded_file = st.file_uploader("Upload PDF or Word file", type=["pdf", "docx"])
    if uploaded_file is not None:
        if st.button("Summarize File"):
            file_type = uploaded_file.name.split('.')[-1]
            text = ""
            if file_type == "pdf":
                reader = PyPDF2.PdfReader(uploaded_file)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
            elif file_type == "docx":
                doc = docx.Document(uploaded_file)
                text = "\n".join([para.text for para in doc.paragraphs])
            else:
                st.error("Unsupported file type.")
            if text.strip():
                with st.spinner("Summarizing..."):
                    obj = PredictionPipeline()
                    summary = obj.predict(text)
                st.success("Summary:")
                st.write(summary)
            else:
                st.warning("No text found in the file.")

# Refresh button
if st.button("🔄 Refresh"):
    st.query_params["dummy"] = str(time.time())