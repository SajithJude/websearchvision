import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
# container_width = st.get_container_width
# width = st.javascript('window.screen.width')
st.set_page_config(layout="wide")
image = Image.open('pages/frame.png')

# st.title("Scan the QR code to view the demo")
st.image(image)
st.subheader("To View, open camera on smartphone and scan code")
st.caption("or visit")
st.write("https://sajithjude.github.io/instancy")
st.caption("on smartphone or tablet")

# embed streamlit docs in a streamlit app
# components.iframe("https://sajithjude.github.io/instancy/",height=400)