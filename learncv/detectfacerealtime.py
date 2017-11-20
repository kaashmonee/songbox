import cv2
import sys
import utils



def main():
    # captures face from default webcam on computer (the one in front of me rn)
    faceCascade = cv2.CascadeClassifier(utils.FACE_CASCADE_CLASSIFIER_PATH)
    eyeCascade = cv2.CascadeClassifier(utils.EYE_CASCADE_CLASSIFIER_PATH)
    
    videoCapture = cv2.VideoCapture(-1)
    print("Video capture:", videoCapture)
    videoCapture.open(-1)
    # print(videoCapture)

    while True:
        # reads stuff in from the video camera
        print("video capture reading:", videoCapture.read())
        ret, frame = videoCapture.read()
        ## BUG -- the frame object is None, but the videocapture object is still
        # there. not sure what the issue is.
        print("frame:",frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # not entirely sure what these parameters are for
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # getting the part of the image that contains only the eyes
            roiGray = gray[y:y + h, x:x + w]
            roiColor = frame[y:y + h, x:x + w]
            eyes = eyeCascade.detectMultiScale(roiGray)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roiColor, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        cv2.imshow("frame", gray)

        if cv2.waitKey(1) and 0xFF == ord("q"):
            break
    videoCapture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
