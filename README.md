To create a Conda environment, launch anaconda_prompt and run:
conda create -n name

To activate the environment, use the name of the environment you just created:
conda activate name

To see the names of all your environments, run:
conda info --envs

Use pip install to download OpenCV:
pip install opencv-python

You can import the module in python using cv2:
import cv2 as cv

OpenCV has a pre-trained Haar Cascade classifier to detect faces:
face_classifier = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

To store an image as a Mat, use cv.imread():
img = cv.imread(file path)

You may want to make the image grayscale for efficiency:
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

The classifier can be used to detect the bounding box of the face. The parameters below are used to improve accuracy:
face = face_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

To draw the bounding box, use cv.rectangle():
for (x, y, w, h) in face:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

The image can then be displayed in a seperate window using cv.imshow():
cv.imshow("window name", img)



Sources:
https://www.datacamp.com/tutorial/face-detection-python-opencv
https://docs.opencv.org/3.4/da/d60/tutorial_face_main.html
