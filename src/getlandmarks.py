import cv2, stasm


def main():
    imgpath = "./learncv/assets/guywitheyes.jpg"
    img = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)
    landmarks = stasm.search_single(img)
    print(landmarks)

if __name__ == "__main__":
    main()
