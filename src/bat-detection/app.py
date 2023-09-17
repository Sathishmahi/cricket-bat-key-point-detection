import streamlit as st
import wget
from utils import read_config
from detection import Detection
import requests
import os

config = read_config()
root_dir = config.get("images").get("root_dir")
input_img_name = config.get("images").get("input_image_name")
input_img_path = os.path.join(root_dir, input_img_name)
out_img_name = config.get("images").get("out_image_name")
out_img_path = os.path.join(root_dir, out_img_name)

detection_obj = Detection()

# Create a dropdown widget

st.write("Bat Key Points Detection")
selected_option = st.selectbox("Select an option to upload image", ["PASTE URL", "UPLOAD FILE FROM LOCAL"])


if selected_option == "PASTE URL":
    url = st.text_input("Paste the URL of the image")
    response = requests.get(url)
    if response.status_code == 200:
        with open(input_img_path,"wb") as f:
            f.write(response.content)
        uploaded_image = True
    else:
        st.write("Invalid URL")

else:
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_image is not None:
        with open(input_img_path,"wb") as f:
            f.write(uploaded_image.read())

if os.path.exists(input_img_path):
    if st.button("Predict"):
        detection_obj.combine_all()

    with open(out_img_path,"rb") as f:

        st.image(f.read(),use_column_width=True)
        st.download_button(
        label="Download The Predicted Image",
        data=f.read(),
        file_name="pred.jpg",
    )