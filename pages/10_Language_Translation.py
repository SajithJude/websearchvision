import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb
from googletrans import Translator
import base64

def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)

def callAPI(image):
    vision_url = 'https://vision.googleapis.com/v1/images:annotate?key='

    # Your Google Cloud Platform (GCP) API KEY. Generate one on cloud.google.com
    api_key = os.environ["API_KEY"] 
    # Load your image as a base64 encoded string

    # Generate a post request for GCP vision Annotation
    json_data= {
        'requests': [
            {
                'image':{
                    'content': image.decode('utf-8')
                },
                'features':[
                    {
                        'type':'TEXT_DETECTION',
                        'maxResults':5
                    }
                ]
            }
        ]
    }

    # Handle the API request
    responses = requests.post(vision_url+api_key, json=json_data)

    # Read the response in json format

    return responses.json()

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
        color="black",
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
    translator = Translator()
    api_key = os.environ["API_KEY"] 

    cam = st.radio('Please select an option',('Open Webcam', 'Upload Image'))
    if cam =='Open Webcam':
        img_file_buffer = st.camera_input("Take a picture")
        if img_file_buffer is not None:
            encoded_image = base64.b64encode(img_file_buffer.read())
            result = callAPI(encoded_image)
            try:
                info = result['responses'][0]['textAnnotations'][0]['description']
                st.image(img_file_buffer)
                st.caption("Text Recognized")
                st.write(info)
                translated_text = translator.translate(info, dest='<tam>').info
                st.write(translated_text)
                # st.write("""
                # #API response Body
                # """)
                # st.write(result) 


            except: 
                st.write("An exception occurred")
                # st.write("##API response Body")
                # st.write(result) 
            

    else:
        img = st.file_uploader("Click to Upload an Image")
        if img is not None:
            encoded_image = base64.b64encode(img.read())
            result = callAPI(encoded_image)
            try:
                info = result['responses'][0]['textAnnotations'][0]['description']
                st.image(img)
                st.caption("Text Recognized")
                st.write(info)

            except: 
                st.write("An exception occurred")

    footer()