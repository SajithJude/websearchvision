import streamlit as st
from googleapiclient.discovery import build
import os
import pandas as pd


url = st.text_input("enter url")
APIKEY = os.environ["API_KEY"] 
IMAGE= str(url)
st.image(IMAGE, width=250)
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
    y = responses['responses'][0]['webDetection']['partialMatchingImages']
    z = responses['responses'][0]['webDetection']['pagesWithMatchingImages']
    w = responses['responses'][0]['webDetection']['visuallySimilarImages']
    
    new = pd.DataFrame(x)
    ne = pd.DataFrame(y)
    n = pd.DataFrame(z)
    wn = pd.DataFrame(w)


    st.text("Full matching ")
    st.dataframe(new)
    st.text("Partial matching ")
    st.dataframe(ne)
    st.text("Pages with matching ")
    st.dataframe(n)
    st.text("Visually similar with matching ")
    st.dataframe(n)    
    

    # print(js.formatter.format(responses))
    st.write(responses)
    # st.write(x)


    