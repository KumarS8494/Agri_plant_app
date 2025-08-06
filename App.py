import streamlit as st
from ui import render_mainpage
from ui_about import render_about

st.sidebar.title("🌿 CropsDiagnosis")
st.sidebar.markdown("AI-powered Crops diagnosis")

st.sidebar.markdown("""
    <style>
    .stButton > button {
        width: 100% !important;
        padding: 0.6rem 1rem;
        font-size: 16px;
        font-weight: 600;
        border-radius: 8px;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)
# --- Initialize Session State ---
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- Sidebar Navigation ---
if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"

if st.sidebar.button("📘 About the Project"):
    st.session_state.page = "About"

# --- Route to Page ---
page = st.session_state.page
if page == "Home":
    render_mainpage()
elif page == "About":
    render_about()
