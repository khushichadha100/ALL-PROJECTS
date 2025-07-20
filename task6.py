import streamlit as st
import os
import subprocess
import tempfile

from langchain.chat_models import ChatOpenAI

# 🔐 Set API key and base
os.environ["OPENAI_API_KEY"] = st.secrets["OPENROUTER_API_KEY"]
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

st.set_page_config(page_title="🧠 Code Generator Agent", layout="wide")
st.title("💻 Generate and Execute Python Code")

# ✅ Secure code execution function
def run_python_code(code: str) -> str:
    forbidden_keywords = ["os.system", "subprocess", "eval(", "exec(", "open(", "import socket", "shutil", "fork"]
    if any(word in code for word in forbidden_keywords):
        return "❌ Unsafe code detected. Execution aborted."

    try:
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".py", delete=False) as tmp_file:
            tmp_file.write(code)
            tmp_file.flush()
            result = subprocess.run(
                ["python", tmp_file.name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=10
            )
            output = result.stdout.decode("utf-8")
            errors = result.stderr.decode("utf-8")
            return output if output.strip() else errors if errors.strip() else "⚠️ No output generated."
    except subprocess.TimeoutExpired:
        return "⏱️ Error: Execution timed out."
    except Exception as e:
        return f"❌ Error while running code: {str(e)}"

# 🤖 Load LLM (no tool/agent this time)
llm = ChatOpenAI(
    temperature=0.3,
    openai_api_key=st.secrets["OPENROUTER_API_KEY"],
    openai_api_base="https://openrouter.ai/api/v1",
    model_name="mistralai/mistral-7b-instruct"
)

# 🎯 User Input
prompt = st.text_area("📝 Enter your prompt (e.g., 'Write Python code to find the factorial of 5')", height=150)

# ▶️ Button to generate and execute code
if st.button("🚀 Generate & Execute"):
    with st.spinner("💬 Generating code..."):
        try:
            # 1. Ask LLM to only return Python code block
            generation_prompt = f"Write only the Python code (no explanation) for this task:\n{prompt}"
            response = llm.predict(generation_prompt)

            # 2. Extract code from markdown block (if any)
            if "```python" in response:
                code = response.split("```python")[1].split("```")[0].strip()
            elif "```" in response:
                code = response.split("```")[1].strip()
            else:
                code = response.strip()

            # 3. Show code
            st.subheader("🧾 Generated Code:")
            st.code(code, language="python")

            # 4. Run code
            st.subheader("✅ Code Output:")
            output = run_python_code(code)
            st.text(output)

        except Exception as e:
            st.error(f"❌ Error: {e}")