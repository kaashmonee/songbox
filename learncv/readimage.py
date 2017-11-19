import numpy as np
import cv2

# load a color image as grayscale
img = cv2.imread("./assets/basketball.png", 0)
#print(img)
# try:
cv2.imshow("image", img)
cv2.waitKey()
print("reaching here")
    
# except Exception as e:
#     print("reaching except statement")
#     print(e)

# print(cv2.__version__)

