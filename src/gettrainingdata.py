import utils

class DataGetter:

    possibleEmotions = {"angry": 0, "disgust": 1, "fear": 2, "happy": 3,
                        "sad": 4, "surprise": 5, "neutral": 6}
    # (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral)
    
    def __init__(self):
        pass

    def getDataFromCamera(self):
        numPics = input("How many pictures would you like to take?")
        curPic = 1
        while curPic < numPics:
            print("Taking picture")
            pic = utils.takePicture(False)
            print("Picture", curPic, "taken")
            emotionNum = input("Please select emotion:\nangry=0\ndisgust=1"
                               "\nfear=2\nhappy=3\nsad=4\nsurprise=5\nneutral=6")
            
            


if __name__=="__main__":
    d = DataGetter()
    d.getData()
