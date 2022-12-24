


import streamlit as st
import base64

from PIL import Image

import streamlit as st


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

col1,col2 = st.columns([1,.5])
with st.container():
    
    with col1:
        x= st.button('Photo')
        if x:
            st.write("hdhdh")

with col2:
    y = st.button("Clear")
    if y:
        st.write("sdsdd")

