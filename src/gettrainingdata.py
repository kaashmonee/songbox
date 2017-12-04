import utils
import csv
import time
import os
from getlandmarks import LandmarkRetriever

class DataGetter:

    possibleEmotions = {"angry": 0, "disgust": 1, "fear": 2, "happy": 3,
                        "sad": 4, "surprise": 5, "neutral": 6}
    # (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral)

    # path to add camera captured data to
    csvPath = "./assets/cameradata.csv"
    
    def __init__(self):
        pass


    def getDataFromCamera(self):

        # opening csv csvFile
        with open(DataGetter.csvPath, "w") as csvFile:
            # looping through possible emotions, taking picture, analyzing, and 
            # writing to csv file
            for key in DataGetter.possibleEmotions:
                print("Taking picture in 2 seconds! Please make this face:", key)
                utils.takePicture("./assets/temp.png")
                print("Picture", DataGetter.possibleEmotions[key], "taken")
                # emotionNum = input("Please select emotion:\nangry=0\ndisgust=1"
                #                    "\nfear=2\nhappy=3\nsad=4\nsurprise=5\nneutral=6")
                retriever = LandmarkRetriever("./assets/temp.png")
                landmarks = retriever.getLandmarks()

                csv.writer(csvFile).writerow([landmarks] + [DataGetter.possibleEmotions[key]])
        
        




        

        
        
            
            
            


if __name__=="__main__":
    print(os.getcwd())
    d = DataGetter()
    d.getDataFromCamera()
