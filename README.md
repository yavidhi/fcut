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

To store a file as a Mat, use cv.imread():
img = cv.imread(file path)

The image can be displayed in a seperate window using cv.imshow():
cv.imshow("window name", img)



For face recognition, go to https://docs.opencv.org/3.4/da/d60/tutorial_face_main.html.
