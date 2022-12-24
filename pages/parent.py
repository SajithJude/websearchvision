


import streamlit as st
import base64

from PIL import Image

import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

# @st.cache(allow_output_mutation=True)



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
     # body 
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
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
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

def body():
    myargs = [
        "Home ",
        
        image("images.png",style=styles( position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="#192A56",
        text_align="center",
        height="auto",
        opacity=1)),
        br(),
    ]
    layout(*myargs)

def footer():
    myargs = [
        "Made with ❤️ from ",
        
        link("www.instancy.com","Instancy Inc"),
        br(),
    ]
    layout(*myargs)


if __name__ == "__main__":
    

#     im = Image.open("images.png")
#     st.set_page_config(
#         page_title="Instancy",
#         page_icon=im,
#         layout="wide",
#     )
#     # st.set_theme('primary_color', primary_color='#BFD731')
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.write('     ')

#     with col2:
#         st.title("Home")

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
    body()
    # st.write("www.instancy.com")
    footer()






