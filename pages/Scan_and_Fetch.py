import streamlit as st
import base64
import requests
import json
# import os
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
                ],
    'image_context': {
        'web_detection_params': {
            'url_filter_set': {
                'url_filters': [
                    {
                        'filter_type': 'CONTAINS',
                        'value': 'wikipedia'
                    }
                ]
            }
        }
    }




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
            pageinfo = result['responses'][0]['webDetection']['pagesWithMatchingImages']
            link = map(lambda pageinfo: pageinfo['url'], pageinfo)
            # for i in list(link):
            #     # st.write(i)
            #     st.image(i,width=100)
        except:
            st.write("No Page Info Found for this image")
            # global lnk
            
        try:
            webent =result['responses'][0]['webDetection']['webEntities']
            entities = [webent['description'] for webent in webent if 'description' in webent]
            ent =  ' , '.join(entities)    
            lnk = ent
        except:
            st.write("No Page Entities  Found for this image")
            # global e


        # lsr = []
        # # [pageinfo['value'] for pageinfo in l if 'value' in pageinfo]
        
        # for url in pageinfo.items():
        #     lsr.append(url)
       
        # st.write(entities)


        guesslabels =result['responses'][0]['webDetection']['bestGuessLabels']
        guesslab = [guesslabels['label'] for guesslabels in guesslabels if 'label' in guesslabels]
        gl =  ' '.join(guesslab)

        col1 ,col2 = st.columns(2)

        with col1:
            st.header("Image annotation")
            st.write(gl)

        with col2:
            st.header("Detected Entities")
            st.write(ent)
            # st.write(annotation['joyLikelihood']) 
        # st.write(gl)

        # link = map(lambda pageinfo: pageinfo['url'], pageinfo)
        # for i in list(link):
        #     st.write(i)
        #     st.image(i,width=100)
        # # for key in link.keys()):
        #     st.image(str(link[key]))
        # lnk = ' '.join(link)
        # st.write(lnk)
        openai.api_key =  os.getenv("OPENAI_API_KEY")
        resp = openai.Completion.create(
        model="text-davinci-002",
        prompt="Combine all the information from the given urls together and describe breifly " + lnk + ".",
        temperature=0.2,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        st.write(resp.choices[0].text)

        st.table(pageinfo)
        st.table(result['responses'][0])

        st.write(result) 


        # except: 
        #     st.write("An exception occurred")
        #     st.write("##API response Body")
        #     st.write(result) 
        

else:
    img = st.file_uploader("Click to Upload an Image")
    if img is not None:
        encoded_image = base64.b64encode(img.read())
        result = callAPI(encoded_image)
        try:
            info = result['responses'][0]
            st.image(img)
            st.text("#Detected Text Results From uploaded Image")
            st.write(result)
        except:
            st.write(result)


        pageinfo = result['responses'][0]['webDetection']['pagesWithMatchingImages']
        # lsr = []
        # # [pageinfo['value'] for pageinfo in l if 'value' in pageinfo]
        
        # for url in pageinfo.items():
        #     lsr.append(url)
        webent =result['responses'][0]['webDetection']['webEntities']
        entities = [webent['description'] for webent in webent if 'description' in webent]
        ent =  ' , '.join(entities)
        # st.write(entities)


        guesslabels =result['responses'][0]['webDetection']['bestGuessLabels']
        guesslab = [guesslabels['label'] for guesslabels in guesslabels if 'label' in guesslabels]
        gl =  ' '.join(guesslab)

        col1 ,col2 = st.columns(2)

        with col1:
            st.header("Image annotation")
            st.write(gl)

        with col2:
            st.header("Detected Entities")
            st.write(ent)
            # st.write(annotation['joyLikelihood']) 
        # st.write(gl)

        link = map(lambda pageinfo: pageinfo['url'], pageinfo)
        for i in list(link):
            st.write(i)
            st.image(i,width=100)
        # # for key in link.keys()):
        #     st.image(str(link[key]))
        lnk = ' '.join(link)
        st.write(lnk)
        openai.api_key =  os.getenv("OPENAI_API_KEY")
        resp = openai.Completion.create(
        model="text-davinci-002",
        prompt="Combine all the information from the given urls together and describe comprehensivley " + lnk + " .",
        temperature=0.2,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0,
        # stop=["\n"]
        )
        st.write(resp.choices[0].text)

        st.table(pageinfo)
        st.table(result['responses'][0])

        st.write(result)
        # st.write(resp)

        # except: 
        #     st.write("An exception occurred")
        #     st.text("##API response Body")
        #     st.write(result)
        

