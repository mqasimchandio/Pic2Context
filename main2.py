from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai

API_KEY = "YOUR_GOOGLE_API_KEY"
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)


def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('Gemini 1.5')
    response = model.generate_content([input,image[0],prompt])
    return response.text
    

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


## Initializing our streamlit app
st.set_page_config(page_title="Gemini Chat")

st.header("Gemini Pro 1.5")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose a file...", type=["jpg", "jpeg", "png", "txt", "pdf", "docx"])
file_display = ""

if uploaded_file is not None:
    if uploaded_file.type.startswith("image/"):
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
    elif uploaded_file.type == "text/plain":
        file_display = uploaded_file.getvalue().decode("utf-8")
        st.text_area("Uploaded Text File", file_display, height=300)
    else:
        st.write("Uploaded file:", uploaded_file.name)

submit = st.button("Tell me about the file")


input_prompt = """
               You are expert in understanding images that study materials in `images`, scenes, 
                and concepts and can analyze the content. You will answer in more details,
                also explain the subtopics in more details. If it is programming/code related then explain line by line by adding the respective line code.
                """

if submit:
    image_data = input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)





