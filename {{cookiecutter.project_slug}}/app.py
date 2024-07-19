import streamlit as st
import navbar

st.set_page_config(layout="wide")
st.header("Multipage navigation")

# Display the menu
navbar.nav("Home")

st.markdown("""
            This app is a demonstrator of programmatically selecting a page in a multipage app.
            
            The pages display GDP data for countries or continents. The data is bundled with Plotly
            and originates from the Gapminder Foundation.
            """)            



st.markdown("[![Click me](app/static/images/welcome.png)](https://streamlit.io)")
st.markdown("""
<table>
    <tr>
        <td>제목</td>
    </tr>
    <tr>
        <td>바람과 함께 사라지다.</td>
    </tr>
</table>
""", unsafe_allow_html=True)

st.markdown("[![Click me](app/static/images/welcome.png)](https://streamlit.io)")


#import streamlit as st
#
#
#if "y" == 'y':
#    from src.components import sidebar
#    sidebar.show_sidebar()
#
#st.title('streamlit_apps')
#st.write('This is my awesome streamlit app.')
