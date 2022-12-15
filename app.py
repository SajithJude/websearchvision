import streamlit as st
# from googleapiclient.discovery import build
import os
import pandas as pd




# python code for latest way to annotate images using gcp vision v-1 without using types.


# Importing necessary Standard Libraries
import base64
import requests
import json

# # The GCP Vision API URL 
# vision_url = 'https://vision.googleapis.com/v1/images:annotate?key='

# # Your Google Cloud Platform (GCP) API KEY. Generate one on cloud.google.com
# api_key = os.environ["API_KEY"] 
# # Load your image as a base64 encoded string


# with open("/content/images.jpg", "rb") as image_file:
#     encoded_image = base64.b64encode(image_file.read())

# # Generate a post request for GCP vision Annotation
# json_data= {
#     'requests': [
#         {
#             'image':{
#                 'content': encoded_image.decode('utf-8')
#             },
#             'features':[
#                 {
#                     'type':'WEB_DETECTION',
#                     'maxResults':5
#                 }
#             ]
#         }
#     ]
# }

# # Handle the API request
# response = requests.post(vision_url+api_key, json=json_data)

# # Read the response in json format
# response_data = response.json()

# # Printing the response, in this case it will return all the labels that are 
# # identified in the image
# print("GCP Vision Annotation :")
# print(json.dumps(response_data, indent=4))


url = st.text_input("enter url")
APIKEY = os.environ["API_KEY"] 

vservice = build('vision', 'v1', developerKey=APIKEY)
if url:
    IMAGE= str(url)
    st.image(IMAGE, width=250)


    request = vservice.images().annotate(body={
            'requests': [{
                    'image': {
                        'source': {
                            'imageUri': IMAGE
                        }
                    },
                    'features': [{
                        'type': 'WEB_DETECTION'
                    }]
                }],
            })
    responses = request.execute()
    # try:
    x = responses['responses'][0]['webDetection']['fullMatchingImages']
    # y = responses['responses'][0]['webDetection']['partialMatchingImages']
    # z = responses['responses'][0]['webDetection']['pagesWithMatchingImages']
    # w = responses['responses'][0]['webDetection']['visuallySimilarImages']
    # f = responses['responses'][0]['webDetection']['bestGuessLabels']
    
    # except:
    # st.write("An exception occurred")

    new = pd.DataFrame(x)
    ne = pd.DataFrame(responses)
    # n = pd.DataFrame(z)
    # wn = pd.DataFrame(w)
    # st.write("keywords  :"+str(f))

    st.text("Full matching ")
    st.dataframe(new)
    # st.text("Partial matching ")
    st.dataframe(ne)
    # st.text("Pages with matching ")
    # st.dataframe(n)
    # st.text("Visually similar matching ")
    # st.dataframe(n)    
    

    # print(js.formatter.format(responses))
    st.write(responses)
    # st.write(x)


    