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
mSize=(200,200)
x=225 # 337 (w/ mSize=(40,40)), 319 (w/ mSize=(200,200))
face = [[0]]
t=1
next_img = img
while str(type(face)) != "<class 'tuple'>" and x <= 400:
    x += t
    img = next_img
    next_img[:, 0:x] = 0
    face = face_classifier.detectMultiScale(
        next_img, scaleFactor=1.1, minNeighbors=5, minSize=mSize
    )
    print(x)
print("Result: "+str(x-t))
img = color_img
img[:,0:x-t]=0
face = face_classifier.detectMultiScale(
    img, scaleFactor=1.1, minNeighbors=5, minSize=mSize
)
print(face)
for (x, y, w, h) in face:
    face_full = img[y:y+h, x:x+w]
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    img[y:y+h, x:x+w]=img[y:y+h, x:x+w]*0.75
    
#cv.imshow("Display window",face_full)
cv.imshow("Display window",img)
k = cv.waitKey(0)