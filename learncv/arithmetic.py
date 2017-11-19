import cv2
import numpy as np

def arithmeticOperations():
    blendImages()

def blendImages():
    img1 = cv2.imread("./learncv/assets/basketball.png")
    img2 = cv2.imread("./learncv/assets/lebron.jpg")

    roi1 = img1[50:75, 110:135]
    roi2 = img2[50:75, 110:135]
    print("type of roi:", type(roi1))

    weight1, weight2, = 0.7, 0.3
    imageSum = cv2.addWeighted(roi1, weight1, roi2, weight2, 0)

    cv2.imshow("combined images", imageSum)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    arithmeticOperations()

if __name__ == "__main__":
    main()