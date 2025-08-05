import streamlit as st
from ui import render_mainpage
from ui_about import render_about

# --- Sidebar Navigation ---
st.sidebar.title("🌿 CropsDiagnosis")
st.sidebar.markdown("AI-powered Crops diagnosis")

if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"
if st.sidebar.button("📘 About the Project"):
    st.session_state.page = "About"

page = st.session_state.page

# === Route to Page ===
if page == "Home":
    render_mainpage()
elif page == "About":
    render_about()
