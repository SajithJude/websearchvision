


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
            font-size:80px;
            color:#000000;
            border-radius:20px 20px 20px 20px; 
        }
        div.stButton > button:hover {
            background-color: #EBEBEB;
            color:#ffffff;
            }


        
        </style>""", unsafe_allow_html=True)
# @st.cache(allow_output_mutation=True)


col1,col2 ,col3= st.columns([1,1,1])
with col1:
    x= st.button('Photo')
    if x:
        st.write("hdhdh")

with col2:
    y = st.button("Clhhhear")
    if y:
        st.write("sdsdd")
with col3:
    d = st.button("Clear")
    if d:
        st.write("sdsdd")


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; } 
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="#192A56",
        text_align="center",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px("auto", "auto", "auto", "auto"),
        border_style="insert",
        border_width=px(1)
    )

    body = div(
       
        style=styles(
        color="#192A56",
        text_align="center",
        opacity=1
    )

    )
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    
    st.markdown(str(foot), unsafe_allow_html=True)
    


def footer():
    

    myargs = [
        
        # with open('footer_st_logo.png', 'rb') as f:
        #     img_logo = f.read()
        # im =  Image.open("images.png")
        br(),
        # st.image(im),

        br(),
        link("www.instancy.com","Instancy Inc"),
        br(),
    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()
    # st.set_page_config( layout="centered")
    # wid
    

#     with col3:
#         st.write('     ')

#     cols1, cols2, cols3 = st.columns(3)

#     with cols1:
#         st.write(' ')

#     with cols2:
#         st.image(im)


#     with cols3:
#         st.write(' ') 




#     st.subheader(
#         """
# Augmented Reality Demos
#         """
#     )

    


#     st.caption(
#     """
#     Click on the Menu to select an augmented reality Scenario.
#     """
# )
    # body()
    # st.write("www.instancy.com")
    






