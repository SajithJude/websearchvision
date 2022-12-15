import streamlit as st
import base64
import requests
import json
import os
import openai
import os

st.title('Scan Image and fetch information')
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
                        'type':'WEB_DETECTION',
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


if cam =='Open Webcam':
    img_file_buffer = st.camera_input("Take a picture")
    if img_file_buffer is not None:
        encoded_image = base64.b64encode(img_file_buffer.read())
        result = callAPI(encoded_image)
        try:
            # info = result['responses'][0]['textAnnotations'][0]['description']
            # st.image(img_file_buffer)
            # st.write("Detected Text Results From Web camera snapshot")
            # st.write(info)
            st.write("""
            #API response Body
            """)
            st.write(result) 


        except: 
            st.write("An exception occurred")
            st.write("##API response Body")
            st.write(result) 
        

else:
    img = st.file_uploader("Click to Upload an Image")
    if img is not None:
        encoded_image = base64.b64encode(img.read())
        result = callAPI(encoded_image)
        # try:
            # info = result['responses'][0]['textAnnotations'][0]['description']
            # st.image(img)
        # st.text("#Detected Text Results From uploaded Image")
        # st.write(result)
        pageinfo = result['responses'][0]['webDetection']['pagesWithMatchingImages']
        lsr = []
        for url in pageinfo.items():
            lsr.append(url)

        link = ' '.join(lsr)
        openai.api_key =  os.getenv("OPENAI_API_KEY")
        resp = openai.Completion.create(
        model="text-davinci-002",
        prompt="Combine all the information from the given urls together and describe breifly " + link + " .",
        temperature=0.2,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        st.write(resp.choices[0].text)

        st.table(pageinfo)
        st.table(result)

        st.write(result)
        # st.write(resp)

        # except: 
        #     st.write("An exception occurred")
        #     st.text("##API response Body")
        #     st.write(result)
        

