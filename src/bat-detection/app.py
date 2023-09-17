
# Import necessary libraries and modules
import streamlit as st  # Import Streamlit for web application development
from utils import read_config  # Import a custom utility function for reading configurations
from detection import Detection  # Import the 'Detection' class from the 'detection' module
import os  # Import the OS module for file operations

# Read configuration settings using the custom utility function
config = read_config()

# Get root directory, input image path, output image name, and output image path from the configuration
root_dir = config.get("images").get("root_dir")
input_img_name = config.get("images").get("input_image_name")
input_img_path = os.path.join(root_dir, input_img_name)
out_img_name = config.get("images").get("out_image_name")
out_img_path = os.path.join(root_dir, out_img_name)

# Create an instance of the 'Detection' class
detection_obj = Detection()

# Set up the Streamlit app
st.write("Bat Key Points Detection")

# Create a file uploader widget for uploading an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Process the uploaded image if available
if uploaded_image is not None:
    # Save the uploaded image to the input image path
    with open(input_img_path, "wb") as f:
        f.write(uploaded_image.read())

    # Check if the input image file exists
    if os.path.exists(input_img_path):
        # Create a button to trigger prediction
        if st.button("Predict"):
            # Perform key-point detection and save the resulting image
            detection_obj.combine_all()

            # Display the predicted image
            with open(out_img_path, "rb") as f:
                st.image(f.read(), use_column_width=True)

            # Create a download button for the predicted image
            with open(out_img_path, "rb") as f:
                st.download_button(
                    label="Download The Predicted Image",
                    data=f.read(),
                    file_name="pred.jpg",
                )
