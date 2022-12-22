import streamlit as st
import streamlit.components.v1 as components

placeholder = st.empty()

import streamlit as st
import base64
import requests
import json
import os

st.title("Face Emotion Detection")
st.caption("Point the camera to a persons photo, the face of a real person, or your own face to detect the emotions.​")
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    # st.write(type(bytes_data))
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
    annotation = response_data['responses'][0]['faceAnnotations'][0]
    # Printing the response, in this case it will return all the labels that are 
    # identified in the image
    # def render():

    #     col1, col2, col3 , col4= st.columns(4)

    #     with col1:
    #         st.header("Suprised")
    #         st.write(annotation['surpriseLikelihood'])

    #         # st.image("https://static.streamlit.io/examples/cat.jpg")

    #     with col2:
    #         st.header("In Joy")
    #         st.write(annotation['joyLikelihood'])    


    #         # st.image("https://static.streamlit.io/examples/dog.jpg")

    #     with col3:
    #         st.header("In Sorrow")
    #         st.write(annotation['sorrowLikelihood'])  

    #     with col4:
    #         st.header("In Anger")
    #         st.write(annotation['angerLikelihood']) 

    
    # x = annotation['angerLikelihood']
         



    st.write(st.markdown(
                   f"""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            <div id="accordion">
            <div class="card">
                {annotation}
                
                <!-- <div class="card-header" id="headingOne">
                <h5 class="mb-0">
                    <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                    Collapsible Group Item #1
                    </button>
                </h5>
                </div>
                <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
                <div class="card-body">
                    Collapsible Group Item #1 content
                </div>
                </div> -->
            </div>
            <div class="card">
                <div class="card-header" id="headingTwo">
                <h5 class="mb-0">
                    <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                    Collapsible Group Item #2
                    </button>
                </h5>
                </div>
                <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
                <div class="card-body">
                    Collapsible Group Item #2 content
                </div>
                </div>
            </div>
            </div>
                    """,
                    unsafe_allow_html=True
                ))

# if st.button("Clear me"):
#     placeholder.empty()