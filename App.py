import streamlit as st
from ui import render_mainpage
from ui_about import render_about

# --- Apply Sidebar-Specific Button CSS ---
st.sidebar.markdown("""
    <style>
    [data-testid="stSidebar"] button {
        width: 100% !important;
        padding: 0.75rem 1rem !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        margin-bottom: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar UI ---
st.sidebar.markdown("## 🌿 CropsDiagnosis")
st.sidebar.markdown("AI-powered Crops diagnosis")

if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"
if st.sidebar.button("📘 About the Project"):
    st.session_state.page = "About"

# --- Page Routing ---
if st.session_state.page == "Home":
    render_mainpage()
elif st.session_state.page == "About":
    render_about()
