import streamlit as st
import base64
import requests
import json
import os

cam = st.radio('Please select an option',('Open Webcam', 'Upload Image'))
# upload = st.checkbox('Upload an Image')

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
    response = requests.post(vision_url+api_key, json=json_data)

    # Read the response in json format
    response_data = response.json()

    return response_data



if cam =='Open Webcam':
    img_file_buffer = st.camera_input("Take a picture")
    if img_file_buffer is not None:
        encoded_image = base64.b64encode(img_file_buffer.read())
        result = callAPI(encoded_image)
        st.write("Detected Text Results from Web Camera")
        st.write(result)
        # The GCP Vision API URL 
        

else:
    img = st.file_uploader("Click to Upload an Image")
    encoded_image = base64.b64encode(img.read())
    result = callAPI(encoded_image)
    st.write("Detected Text Results From uploaded Image")
    st.write(result)
    

