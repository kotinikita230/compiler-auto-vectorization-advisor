import streamlit as st
import tempfile
import os

from src.benchmarking.benchmark import benchmark_gcc, benchmark_cpp, benchmark_java, benchmark_python
from src.analysis.loop_detector import detect_loops
from src.analysis.dependency_analysis import is_vectorizable
from src.optimization.suggester import suggest_optimization


# ----------- PAGE CONFIG -----------
st.set_page_config(page_title="Auto Vectorization Advisor", layout="wide")


# ----------- CUSTOM CSS (PRO UI) -----------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}

.block {
    background: linear-gradient(145deg, #111827, #1f2937);
    padding: 20px;
    border-radius: 15px;
    color: white;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}

.title {
    font-size: 32px;
    font-weight: bold;
    color: #22c55e;
}

.subtitle {
    color: #9ca3af;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)


# ----------- TITLE -----------
st.markdown('<div class="title">🚀 Compiler Auto Vectorization Advisor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Analyze loops, execution time & optimization</div>', unsafe_allow_html=True)


# ----------- FILE UPLOAD -----------
uploaded_file = st.file_uploader("Upload your code (.c, .cpp, .java, .py)")


def detect_language(file_name):
    if file_name.endswith(".c"):
        return "C"
    elif file_name.endswith(".cpp"):
        return "C++"
    elif file_name.endswith(".java"):
        return "Java"
    elif file_name.endswith(".py"):
        return "Python"
    return "Unknown"


if uploaded_file:
    file_ext = uploaded_file.name
    language = detect_language(file_ext)

    # Save temp file
    file_path = os.path.join("temp", uploaded_file.name)

    os.makedirs("temp", exist_ok=True)

    with open(file_path, "wb") as f:
     f.write(uploaded_file.read())  

    # Read code
    with open(file_path, "r") as f:
        code = f.read()

    # ----------- BENCHMARK -----------
    time_taken = None
    output = ""

    if language == "C":
        time_taken, output = benchmark_gcc(file_path)

    elif language == "C++":
        time_taken, output = benchmark_cpp(file_path)

    elif language == "Java":
        time_taken, output = benchmark_java(file_path)

    elif language == "Python":
        time_taken, output = benchmark_python(file_path)

    else:
        output = "Execution not supported for this language"

    # ----------- TOP CARDS -----------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f'<div class="block">💻<br>{language}</div>', unsafe_allow_html=True)
    
    with col2:
       
     if time_taken is not None:
      time_display = f"{time_taken:.4f} sec"
     else:
      time_display = "Error"

    st.markdown(f'<div class="block">⚡<br>{time_display}</div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="block">📊<br>Analysis Ready</div>', unsafe_allow_html=True)

    st.divider()

    # ----------- OUTPUT SECTION -----------
    st.subheader("📤 Program Output")

    if time_taken is None:
      st.error(output)   # shows compilation/runtime error
    else:
     st.code(output)

    st.divider()

    # ----------- LOOP ANALYSIS -----------
    st.subheader("🔍 Loop Analysis")

    loops = detect_loops(code)

    if not loops:
        st.warning("No loops detected")
    else:
        for i, loop in enumerate(loops, 1):
            st.markdown(f"### Loop {i}")
            st.code(loop["line"])

            vectorizable = is_vectorizable(loop)

            st.write("**Vectorizable:**", "YES" if vectorizable else "NO")

            suggestions = suggest_optimization(loop, vectorizable)

            st.write("**Suggestions:**")
            for s in suggestions:
                st.write("•", s)