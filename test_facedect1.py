import cv2 as cv
import sys
face_classifier = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

color_img = cv.imread(r"C:\Users\freed\Desktop\opencv1\Screenshot 2024-11-11 140855.png")
# color_img = cv.imread(r"C:\Users\freed\Desktop\opencv1\Screenshot 2024-11-11 144539.png")
if color_img is None:
    sys.exit("o no")
img = cv.cvtColor(color_img, cv.COLOR_BGR2GRAY)
face = face_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)
for (x, y, w, h) in face:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    img[x:x+w, y:y+h]=img[x:x+w, y:y+h]*0.75
cv.imshow("Display window",img)
k = cv.waitKey(0)