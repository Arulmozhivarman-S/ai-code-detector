import streamlit as st
import joblib
from src.preprocess import clean_code
from src.feature_extraction import get_embedding

# Title
st.title("Classify Your Code")

# Load model
model = joblib.load("model.pkl")

# --- Callback function ---
def update_code():
    st.session_state.code_input = st.session_state.code_box

# Initialize session state
if "code_input" not in st.session_state:
    st.session_state.code_input = ""

# Text area (bound to code_box, not code_input!)
st.text_area(
    "Paste your code here:",
    key="code_box",
    value=st.session_state.code_input,
    on_change=update_code,
)

# Prediction button
if st.button("Verify"):
    code = st.session_state.code_box
    if code.strip():
        cleaned = clean_code(code)
        embedded = get_embedding(cleaned)
        result = model.predict([embedded])[0]

        label = "ChatGPT" if result == 1 else "Human"
        st.success(f"Your code is written by: **{label}**")
    else:
        st.warning("Please paste some code before clicking Verify.")
