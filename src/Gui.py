import sys
from PyQt4 import QtGui



class SongDash(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        # determines where on the screen it it will show up and how big the 
        # screen should be
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("SongBox")
    
    # shows the window
    def _show(self): self.show()


# main function for testing purposes
def main(): 
    app = QtGui.QApplication(sys.argv)
    dash = SongDash()
    dash._show()
    app.exec_()

if __name__ == "__main__":
    main()
