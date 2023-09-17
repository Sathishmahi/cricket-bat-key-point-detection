# Import necessary libraries and modules
from utils import read_config  # Import a custom utility function
import gdown  # Import gdown for downloading files
import cv2  # Import OpenCV for image processing
import numpy as np  # Import NumPy for numerical operations
from ultralytics import YOLO  # Import YOLOv8 from Ultralytics for object detection
import os  # Import the OS module for file operations
import cvzone  # Import cvzone for additional image processing functions
import json
import logging

# Define a class named 'Detection'
class Detection:

    def __init__(self):
        # Read configuration settings using the custom utility function
        self.config = read_config()
        logging.info(f"config details {self.config} ")

    def dowload_model(self)->None:
        """
        Download a pre-trained YOLOv8 model from Google Drive based on the provided model ID.
        Save the model to the specified directory.
        """

        # Get root directory and create it if it doesn't exist
        self.root_dir = self.config.get("images").get("root_dir")
        os.makedirs(self.root_dir, exist_ok=True)

        # Get the model ID and model name from the configuration
        model_id = self.config.get("images").get("pretrained_model_drive_id")
        model_name = self.config.get("images").get("model_name")

        # Define the full model path
        self.model_path = os.path.join(self.root_dir, model_name)

        # Check if the model ID is provided
        if not model_id:
            e = "No model id provided"
            logging.exception(e)
            raise ValueError(e)

        try:
            # Download the model only if it doesn't already exist
            if not os.path.exists(self.model_path):
                gdown.download(id=model_id, output=self.model_path)
            else:
                print(f"Model already downloaded {self.model_path}")
        except Exception as e:
            logging.exception(e)
            raise Exception(f"Something failed to download the model. Please check model id {model_id} or other issues.")

    def load_model(self)->None:
        """
        Load the YOLOv8 model from the saved model path.
        """

        # Check if the model file exists
        if not os.path.exists(self.model_path):
            e = f"Model not found {self.model_path}"
            logging.exception(e)
            raise FileExistsError(e)

        # Load the YOLOv8 model using Ultralytics
        self.model = YOLO(self.model_path)

    def detection(self, model)->dict:
        """
        Perform object detection on the input image using the loaded YOLOv8 model.
        Return the detection results.
        """

        # Get the input image name and path from the configuration
        input_img_name = self.config.get("images").get("input_image_name")
        input_img_path = os.path.join(self.root_dir, input_img_name)

        # Check if the input image file exists
        if not os.path.exists(input_img_path):
            e = f"Input image path {input_img_path} not found"
            logging.exception(e)
            raise FileNotFoundError(e)

        # Perform object detection using the YOLOv8 model and return the results
        return model.predict(input_img_path)[0]

    def draw_circle_bb(self, result: dict)->np.array:
        """
        Draw circles around keypoints and bounding boxes on the input image based on the detection results.
        Return the modified image array.
        """
        final_dict = {"key_points":[],"bboxes":[]}
        # Get the original image array from the results
        input_arr = result.orig_img

        # Extract key points from the results
        key_points = result[0].keypoints.data[0]

        # Draw circles around key points
        for p in key_points:
            points = [int(p[0]), int(p[1])]
            final_dict["key_points"].append(points)
            cv2.circle(input_arr,points , 3, (255, 0, 0), 5)

        # Extract bounding box data from the results
        bb_data = result.boxes.data

        # Draw bounding boxes with labels
        for bb in bb_data:
            cfs, cls = bb[-2], "bat"
            x1, y1 = (int(bb[0]) - 10, int(bb[1]) - 10)
            x2, y2 = (int(bb[2]) + 10, int(bb[3]) + 10)
            final_dict["bboxes"].append([x1,y1,x2,y2])
            cvzone.cornerRect(input_arr, (x1, y1, (x2 - x1), (y2 - y1)), 15, 3)
            cvzone.putTextRect(input_arr, f"{cls}", (int(bb[0]), int(bb[1]) - 20), 2, 2, offset=1)
        logging.info(f"result {final_dict}")
        return input_arr,final_dict
    def save_json(self,content:dict)->None:
        json_name = self.config.get("images").get("json_file_name")
        with open(os.path.join(self.root_dir,json_name),"w") as f:
            json.dump(content, f)
    def save_img(self, img_arr: np.ndarray)->None:
        """
        Save the modified image array to the specified output image path.
        """

        # Get the output image name and path from the configuration
        img_name = self.config.get("images").get("out_image_name")
        img_path = os.path.join(self.root_dir, img_name)

        # Save the image using OpenCV
        cv2.imwrite(img_path, img_arr)

    def combine_all(self)->bool:
        """
        Perform all necessary steps to download the model, load it, perform detection, draw key points and bounding boxes, and save the resulting image.
        """

        # Download the pre-trained model
        self.dowload_model()

        # Load the YOLOv8 model
        self.load_model()

        # Perform object detection and get the results
        result = self.detection(self.model)
        if result:
            # Draw key points and bounding boxes, and save the resulting image
            img_arr,result = self.draw_circle_bb(result)
            self.save_json(result)
            self.save_img(img_arr)
            return True
        else:
            return False

if __name__ == "__main__":
    # Create an instance of the Detection class and execute the entire pipeline
    detection = Detection()
    detection.combine_all()
