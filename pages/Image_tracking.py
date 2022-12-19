import streamlit as st
import streamlit.components.v1 as components
# container_width = st.get_container_width
screen_width = st.get_screen_width
st.set_page_config(layout="wide")
# embed streamlit docs in a streamlit app
components.iframe("https://sajithjude.github.io/instancy/",width=screen_width, height=None)