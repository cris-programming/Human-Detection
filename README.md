# Human Detection using OpenCV

This Python script uses the OpenCV library to detect humans, faces, upper bodies, and lower bodies through a camera feed. It captures frames from the camera, processes them to identify objects, and logs the detection times and saves images when objects are detected.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)

## Prerequisites
Before running the script, you need to ensure you have the following prerequisites installed on your system:
- Python 3
- OpenCV Python Library
- A webcam or camera connected to your computer
- XML files from OpenCv GitHub

You can install OpenCV for Python using pip:

```bash
pip install opencv-python
```

## Getting Started
1. Clone this repository to your local machine or download the script directly.

2. Ensure you have the required Haar cascade XML files for human, face, upper body, and lower body detection. You can find these XML files online or use the pre-trained ones. Update the paths to these files in the script:

```python
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
upperbody_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
lowerbody_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')
profile_cascade = CascadeClassifier('haarcascade_profileface.xml')
```

3. Run the script:

```bash
python main.py
```

## Usage
- Once the script is running, it will open the camera feed.

- The script continuously captures frames from the camera and processes them for human, face, upper body, and lower body detection.

- If any of these objects are detected, the script will save an image with a timestamp in the format "human_YYYY-MM-DD_HH-MM-SS.jpg".

- It also logs the detection time in a text file named "detection_log.txt".

- To exit the script, press the 'q' key.

## Configuration
You can configure the following settings in the script:

- `camera`: Set to '0' for the default camera. Change it to a different number if you have multiple cameras.

- `log_interval`: Set the interval (in seconds) at which the script logs detection times and saves images.

- `quit_key`: Set the key you will use to quit the program
