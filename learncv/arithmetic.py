import cv2
import numpy as np

def arithmeticOperations():
    blendImages()

def blendImages():
    img1 = cv2.imread("./learncv/assets/basketball.png")
    img2 = cv2.imread("./learncv/assets/lebron.jpg")

    roi1 = img1[0:0, 100:100]
    roi2 = img2[0:0, 100:100]

    weight1, weight2, = 0.7, 0.3
    imageSum = cv2.addWeighted(roi1, weight1, roi2, weight2, 0)

    cv2.imshow("combined images", imageSum)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    arithmeticOperations()

if __name__ == "__main__":
    main()