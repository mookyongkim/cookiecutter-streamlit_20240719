import streamlit as st
import navbar

current_page = "Page 1"
st.title("Page 1")
navbar.nav(current_page)
st.write("This is a dummy page for {{ cookiecutter.project_slug }}.")
