import streamlit as st
import base64
import requests
import gmaps
import os
import openai
# import os
gmapapi= os.environ["API_KEY"] 
gmaps.configue(api_key=gmapapi)
nyc = (940.75,-74.00)
gmaps.figure(center=nyc,zoom_level=12)


st.title('Famous Location/Landmarks Detection based on Image')
# cam = st.radio('Please select an option',('Open Webcam', 'Upload Image'))
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
                        'type':'LANDMARK_DETECTION',
                        'maxResults':10
                    }
                ]
            }
        ]
    }

    # Handle the API request
    responses = requests.post(vision_url+api_key, json=json_data)

    # Read the response in json format

    return responses.json()


# if cam =='Open Webcam':
#     img_file_buffer = st.camera_input("Take a picture")
#     if img_file_buffer is not None:
#         encoded_image = base64.b64encode(img_file_buffer.read())
#         result = callAPI(encoded_image)
#         try:
#             info = result['responses'][0]['landmarkAnnotations'][0]['description']
#             # st.image(img)
#             st.text("#Detected Text Results From uploaded Image")
#             st.write(info)
#             openai.api_key =  os.getenv("OPENAI_API_KEY")
#             resp = openai.Completion.create(
#             model="text-davinci-002",
#             prompt="Find some information about this location : " + info + "  .",
#             temperature=0.2,
#             max_tokens=3500,
#             top_p=1,
#             frequency_penalty=0.35,
#             presence_penalty=0,
#             # stop=["\n"]
#             )
#             st.write(resp.choices[0].text)

#         except: 
#             st.write("An exception occurred")
#             # st.text("##API response Body")
#             st.write(result)
        

# else:
img = st.file_uploader("Click to Upload an Image")
if img is not None:
    encoded_image = base64.b64encode(img.read())
    result = callAPI(encoded_image)
    try:
        info = result['responses'][0]['landmarkAnnotations'][0]['description']
        coor = result['responses'][0]['landmarkAnnotations'][0]['locations'][0]['latLng']
        st.image(img)
        col1,col2  = st.columns(2)
        with col1:
            st.header("Detected Text  :")
            # st.write(gl)

        with col2:
            # st.header("Detected Entities")
            # st.write(ent)
            st.subheader(info)
        st.caption(info)
        st.caption("Coordinates :"+ str(coor))
        openai.api_key =  os.getenv("OPENAI_API_KEY")
        resp = openai.Completion.create(
        model="text-davinci-003",
        prompt="Find some information about this location : " + info + "  .",
        temperature=0.2,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        st.write(resp.choices[0].text)


    except: 
        st.write("An exception occurred")
        # st.text("##API response Body")
        st.write(result)
        

