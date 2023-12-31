from cv2 import CascadeClassifier, VideoCapture, cvtColor, COLOR_BGR2GRAY, imwrite, rectangle, imshow, waitKey, destroyAllWindows
from datetime import datetime
quit_key = 'q'

# Load pre-trained human detection models
human_cascade = CascadeClassifier('haarcascade_fullbody.xml')
face_cascade = CascadeClassifier('haarcascade_frontalface_default.xml')
upperbody_cascade = CascadeClassifier('haarcascade_upperbody.xml')
lowerbody_cascade = CascadeClassifier('haarcascade_lowerbody.xml')
profile_cascade = CascadeClassifier('haarcascade_profileface.xml')

# Initialize the camera
camera = 0 # 0 for default camera, change to a different number if you have multiple cameras.
cap = VideoCapture(camera)
# Check if the camera exist
if not cap.isOpened():
    print("Error: Camera not found.")
    exit(1)

# Initialize variables to control picture and log intervals
last_capture_time = datetime.now()
log_interval = 10  # Log an entry and take picture every X seconds

def save_image(timestamp, frame, humans, faces, lower_bodies, upper_bodies, profile):
    # Draw rectangles around detected humans
    for (x, y, w, h) in humans:
        frame = rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw a green rectangle for humans
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        frame = rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Draw a red rectangle for faces
    # Draw rectangles around detected upper bodies
    for (x, y, w, h) in upper_bodies:
        frame = rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw a blue rectangle for upper bodies
    # Draw rectangles around detected lower bodies
    for (x, y, w, h) in lower_bodies:
        frame = rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)  # Draw a yellow rectangle for lower bodies
    # Draw rectangles around detected profile faces
    for (x, y, w, h) in profile:
        frame = rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)  # Draw an orange rectangle for profile faces
    
    image_filename = f"human_{timestamp}.jpg"
    imwrite(image_filename, frame)
    # Check if is possible to save the img
    if not imwrite(image_filename, frame):
        print(f"Error: Unable to save image {image_filename}")

def save_log(timestamp):
    try:
        with open('detection_log.txt', 'a') as log_file:
            log_file.write(f"Human detected at {timestamp}\n")
    except IOError:
        print("Error: Unable to write to the log file.")

while True:
    ret, frame = cap.read()  # Capture a frame from the camera

    if not ret:
        print("Error: Unable to capture frame.")
        continue

    # Convert the frame to grayscale for detection
    gray = cvtColor(frame, COLOR_BGR2GRAY)

    # Detect humans in the frame
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    profile = profile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Detect lower and upper bodies
    upper_bodies = upperbody_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    lower_bodies = lowerbody_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    time_difference = int((datetime.now() - last_capture_time).total_seconds())

    if (len(humans) > 0 or len(faces) > 0 or len(upper_bodies) > 0 or  len(profile) > 0) and time_difference - log_interval >= 0:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # A human is detected, capture the image
        save_image(timestamp, frame, humans, faces, profile, upper_bodies, lower_bodies)

        # Log the detection time to a text file
        save_log(timestamp)
        
        last_capture_time = datetime.now()

    imshow('Human Detection', frame)
    
    if waitKey(1) & 0xFF == ord(quit_key):
        break

cap.release()
destroyAllWindows()