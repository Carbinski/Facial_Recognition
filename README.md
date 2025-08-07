# Facial Recognition System – v2

## 📝 Description

**Facial Recognition** is a work-in-progress project focused on implementing facial detection and recognition capabilities. The primary goal is to identify individuals in real-time and enable customized responses based on who is recognized.

The envisioned use case is a smart home system that detects who is walking by and delivers personalized interactions, such as greetings, notifications, or environment adjustments. This project aims to blend computer vision with contextual awareness to create a more intelligent and human-centered home experience.

## 🚀 Setup

Install the required Python packages in the project root directory (I definitely forgot some):

```
pip install opencv-python
pip install numpy
pip install pillow
pip install edge-tts
pip install pygame
```

**💡 Note:** If you’re having installation or usage issues, feel free to ask ChatGPT for help.

**🔧 Version Info**

Current development is happening in the `v2/` folder. You can ignore `v1/`.

Also, sometimes the computers connection to camera doesn't work on the first try. Run the script again if needed.

⸻

## 🎯 Usage Guide

### 1. Generate a Dataset

Open `Dataset_Generation.py` and set the id to a unique number and name for the person you’re adding to the dataset.

Then:
-	Have the person stand in front of the camera.
- Run the script for 15–30 seconds.
- The system will automatically detect and save their face images to `v2/data/` under a folder with their ID.

⚠️ Important: After collecting the data, review the images and delete any false positives if you want to boost performance.

⸻

### 2. Create the Classifier

Run `Create_Classification.py`.
This will generate a `classifier.yml` file based on the face data collected earlier.
-	The more data you collect, the better the model will perform (in theory).
-	15–30 seconds of good quality data per person usually works well.
- If you want to add more people you will need to do either:
  - Manual input it before running `Create_Classification.py`
  - Edit the `users.json` file
  - Use Controller.py to run `Create_Classification.py`

⸻

### 3. Detect People

Use `Detect_Person.py` to test recognition.
- It should draw a box around detected faces with the associated names (based on IDs).

⸻

**🛠️ Extra Tools**
-	`Controller.py`: A menu-based interface to run the above scripts.
-	`Detect_Face_Features.py`: Just a demo to visualize basic face detection in action.

⸻

**❓ Troubleshooting**
-	If the code fails unexpectedly, just try running it again.
-	Make sure your camera is connected and accessible by OpenCV.
-	Clean your dataset regularly to maintain accuracy.
-	The Haas Cascade Facial detection works best when facing head on.
-	Try to have training data mirror use case when testing the `Detect_Person.py`
 
