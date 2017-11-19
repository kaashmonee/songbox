import numpy as np
import cv2
import os

# hold training data
def main():
    # print("This is running.")
    # getting the classifiers that come with opencv

    faceCascadeClassifierPath = (
        "./learncv/assets/classifiers/haarcascade_frontalface_default.xml"
    )

    eyeCascadeClassifierPath = (
        "./learncv/assets/classifiers/haarcascade_eye.xml"
    )
    
    print("cur path:", os.getcwd())

    faceCascade = cv2.CascadeClassifier(faceCascadeClassifierPath)
    # print("face cascade", faceCascade)
    eyeCascade = cv2.CascadeClassifier(eyeCascadeClassifierPath)
    # print("eyeCascade", eyeCascade)
    
    # print("This is running")
    
    img = cv2.imread("./learncv/assets/images/twopeoplewitheyes.png")
    # gray = cv2.imread("./learncv/assets/images/myface.jpg", 0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # print("This is running.")

    # not sure what this line does
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    # detect multiscale does the detection and faceCascade is the classifier
    print(faces)
    for (x, y, w, h) in faces:
        print("x, y, w, h", x, y, w, h)
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roiGray = gray[y:y+h, x:x+w]
        roiColor = img[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(roiGray)

        for (ex, ey, ew, eh) in eyes[:2]:
            print("eyes:", ex, ey, ew, eh)
            cv2.rectangle(roiColor, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    
    cv2.imshow("My Face", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
