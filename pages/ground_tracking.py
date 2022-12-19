import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
# container_width = st.get_container_width
# width = st.javascript('window.screen.width')
st.set_page_config(layout="wide")
image2 = Image.open('pages/ground.png')

st.title("Scan the QR code to view the Ground Tracking Demo")
st.image(image2)
# embed streamlit docs in a streamlit app
# components.iframe("https://sajithjude.github.io/instancy/",height=400)