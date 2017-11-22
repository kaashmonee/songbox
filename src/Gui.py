import sys
from PyQt4 import QtGui, QtCore
# QtCore is used for event handling things



class SongDash(QtGui.QMainWindow):
    # basically I can call different functions to open and trigger different 
    # pages
    MUSIC_ICON = "./src/assets/musicalnote.png"
    def __init__(self):
        super().__init__()
        # determines where on the screen it it will show up and how big the 
        # screen should be
        self.setGeometry(50, 50, 500, 500)
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
        btn = QtGui.QPushButton("Quit", self)
        # if the button is clicked, finds instance of QCore application and 
        # quits

        # size hint resizes it to whatever size it thinks is appropriate
        btn.resize(btn.sizeHint())
        btn.move(100, 100)
        # binding buttons to custom functions 
        btn.clicked.connect(self.closeApplication)
        #QtCore.QCoreApplication.instance().quit)
        # self.show()

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
