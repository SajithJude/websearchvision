import streamlit as st
import streamlit.components.v1 as components
# container_width = st.get_container_width
width = st.javascript('window.screen.width')
st.set_page_config(layout="wide")
# embed streamlit docs in a streamlit app
components.iframe("https://sajithjude.github.io/instancy/",width=width, height=None)