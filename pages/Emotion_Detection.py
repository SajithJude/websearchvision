import streamlit as st
import base64
import requests
import json
import os

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
    

    # The GCP Vision API URL 
    vision_url = 'https://vision.googleapis.com/v1/images:annotate?key='

    # Your Google Cloud Platform (GCP) API KEY. Generate one on cloud.google.com
    api_key = os.environ["API_KEY"] 
    # Load your image as a base64 encoded string


    
    encoded_image = base64.b64encode(img_file_buffer.read())

    # Generate a post request for GCP vision Annotation
    json_data= {
        'requests': [
            {
                'image':{
                    'content': encoded_image.decode('utf-8')
                },
                'features':[
                    {
                        'type':'FACE_DETECTION',
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
    annotation = response_data['response_data'][0]['faceAnnotations'][0]
    # Printing the response, in this case it will return all the labels that are 
    # identified in the image
    st.write("Suprised :")
    st.write(annotation['surpriseLikelihood'])
    st.write("Joy :")
    st.write(annotation['joyLikelihood'])    
    st.write("Sorrow :")
    st.write(annotation['sorrowLikelihood'])        
    # st.write(json.dumps(response_data, indent=4))