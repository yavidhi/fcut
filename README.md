To create a Conda environment, launch anaconda_prompt and run:
conda create -n name

To activate the environment, use the name of the environment you just created:
conda activate name

To see the names of all your environments, run:
conda info --envs

Use pip install to download OpenCV:
pip install opencv-python

You can import the module in python using cv2:
import cv2

OpenCV has a pre-trained Haar Cascade classifier to detect faces:
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

To store an image as a Mat, use cv2.imread():
img = cv2.imread(file path)

You may want to make the image grayscale for efficiency:
img = cv2.cvtColor(img, cv.COLOR_BGR2GRAY)

The classifier can be used to detect the bounding box of the face. The parameters below are used to improve accuracy:
face = face_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

To draw the bounding box, use cv2.rectangle():
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    img[y:y+h, x:x+w]=img[y:y+h, x:x+w]*0.75

The image can then be displayed in a seperate window using cv2.imshow():
cv2.imshow("window name", img)



Sources:
https://www.datacamp.com/tutorial/face-detection-python-opencv
https://docs.opencv.org/3.4/da/d60/tutorial_face_main.html



Project Notes:
* The classifier did not detect the face when half of it was covered with paper. (refer to test_facedect1.py)
* When testing how much the face can be covered such that the classifier still recognizes it as a face, the classifier detected the nose and mouth as a face. One solution was to change the minSize from (40,40) to (200,200). (refer to test_facedect2.py)
