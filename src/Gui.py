import sys
from PyQt4 import QtGui, QtCore
# QtCore is used for event handling things



class SongDash(QtGui.QWidget):
    # basically I can call different functions to open and trigger different 
    # pages
    MUSIC_ICON = "./src/assets/musicalnote.png"
    def __init__(self):
        super().__init__()
        # determines where on the screen it it will show up and how big the 
        # screen should be
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("SongBox")
        # setting a window icon (definitely change later)
        self.setWindowIcon(QtGui.QIcon(SongDash.MUSIC_ICON))
        self.home()
    
    # shows the window
    def _show(self): self.show()

    # this is for a particular page in the GUI (the home page)
    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        # if the button is clicked, finds instance of QCore application and 
        # quits
        btn.resize(100, 50)
        btn.move(100, 100)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.show()


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
