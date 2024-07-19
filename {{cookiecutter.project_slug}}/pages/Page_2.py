import streamlit as st
import navbar

current_page = "Page 2"
st.title("Page 2")
navbar.nav(current_page)
st.write("This is a dummy page for {{ cookiecutter.project_slug }}.")
