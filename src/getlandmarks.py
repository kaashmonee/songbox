from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import argparse
from detectface import FaceDetector




# def main():
#     imgpath = "./learncv/assets/guywitheyes.jpg"
#     img = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)
#     landmarks = stasm.search_single(img)
#     print(landmarks)

# if __name__ == "__main__":
#     main()


# detector = dlib.get_frontal_face_detector()

## READ
## self.facesImage is the image in which we are trying to detect faces and 
# facial landmarks

class LandmarkRetriever:

    # class attributes
    LANDMARKS_CLASSIFIER = "./src/assets/shape_predictor_68_face_landmarks.dat"
    IMAGE_PATH = "./src/assets/captures.png"
    predictor = dlib.shape_predictor(LANDMARKS_CLASSIFIER)


    def __init__(self, image=IMAGE_PATH):
        self.facesImage = FaceDetector(image)
        self.faceCoordinates = None
        if not self.facesImage.hasFaces():
            raise Exception("No faces found! Please select another image.")
        self.getLandmarks()
        
    def getLandmarks(self):
        for rect in self.facesImage.dlibfaces:
            # rect = dlib.rectangle(left=x, top=y, right=x+w, bottom=y+h)
            # gets the region of interest from the grayscale of the image
            # roiGray = self.facesImage.gray[x:x+w, y:y+h]
            shape = LandmarkRetriever.predictor(self.facesImage.gray, rect)
            print("Getting here")
            self.faceCoordinates = LandmarkRetriever.shapeToArray(shape)
            for (x, y) in LandmarkRetriever.shapeToArray(shape):
                print("x:", x, "y:", y)
                cv2.circle(self.facesImage.img, (x, y), 1, (0, 0, 255), -1)
    
    def showImage(self):
        cv2.imshow("Landmarks", self.facesImage.img)
        cv2.waitKey(0)

    # function inspired from Aiden Rosebrock
    # converts shape object to numpy array
    @staticmethod
    def shapeToArray(shape, dtype="int"):
        # getting a list of x, y coordinates
        coords = np.zeros((68, 2), dtype=dtype)

        # looping over the landmarks and converting them to tuple
        for i in range(68):
            coords[i] = (shape.part(i).x, shape.part(i).y)

        return coords

def main():
    # import sys; print(sys.version_info)
    l = LandmarkRetriever(LandmarkRetriever.IMAGE_PATH)
    l.showImage()

if __name__ == "__main__":
    main()




