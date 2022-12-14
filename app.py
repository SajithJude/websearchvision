import streamlit as st
from googleapiclient.discovery import build
import os


url = st.text_input("enter url")
APIKEY = os.environ["API_KEY"] 
IMAGE= str(url)
vservice = build('vision', 'v1', developerKey=APIKEY)
if url:


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
    x = responses['responses'][0]['webDetection']['fullMatchingImages']

    # print(js.formatter.format(responses))
    st.write(responses)
    st.write(x)


    