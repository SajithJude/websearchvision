import streamlit as st
from googleapiclient.discovery import build
import os


url = st.text_input("enter url")

if st.button("submit"):
    APIKEY = os.environ["API_KEY"] 
    IMAGE= url
    vservice = build('vision', 'v1', developerKey=APIKEY)
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
    responses = request.execute(num_retries=2)
    x = responses['responses'][0]['webDetection']['fullMatchingImages']

    # print(js.formatter.format(responses))
    st.text(x)
    
    