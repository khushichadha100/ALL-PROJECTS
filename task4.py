import streamlit as st
import PyPDF2
from PyPDF2 import PdfReader
import docx2txt
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os

# ✅ Set OpenRouter API config using Streamlit secrets
import streamlit as st
import os

# 🔐 Load secrets safely
api_key = st.secrets.get("OPENROUTER_API_KEY", None)

if not api_key:
    st.error("❌ OPENROUTER_API_KEY not found in secrets!")
else:
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"



st.set_page_config(page_title="Chat with Your Documents using RAG", layout="wide")
st.title("📄 Chat with Your Documents using RAG")

# 1. Upload multiple files
uploaded_files = st.file_uploader(
    "Upload your PDF, DOCX, or TXT files",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

# Function to read file content
def read_file(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""

# 2. Process uploaded documents
if uploaded_files and st.button("Process Documents"):
    raw_text = ""
    for file in uploaded_files:
        raw_text += read_file(file)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(raw_text)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    st.session_state.vector_store = vector_store
    st.session_state.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    st.success("✅ Documents processed !")

# 3. Chat interface
question = st.text_input("💬 Ask a question from your documents")

if question and "vector_store" in st.session_state:
    # Setup OpenRouter-compatible LLM
    llm = ChatOpenAI(
        temperature=0,
        openai_api_key=st.secrets["OPENROUTER_API_KEY"],
        openai_api_base="https://openrouter.ai/api/v1",
        model_name="mistralai/mistral-7b-instruct"  # ✅ Use chat-compatible model
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=st.session_state.vector_store.as_retriever(),
        memory=st.session_state.memory
    )

    result = qa_chain.run(question)
    st.markdown("**🧠 Answer:** " + result)
