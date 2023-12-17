import streamlit as st
from PIL import Image

import os

import google.generativeai as genai

from dotenv import load_dotenv, dotenv_values  # we can use load_dotenv or dotenv_values both perform the same task

load_dotenv()

# print(os.getenv("MY_SECRET_KEY"))

genai.configure(api_key=os.getenv("MY_SECRET_KEY")) 

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
}


def main():
    st.title("Object Finder 🔍")
    
    disclaimer_message = """This is a object detector model so preferably use images containing different objects,tools... for best results 🙂"""

    # Hide the disclaimer initially
    st.write("")

    # Show the disclaimer if the button is clicked
    with st.expander("Disclaimer ⚠️", expanded=False):
       st.markdown(disclaimer_message)
    

    # Upload image through Streamlit
    uploaded_image = st.file_uploader("Choose an image ...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

        # Process the image (example: get image dimensions)
        image = Image.open(uploaded_image)
        width, height = image.size
        st.write("Image Dimensions:", f"{width}x{height}")

        if st.button("Identify the objects"):

            st.success("Detecting...")

            vision_model = genai.GenerativeModel('gemini-pro-vision')
            response = vision_model.generate_content(["Extract the objects in the provided image and output them in a list in alphabetical order",image])

            
            st.write("The objects detected are \n", response.text)

            st.success("Thanks for visiting 🤩!!")

            st.info("For trying out with another image just click on browse files, enjoy 😄!!!")


if __name__ == "__main__":
    main()

