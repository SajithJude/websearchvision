import streamlit as st


st.title("Ïnstancy Demo Gallery")


st.subheader(
        """
        **Read Me**: 👆 Click on the arrow icon on the left to toggle the navigationa bar and select the individual demo to run them

        """
    )

st.subheader(
    """
    **Available Demos**: Scan and Fetch,\n OCR Text Detection,\n Drug Scanner, \n Emotion Detector .
        all the above demos will request webcamera permissions to process video or you can upload an image and run the inference as well !
    """
)