import sys
from PyQt4 import QtGui


app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
print("reachign here")

window.show()
print("something not happening here.")
app.exec_()