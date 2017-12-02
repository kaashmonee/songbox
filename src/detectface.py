import numpy as np
import cv2
import os
import dlib

# hold training data

class FaceDetector:
    FACE_CASCADE_CLASSIFIER_PATH = (
        "./learncv/assets/classifiers/haarcascade_frontalface_default.xml"
    )

    EYE_CASCADE_CLASSIFIER_PATH = (
        "./learncv/assets/classifiers/haarcascade_eye.xml"
    )

    # getting the frontal face detector
    dlibDetector = dlib.get_frontal_face_detector()

    def __init__(self, image):
        self.faceCascade = cv2.CascadeClassifier(
            FaceDetector.FACE_CASCADE_CLASSIFIER_PATH
        )
        # print(self.faceCascade)s
        self.eyesCascade = cv2.CascadeClassifier(
            FaceDetector.EYE_CASCADE_CLASSIFIER_PATH
        )

        self.readImage(image)
        # self.getFacesAndEyes()
    
    def readImage(self, image):
        self.img = cv2.imread(image)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.faces = self.faceCascade.detectMultiScale(self.gray, 1.3, 5)
        # uses dlib instead of opencv...i think this might resolve the issue
        # ive been having. 
        self.dlibfaces = FaceDetector.dlibDetector(self.gray, 0)

    def getRegionsOfInterest(self):
        pass

    def showFace(self):
        # if there are no faces, then it shits itself and crashes...will 
        # fix this later to ensure that it lets the user know
        # self.faces = self.faceCascade.detectMultiScale(self.gray, 1.3, 5)
        print("getting here")
        if len(self.faces) == 0:
            raise Exception("Couldn't detect face in image...please select"
                            " new image!")
        
        # print("self.faces", self.faces, "self.eyes", self.eyes)

        for (x, y, w, h) in self.faces:
            # creates a rectangle for all the faces in the image

            cv2.rectangle(self.img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # creates a gray and a color image. the roi stands for 
            # region of interest
            self.roiGray = self.gray[y:y + h, x:x + w]
            self.roiColor = self.img[y:y + h, x:x + w]
            # for each x, y, w, h in the eyes, create rectangles
            self.eyes = self.eyesCascade.detectMultiScale(self.roiGray)

            for (ex, ey, ew, eh) in self.eyes[:2]:
                cv2.rectangle(self.roiColor, (ex, ey), 
                             (ex+ew, ey+eh), (0, 255, 2), 2)
            # show the image
            cv2.imshow("Face", self.img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def hasFaces(self):
        # self.showFace()
        return True if len(self.faces) != 0 else False

    def getROIColor(self):
        return self.roiColor
    
    def getROIGray(self):
        return self.roiGray
    
def main():
    f = FaceDetector("./src/assets/captured.png")
    print(f.getROIColor, f.getROIGray)
    f.showFace()


    
# """ 
# def main():
#     # print("This is running.")
#     # getting the classifiers that come with opencv

#     faceCascadeClassifierPath = (
#         "./learncv/assets/classifiers/haarcascade_frontalface_default.xml"
#     )

#     eyeCascadeClassifierPath = (
#         "./learncv/assets/classifiers/haarcascade_eye.xml"
#     )
    
#     print("cur path:", os.getcwd())

#     faceCascade = cv2.CascadeClassifier(faceCascadeClassifierPath)
#     # print("face cascade", faceCascade)
#     eyeCascade = cv2.CascadeClassifier(eyeCascadeClassifierPath)
#     # print("eyeCascade", eyeCascade)
    
#     # print("This is running")
    
#     img = cv2.imread("./learncv/assets/images/twopeoplewitheyes.png")
#     # gray = cv2.imread("./learncv/assets/images/myface.jpg", 0)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # print("This is running.")

#     # not sure what this line does
#     faces = faceCascade.detectMultiScale(gray, 1.3, 5)
#     # detect multiscale does the detection and faceCascade is the classifier
#     print(faces)
#     for (x, y, w, h) in faces:
#         print("x, y, w, h", x, y, w, h)
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#         roiGray = gray[y:y+h, x:x+w]
#         roiColor = img[y:y+h, x:x+w]
#         eyes = eyeCascade.detectMultiScale(roiGray)

#         for (ex, ey, ew, eh) in eyes[:2]:
#             print("eyes:", ex, ey, ew, eh)
#             cv2.rectangle(roiColor, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    
#     cv2.imshow("My Face", img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# """

if __name__ == "__main__":
    main()
