**Experience and Challenges:**
- The task of key-point detection, especially for cricket batsman bat's four corner keypoints, proved challenging due to the precision required.
- Data collection was time-consuming as automated scripts did not yield high-quality data. So manually collected around 140 images for the project.
- Data labeling was complex because the order of keypoints varied between images. You addressed this challenge by using the CVAT.ai tool for data annotation.
- Training a YOLOv8 large model for both object detection and key-point detection increased training time compared to single-task models.

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
