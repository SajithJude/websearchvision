# python code to draw bounding boxes on Google Cloud vision text_detection api images streamlit.

import streamlit as st
import io
from PIL import Image
import matplotlib.pyplot as plt
import requests
import json
import os
import base64


#@st.cache 

def draw_bbox(image):    
    API_KEY = os.environ["API_KEY"] 

    URL = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(API_KEY)
    headers = {'Content-Type': 'application/json'}

    # make image data
    # image_data = b64_to_imagebytes(image)
    image_data = base64.b64encode(image.read())


    # construct request body
    body = {
        'requests': [
            {
                'image': {
                    'content': image_data.decode('utf-8')
                },
                'features': [
                    {
                        'type': 'TEXT_DETECTION' 
                    }
                ]
            }
        ]
    }

    # send request
    response = requests.post(URL, data=json.dumps(body), headers=headers)
    response = json.loads(response.text)

    # extract bounding box points
    x, y, width, height = [], [], [], []
    # if 'fullTextAnnotation' in response['responses'][0]:
    for i in response['responses'][0]['textAnnotations'][1:]:
        vertices = i['boundingPoly']['vertices']
        x.append(vertices[0]['x'])
        y.append(vertices[0]['y'])
        width.append(vertices[3]['x'] - vertices[0]['x'])
        height.append(vertices[3]['y'] - vertices[0]['y'])
    
    # draw Bounding box
    fig, ax = plt.subplots(figsize=(10,10))
    ax.imshow(plt.imread(image))
    for idx in range(len(x)):
        rect = patches.Rectangle((x[idx], y[idx]), width[idx], height[idx], linewidth=1, edgecolor='r',facecolor='none')
        ax.add_patch(rect)
        plt.axis('off')
    plt.tight_layout()
    return fig

st.title('Draw Bounding Box on Images') 
uploaded_file = st.file_uploader("Choose an image: ", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    bboxed_image = draw_bbox(uploaded_file)
    st.pyplot()