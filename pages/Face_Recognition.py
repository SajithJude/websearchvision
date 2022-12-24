# import streamlit as st
# import streamlit.components.v1 as components

# placeholder = st.empty()

# import streamlit as st
# import base64
# import requests
# import json
# import os

# st.title("Face Emotion Detection")
# st.caption("Point the camera to a persons photo, the face of a real person, or your own face to detect the emotions.​")
# img_file_buffer = st.camera_input("Take a picture")

# if img_file_buffer is not None:
#     # To read image file buffer as bytes:
#     bytes_data = img_file_buffer.getvalue()
#     # Check the type of bytes_data:
#     # Should output: <class 'bytes'>
#     # st.write(type(bytes_data))
#     # The GCP Vision API URL 
#     vision_url = 'https://vision.googleapis.com/v1/images:annotate?key='

#     # Your Google Cloud Platform (GCP) API KEY. Generate one on cloud.google.com
#     api_key = os.environ["API_KEY"] 
#     # Load your image as a base64 encoded string
#     encoded_image = base64.b64encode(img_file_buffer.read())

#     # Generate a post request for GCP vision Annotation
#     json_data= {
#         'requests': [
#             {
#                 'image':{
#                     'content': encoded_image.decode('utf-8')
#                 },
#                 'features':[
#                     {
#                         'type':'FACE_DETECTION',
#                         'maxResults':5
#                     }
#                 ]
#             }
#         ]
#     }

#     # Handle the API request
#     response = requests.post(vision_url+api_key, json=json_data)

#     # Read the response in json format
#     response_data = response.json()
#     annotation = response_data['responses'][0]['faceAnnotations'][0]
#     # Printing the response, in this case it will return all the labels that are 
#     # identified in the image
#     # def render():

#     #     col1, col2, col3 , col4= st.columns(4)

#     #     with col1:
#     #         st.header("Suprised")
#     #         st.write(annotation['surpriseLikelihood'])

#     #         # st.image("https://static.streamlit.io/examples/cat.jpg")

#     #     with col2:
#     #         st.header("In Joy")
#     #         st.write(annotation['joyLikelihood'])    


#     #         # st.image("https://static.streamlit.io/examples/dog.jpg")

#     #     with col3:
#     #         st.header("In Sorrow")
#     #         st.write(annotation['sorrowLikelihood'])  

#     #     with col4:
#     #         st.header("In Anger")
#     #         st.write(annotation['angerLikelihood']) 

    
#     # x = annotation['angerLikelihood']
         


import streamlit as st
import base64

from PIL import Image

import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

# @st.cache(allow_output_mutation=True)
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_png_as_page_bg(png_file):
# #     bin_str = get_base64_of_bin_file(png_file)
# #     page_bg_img = '''
# #     <style>
# #     body {
# #     background-image: url("data:image/png;base64,%s");
# #     background-size: cover;
# #     }
# #     </style>
#     ''' % bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return



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


def footer():
    myargs = [
        "Made with ❤️ from ",
        
        link("www.instancy.com","Instancy Inc"),
        br(),
    ]
    layout(*myargs)


if __name__ == "__main__":
    

    im = Image.open("images.png")
    st.set_page_config(
        page_title="Instancy",
        page_icon=im,
        layout="wide",
    )
    # st.set_theme('primary_color', primary_color='#BFD731')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write('     ')

    with col2:
        st.title("Home")

    with col3:
        st.write('     ')

    cols1, cols2, cols3 = st.columns(3)

    with cols1:
        st.write(' ')

    with cols2:
        st.image('https://cdn-apinb.nitrocdn.com/LGFQTZTBRQFYZkDHnBAkeTYvUEPBCNKO/assets/static/optimized/rev-f886686/wp-content/uploads/2022/11/logo-instancy.png')


    with cols3:
        st.write(' ') 




    st.subheader(
        """
Augmented Reality Demos
        """
    )

    


    st.caption(
    """
    Click on the Menu to select an augmented reality Scenario.
    """
)

    # st.write("www.instancy.com")
    footer()






