import streamlit as st
import base64
import requests
import json
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

st.title('Product Search')
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
        full_matching_image_urls = []
        st.subheader("Matching Products in the Web")
        for item in result['responses'][0]['webDetection']['fullMatchingImages']:
            full_matching_image_urls.append(item['url'])
        # st.write(full_matching_image_urls)
        for item in full_matching_image_urls:
            st.image(item, width=150)
            st.write(item)

        if st.checkbox("Show only Shopify"):
            try:
                
                st.subheader("Shopify product matches")
                linkedInUrl = [site for site in full_matching_image_urls if "shopify.com" in site]
                
                # st.write(linkedInUrl)
                # inlik = map(lambda linkedInUrl: linkedInUrl[0]['url'], linkedInUrl)
                for item in linkedInUrl:
                    st.image(item, width=150)
                    st.write(item)
                if len(linkedInUrl)==0:
                    st.caption("No Products found in flipkart")
                # st.write(linkedInUrl)
            except:
                st.write("API EXCEPtoin error")

        if st.checkbox("Show only flipkart"):
            try:
                
                st.subheader("flipkart product matches")
                linkedInUrl = [site for site in full_matching_image_urls if "flipkart.com" in site]
                
                # st.write(linkedInUrl)
                # inlik = map(lambda linkedInUrl: linkedInUrl[0]['url'], linkedInUrl)
                for item in linkedInUrl:
                    st.image(item, width=150)
                    st.write(item)
                if len(linkedInUrl)==0:
                    st.caption("No Products found in flipkart")
                # st.write(linkedInUrl)
            except:
                st.write("API EXCEPtoin error")
        
        try:
            info = result['responses'][0]['webDetection']['pagesWithMatchingImages']
            st.image(img)
            st.text("#Detected Text Results From uploaded Image")
            st.write(info)

        except: 
            st.write("An exception occurred")
            st.text("##API response Body")
            st.write(result)
        


        

else:
    img = st.file_uploader("Click to Upload an Image")
    if img is not None:
        encoded_image = base64.b64encode(img.read())
        result = callAPI(encoded_image)
        full_matching_image_urls = []
        for item in result['responses'][0]['webDetection']['fullMatchingImages']:
            full_matching_image_urls.append(item['url'])
        # st.write(full_matching_image_urls)
        for item in full_matching_image_urls:
            st.image(item, width=150)
            st.write(item)

        if st.checkbox("Show only Shopify"):
            try:
                
                st.subheader("Shopify product matches")
                linkedInUrl = [site for site in full_matching_image_urls if "shopify.com" in site]
                
                # st.write(linkedInUrl)
                # inlik = map(lambda linkedInUrl: linkedInUrl[0]['url'], linkedInUrl)
                for item in linkedInUrl:
                    st.image(item, width=150)
                    st.write(item)
                if len(linkedInUrl)==0:
                    st.caption("No Products found in flipkart")
                # st.write(linkedInUrl)
            except:
                st.write("API EXCEPtoin error")

        if st.checkbox("Show only flipkart"):
            try:
                
                st.subheader("flipkart product matches")
                linkedInUrl = [site for site in full_matching_image_urls if "flipkart.com" in site]
                
                # st.write(linkedInUrl)
                # inlik = map(lambda linkedInUrl: linkedInUrl[0]['url'], linkedInUrl)
                for item in linkedInUrl:
                    st.image(item, width=150)
                    st.write(item)
                if len(linkedInUrl)==0:
                    st.caption("No Products found in flipkart")
                # st.write(linkedInUrl)
            except:
                st.write("API EXCEPtoin error")
        
        try:
            info = result['responses'][0]['webDetection']['pagesWithMatchingImages']
            st.image(img)
            st.text("#Detected Text Results From uploaded Image")
            # st.table(info)

        except: 
            st.write("An exception occurred")
            # st.text("##API response Body")
            # st.write(result)
        

