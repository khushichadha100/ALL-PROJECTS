import streamlit as st
from PyPDF2 import PdfReader
import docx2txt
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

st.set_page_config(page_title="Chat with Your Documents", layout="wide")
st.title("📄 Chat with Your Documents (Streamlit Cloud Safe)")

# 1️⃣ Upload multiple files
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

# 2️⃣ Process uploaded documents
if uploaded_files and st.button("Process Documents"):
    raw_text = ""
    for file in uploaded_files:
        raw_text += read_file(file)

    if raw_text.strip() == "":
        st.error("❌ No readable text found in the uploaded files.")
    else:
        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_text(raw_text)

        # CPU-safe embeddings (no HuggingFace or PyTorch GPU issues)
        embeddings = CohereEmbeddings(model="small")
        vector_store = FAISS.from_texts(chunks, embedding=embeddings)

        # Store in session
        st.session_state.vector_store = vector_store
        st.session_state.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        st.success("✅ Documents processed successfully!")

# 3️⃣ Chat interface
question = st.text_input("💬 Ask a question from your documents")

if question and "vector_store" in st.session_state:
    llm = ChatOpenAI(
        temperature=0,
        model_name="mistralai/mistral-7b-instruct"  # works via OpenRouter
    )
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=st.session_state.vector_store.as_retriever(),
        memory=st.session_state.memory
    )
    result = qa_chain.run(question)
    st.markdown("**🧠 Answer:** " + result)
