


import streamlit as st
import base64

from PIL import Image

import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

m = st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #BFD731;
            font-weight: 400;
            width=100px
            font-size:80px;
            color:#000000;
            border-radius:20px 20px 20px 20px; 
        }
        div.stButton > button:hover {
            background-color: #EBEBEB;
            color:#ffffff;
            }
        
        .css-184ep1k {
            flex-direction : row;
        }

        
        </style>""", unsafe_allow_html=True)
# @st.cache(allow_output_mutation=True)


col1,col2 = st.columns([0.5,3])
with col1:
    x= st.button('Photo')
    if x:
        st.write("hdhdh")

with col2:
    y = st.button("Clear")
    if y:
        st.write("sdsdd")

