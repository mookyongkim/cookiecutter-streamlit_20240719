import streamlit as st
from streamlit_option_menu import option_menu

# Define the pages and their file paths
pages = {"Home":"app.py",
         "상황별 대화 만들기":"pages/Create contextual conversations.py",
         "RAG 챗봇":"pages/EmbedChain.py",
         "등산 챗봇":"pages/Mountain_Chat_Bot.py"
}

# Create a list of the page names
page_list = list(pages.keys())

def nav(current_page=page_list[0]):
    with st.sidebar:
        p = option_menu("Page Menu", page_list, 
            default_index=page_list.index(current_page), 
            orientation="vertical")

        if current_page != p:
            st.switch_page(pages[p])
          
