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


# detector = dlib.get_frontal_face_detector()

class LandmarkRetriever:

    # class attributes
    LANDMARKS_CLASSIFIER = "./src/assets/shape_predictor_68_face_landmarks.dat"
    IMAGE_PATH = "./src/assets/captured.png"
    predictor = dlib.shape_predictor(LandmarkRetriever.LANDMARKS_CLASSIFIER)


    def __init__(self, image=LandmarkRetriever.IMAGE_PATH):
        self.faces = FaceDetector(image)
        if not self.faces.hasFaces():
            raise Exception("No faces found! Please select another image.")
        
    def getLandmarks(self):
        for (x, y, w, h) in self.faces:
            rect = dlib.rectangle(left=x, top=y, width=w, height=h)
            # gets the region of interest from the grayscale of the image
            roiGray = self.faces.gray[x:x+w, y:y+h]
            shape = LandmarkRetriever.predictor(roiGray, rect)

            for (x, y) in shape:
                cv2.circle(self.faces.img, (x, y), 1, (0, 0, 255), -1)
    
    def showImage(self):
        cv2.imshow("Landmarks", self.faces.img)
        cv2.waitKey(0)


    @staticmethod
    def shapeToArray(shape, dtype="int"):
        # getting a list of x, y coordinates
        coords = np.zeros((68, 2), dtype=dtype)

        # looping over the landmarks and converting them to tuple
        for i in range(68):
            coords[i] = (shape.part(i).x, shape.part(i).y)

        return coords

def main():
    l = LandmarkRetriever(LandmarkRetriever.IMAGE_PATH)




