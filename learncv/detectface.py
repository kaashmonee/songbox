import numpy as np
import cv2


# hold training data
def main():
    # getting the classifiers that come with opencv
    faceCascade = cv2.CascadeClassifier("./learncv/assets/classifiers/haarcascade_frontalface_default.xml")
    eyeCascade = cv2.CascadeClassifier("./learncv/assets/classifiers/haarcascade_eye.xml")

    img = cv2.imread("./learncv/assets/myface.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # not sure what this line does
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roiGray = gray[y:y+h, x:x+w]
        roiColor = img[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(roiGray)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roiColor, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        cv2.imshow("My Face", img)

if __name__ == "__main__":
    main()
