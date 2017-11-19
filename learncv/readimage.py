import numpy as np
import cv2
import random


def loadImage():
    # load a color image as grayscale
    img = cv2.imread("./learncv/assets/basketball.png", 0)

    # showing the image
    cv2.imshow("image", img)
    # waiting indefinitely for a keystroke, and captures keystroke
    k = cv2.waitKey(0)
    # depending on what k is, it does certain things
    # if k = 27, (esc key) it destroys everything
    if k == 27:
        cv2.destroyAllWindows()
    # if k is the s key, it will save and close windows
    elif k == ord("s"):
        cv2.imwrite("./learncv/assets/grayscale.png", img)
        cv2.destroyAllWindows()
    print("reaching here")


def main():
    functions = dict()
    functions[1] = loadImage
    functions[1]()


if __name__ == "__main__":
    main()
