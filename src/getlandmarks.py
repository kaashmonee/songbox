from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import argparse
from src.detectface import FaceDetector




# def main():
#     imgpath = "./learncv/assets/guywitheyes.jpg"
#     img = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)
#     landmarks = stasm.search_single(img)
#     print(landmarks)

# if __name__ == "__main__":
#     main()

LANDMARKS_CLASSIFIER = "./src/assets/shape_predictor_68_face_landmarks.dat"
IMAGE_PATH = "./src/assets/captured.png"

def shapeToArray(shape, dtype="int"):
    # getting a list of x, y coordinates
    coords = np.zeros((68, 2), dtype = dtype)

    # looping over the landmarks and converting them to tuple
    for i in range(68):
        coords[i] = (shape.part(i).x, shape.part(i).y)

    return coords

# detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(LANDMARKS_CLASSIFIER)

class LandmarkRetriever:
    def __init__(self, image):

