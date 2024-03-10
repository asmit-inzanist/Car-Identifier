
import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
from PIL import Image

load_dotenv()


genai.configure(api_key = os.getenv('Gemini_Api_Key'))
def find_img(prompt,uploaded_img):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([prompt, uploaded_img[0]])
    return response.text

def input_img_setup(uploaded_img):
    if uploaded_img is not None:
        bytes_data = uploaded_img.getvalue()
        
        image_parts = [
            {
                
                "mime_type": uploaded_img.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")

st.title("Welcome to :red[CAR] identifier app")
st.header("Upload Image Of The Car U Want To Identify")
uploaded_img=st.file_uploader( type=["jpg","jpeg","png","webp"],label="" )


if uploaded_img is not None:
    try:
        image = Image.open(uploaded_img)  
        st.image(image, caption="Uploaded Image", use_column_width=True)
    except Exception as e:  
        st.error(f"Error processing image: {e}")

submit=st.button("Tell me about the car✨")   

prompt='''give the name of the car along with short detail of its manufacturing company and list every components, specifications in tabular format and provide a link to buy the car from its official company website     '''

if submit:
    if uploaded_img is None:
        st.error("Please upload an image before submitting.")
    else:
        image_data = input_img_setup(uploaded_img)
        response = find_img(prompt, image_data)
        st.header("The response is: ")
        st.subheader("here's what we found")
        st.write(response)
        st.info("Information provided may be inaccurate.KIndly cosider double-checking the responses.")


footer="""<style>
a:link , a:visited{
color: #FFFFFF;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: #7AE7C7;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color:transparent;
color: #FFFFFF;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a text-align: justify;' href="https://twitter.com/Asmit_inzanist" target="_blank">Asmit</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)