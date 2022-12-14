import streamlit as st
from googleapiclient.discovery import build
import os
os.environ["API_KEY"] = APIKEY
IMAGE="https://get.pxhere.com/photo/road-highway-advertising-travel-sign-community-usa-landmark-street-sign-attraction-historic-tourism-signage-road-sign-illinois-history-66-traffic-sign-route-66-mother-road-odell-644464.jpg"

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
# print(js.formatter.format(responses))
st.text(responses)