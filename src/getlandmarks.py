from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import argparse



# def main():
#     imgpath = "./learncv/assets/guywitheyes.jpg"
#     img = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)
#     landmarks = stasm.search_single(img)
#     print(landmarks)

# if __name__ == "__main__":
#     main()

def shapeToArray(shape, dtype="int"):
    # getting a list of x, y coordinates
    coords = np.zeros((68, 2), dtype = dtype)

    # looping over the landmarks and converting them to tuple
    for i in range(68):
        coords[i] = (shape.part(i).x, shape.part(i).y)

    return coords