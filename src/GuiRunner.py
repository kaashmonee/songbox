from PyQt4 import QtCore, QtGui
import picture as picGui
import sys

import welcome

class MainGui(QDialog, welcome.Ui_Form):
    super(MainDialog, self).__init__(parent)
    self.setupUi(self)