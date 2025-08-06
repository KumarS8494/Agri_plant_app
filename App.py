import streamlit as st
from ui import render_mainpage
from ui_about import render_about

st.sidebar.title("🌿 CropsDiagnosis")
st.sidebar.markdown("AI-powered Crops diagnosis")

# --- Equal Width Fix for Sidebar Buttons ---
sidebar_button_style = """
    <style>
    div.stButton > button {
        width: 100% !important;
        text-align: left;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        border-radius: 8px;
    }
    </style>
"""
st.sidebar.markdown(sidebar_button_style, unsafe_allow_html=True)

# --- Session State ---
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- Buttons (vertically stacked) ---
if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"
if st.sidebar.button("📘 About"):
    st.session_state.page = "About"

# --- Route to Page ---
page = st.session_state.page
if page == "Home":
    render_mainpage()
elif page == "About":
    render_about()
