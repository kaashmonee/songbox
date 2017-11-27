import sys
from PyQt4 import QtGui, QtCore
import cv2
import pygame
import pygame.camera
import time
# QtCore is used for event handling things



class SongDash(QtGui.QMainWindow):
    # basically I can call different functions to open and trigger different 
    # pages
    MUSIC_ICON = "./src/assets/musicalnote.png"
    def __init__(self):
        super().__init__()
        # determines where on the screen it it will show up and how big the 
        self.width = 500
        self.height = 500
        # screen should be
        self.setGeometry(5,5,self.width, self.height)
        self.actions = dict()
        self.setWindowTitle("SongBox")
        # setting a window icon (definitely change later)
        self.setWindowIcon(QtGui.QIcon(SongDash.MUSIC_ICON))

        # creating a menu item
        extractAction = QtGui.QAction("&Quit the app", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the app")
        extractAction.triggered.connect(self.closeApplication)
        # appending file to dictionary
        self.actions["QuitAppFile"] = extractAction

        #creating a new menu item
        action2 = QtGui.QAction("&Add button", self)
        action2.setShortcut("Ctrl+B")
        extractAction.setStatusTip("Creating button.")
        extractAction.triggered.connect(self.createButton)
        self.actions["createButton"] = action2
        
        # add the menu item to the previous item
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)
        fileMenu.addAction(self.actions["createButton"])

        self.statusBar()

        self.home()
    
    # shows the window
    def _show(self): self.show()

    # this is for a particular page in the GUI (the home page)
    def home(self):
        btn = QtGui.QPushButton("Take Picture", self)
        # if the button is clicked, finds instance of QCore application and 
        # quits

        # size hint resizes it to whatever size it thinks is appropriate
        btn.resize(btn.sizeHint())
        btn.move(self.width/2, self.height/2)
        # binding buttons to custom functions 
        btn.clicked.connect(self.takePicture)
        #QtCore.QCoreApplication.instance().quit)
        # self.show()

        # creating a toolar
        self.toolBar = self.addToolBar("Testing toolbar")
        # self.toolBar.addAction(getChe)

        # checkbox
        checkBox = QtGui.QCheckBox("Check the box!")
        # it will run the printSomething function
        checkBox.stateChanged.connect(self.printSomething)

    def songs(self):
        pass

    def closeApplication(self):
        # print("Custom functionular region!")
        choice = QtGui.QMessageBox.question(self, "Quitting!", 
                                            "Really quit?",
                                            QtGui.QMessageBox.Yes | 
                                            QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Exiting!")
            sys.exit()
        else:
            pass
        # sys.exit()

    def createButton(self):
        print("Create button getting triggered")
        btn = QtGui.QPushButton("New Button", self)
        btn.move(200, 200)
        btn.resize(btn.sizeHint())

    def printSomething(self):
        label = QtGui.QLabel()
        label.setText("Testing label!")
        label.setAlignment(Qt.AlignCenter)

    def takePicture(self):
        import pygame.camera
        pygame.camera.init()
        # taking the image by initializing the camera location
        cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
        # sleeping
        time.sleep(2)
        cam.start()
        # grabbing the image
        img = cam.get_image()
        import pygame.image
        # saving the image
        pygame.image.save(img, "./src/assets/captured.png")
        cam.stop()



# main function for testing purposes
# this file will probably be imported elsewhere, but main function is here for 
# testing
def main(): 
    app = QtGui.QApplication(sys.argv)
    dash = SongDash()
    dash._show()
    app.exec_()

if __name__ == "__main__":
    main()
