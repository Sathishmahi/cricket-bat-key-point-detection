# cricket-bat-key-point-detection

## Objective:

The project focuses on developing a key-point detection system to identify the four corners of a cricket batsman's bat.

## Tech Stack

**Language:** Python

**Libraries to Use:** CVZone,Cv2,Ultralytics

**UI:** StreamLit

**Model to Use:** Finetuned Yolo-V8 large Model with Custom Dataset


## Run Locally

Clone the project

```bash
git clone https://github.com/Sathishmahi/cricket-bat-key-point-detection.git
```

create ,activate conda env and install requirements   

```bash
 bash env.sh 
```
run streamlit app

```bash
bash run.sh
```

### sample output

## input image
![138](https://github.com/Sathishmahi/cricket-bat-key-point-detection/assets/88724458/343640ff-0507-44cb-9a59-4da45c65162b)



## After Predict the Model 
### output image 


![pred (6)](https://github.com/Sathishmahi/cricket-bat-key-point-detection/assets/88724458/8a587563-30e3-45ed-a304-81a30a6150e9)



**Experience and Challenges:**
- The task of key-point detection, especially for cricket batsman bat's four corner keypoints, proved challenging due to the precision required.
- Data collection was time-consuming as automated scripts did not yield high-quality data. So manually collected around 140 images for the project.
- Data labeling was complex because the order of keypoints varied between images. CVAT.ai tool for data annotation.
- Training a YOLOv8 large model for both object detection and key-point detection increased training time compared to single-task models.

**Training time**
 - I trained the YOLOv8 large model for pose detection, and the training or finetuning process took approximately 30 minutes in Google Colab, which I used for free version. My training dataset consisted of around 140 images.

**Key Point Detection:**
- Key-point detection is a computer vision task focused on identifying and locating specific points of interest in images. These points serve as critical landmarks for various applications.
- Key-point detection is vital for tasks such as object tracking, pose estimation, and facial recognition, providing essential information for image analysis.

**Key-Point Detection Complexity:**
Key-point detection is inherently complex compared to other computer vision tasks due to the precision required in identifying specific points within an image.
Unlike tasks such as object detection or segmentation, key-point detection involves pinpointing exact locations of crucial landmarks, often requiring fine-grained analysis.

**Advantages of YOLO (You Only Look Once):**
- YOLO is a popular object detection framework known for its speed and accuracy.
- YOLO processes the entire image in one forward pass, making it real-time capable and efficient.
- It excels in detecting objects of varying sizes and multiple objects in a single image.
- YOLOv8, in particular, builds on the strengths of previous versions, offering a balance between speed and accuracy.

### model weights , datasets , annotation (Click and download the files or folder)

[model-checkpoints](https://drive.google.com/file/d/1gun4_HTdz3zl1KH86nwL6D7BbGin3n4G/view?usp=sharing)

[custom dataset](https://drive.google.com/drive/folders/1IF6tmkbp6dXlLv0IdP1MorUbzRFhxPLs?usp=drive_link)

[config.yaml file](https://drive.google.com/file/d/1S9-3NNy2X94O9YlksQ3IJ_KRGDW22cHF/view?usp=sharing)

[data annotation zip file](https://drive.google.com/file/d/1M2VkDp2KWFEdo_4LF9ZqZLoE18RcS5rg/view?usp=sharing)

[data annotation in .xml format](https://drive.google.com/file/d/1ZtttN5ZVfPmlMSVS4LrGg2BYmz00T4RH/view?usp=sharing)

### Demo Video

https://github.com/Sathishmahi/cricket-bat-key-point-detection/assets/88724458/8f60bc61-65cc-4783-bf44-d930c1f29dee

