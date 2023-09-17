from utils import read_config
import gdown
import cv2
import numpy as np
from ultralytics import YOLO
class Detection:

    def __init__(self):
        self.config = read_config()

    def dowload_model(self)->None:

        self.root_dir = self.config.get("images").get("root_dir")
        model_id = self.config.get("images").get("pretrained_model_drive_id")
        model_name = self.config.get("images").get("model_name")
        self.model_path = os.path.join(self.root_dir,model_name)

        if not model_id:
            raise ValueError("No model id provided")
        
        try:
            gdown.download(id = model_id, out = self.model_path )
        except Exception as e:
            raise Exception(f"somthing failed to download model please check model id {model_id} or other ")

    def load_model(self)->None:
        if not os.path.exists(self.model_path):
            raise FileExistsError(f" model not found {self.model_path} ")
        self.model = YOLO(self.model_path)
    def detection(self,model)->dict:

        input_img_name = self.config.get("images").get("input_image_name")
        input_img_path = os.path.join(self.root_dir,input_img_name)
        if not os.path.exists(input_img_path):
            raise FileNotFoundError(f"input_img_path {input_img_path} not found")

        return model.predict(input_img_path)[0]

    def draw_circle_bb(self,result:dict)->np.array:

        input_arr = result.orig_img
        key_points = result[0].keypoints.data[0]
        for p in key_points:
            cv2.circle(input_arr,[int(p[0]),int(p[1])],3,(0,0,0),3)
        bb_data = result.boxes.data

        for bb in bb_data:
            cfs,cls = bb[-2], "bat"
            cv2.rectangle(input_arr,(int(bb[0]),int(bb[1])),
                          (int(bb[2]),int(bb[3])),
                          (0,0,255),2)
            cv2.putText(input_arr,f"{cls} - {cfs}",
                        (int(bb[0]),int(bb[1])-20),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,(0,0,255),2)

        return input_arr
    def save_img(self,img_arr:np.ndarray)->None:

        img_name = self.config.get("images").get("output_image_name")
        img_path = os.path.join(self.root_dir,img_name)
        cv2.imwrite(img_path,img_arr)

    def combine_all(self)->None:

        self.dowload_model
        result = self.detection(self.model)
        img_arr = self.draw_circle_bb(result)
        self.save_img(img_arr)
