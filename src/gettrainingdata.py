import utils
import csv
import time
import os
from getlandmarks import LandmarkRetriever


class DataGetter:

    possibleEmotions = [("angry", 0), ("disgust", 1), ("fear", 2), ("happy", 3),
                        ("sad", 4), ("surprise", 5), ("neutral", 6)]
    # (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral)

    # path to add camera captured data to
    csvPath = "./assets/cameradata.csv"

    facialDatasetPath = "./assets/fer2013/fer2013.csv"

    def __init__(self):
        pass

    def getDataFromCamera(self):

        done = False

        while not done:

            # opening csv csvFile
            with open(DataGetter.csvPath, "a") as csvFile:
                # looping through possible emotions, taking picture, analyzing, and
                # writing to csv file
                for key, value in DataGetter.possibleEmotions:
                    print("Taking picture in 2 seconds! Please make this face:", key)
                    # keeps going until picture is successfully taken
                    landmarks = ""
                    retriever = ""
                    while True:
                        try:
                            utils.takePicture("./assets/temp.png")
                            print(
                                "Picture", DataGetter.possibleEmotions[value][0], "taken")
                            # emotionNum = input("Please select emotion:\nangry=0\ndisgust=1"
                            #                    "\nfear=2\nhappy=3\nsad=4\nsurprise=5\nneutral=6")
                            retriever = LandmarkRetriever("./assets/temp.png")
                            landmarks = retriever.getLandmarks()
                        except Exception as e:
                            print("No face deteced! Trying again!")
                            # time.sleep(2)
                            continue
                        break

                    writer = csv.writer(csvFile)
                    writer.writerow(landmarks.tolist() + [value])

            response = input("Would you like to erase and try again? [Y/n] ")
            # if the user would like to retrain, then they can do this
            if response.lower() == "y":
                self.undoLastPass()
            else:
                done = True
                print("Data recorded")

    def getDataFromFacialDataset(self):
        # not sure how i'm going to parse this.
        # a few things i have to do here:
        # 1. pass into opencv to get the location of the face
        # 2. if a face is detectable, then just get features, ez
        # 3. if a face is not detectable, then you're fucked.
        pass

    def undoLastPass(self):

        with open(DataGetter.csvPath, "r") as csvFile:
            lines = csvFile.readlines()
            # removing the last 7 lines
            lines = lines[:-7]

        with open(DataGetter.csvPath, "w") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(lines)


if __name__ == "__main__":
    print(os.getcwd())
    d = DataGetter()
    d.getDataFromCamera()
