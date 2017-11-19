import cv2
import numpy as np


def playWithPixels():
    # getting the image
    img = cv2.imread("./assets/basketball.png")

    print(type(img))

    # returns numpy array with BGR values at specified pixel location
    px = img[100, 100]

    # accessing only the blue pixel (not sure how this works)
    # specifically, what is the 3rd parameter? oh shit nevermind, i get it now
    # the third parameter is the parameter associated with B=0,G=1,R=2
    blue = img[100, 100, 0]
    print(blue)

    ## Modifying pixels ##

    # modifies the red value of the pixel at 10, 10 to 100
    img.itemset((10, 10, 2), 100)

    print("red value after setting:", img.item(10, 10, 2))

    print(px)

    print("image shape:", img.shape)
    print("image size:", img.size)

    # getting the image datatype
    print("img datatype:", img.dtype)

    # manipulating certain colors in the image:
    print("Setting all the reds in the image to 0 using Numpy indexing:")
    img[:,:,2] = 0



def main():
    playWithPixels()


if __name__ == "__main__":
    main()
