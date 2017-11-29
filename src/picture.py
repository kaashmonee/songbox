# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'picture.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# APP


class PictureGui(QtGui.QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0)"))
        self.takePictureButton = QtGui.QPushButton(Form)
        self.takePictureButton.setGeometry(QtCore.QRect(0, 200, 751, 57))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Mono L"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)


        self.takePictureButton.setFont(font)
        self.takePictureButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 238, 0)"))
        self.takePictureButton.setObjectName(_fromUtf8("takePictureButton"))

        self.Form = Form
        self.takePictureButton.clicked.connect(self.takePicture)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.takePictureButton.setText(_translate("Form", "Take Picture", None))

    def takePicture(self):
        import pygame.camera
        # print(Form)
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
        
        self.insertImage()

    def insertImage(self):
        pass


    def show(self):
        Form = QtGui.QWidget()
        ui = self
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())



if __name__ == "__main__":

    global app
    app = QtGui.QApplication(sys.argv)

    obj = PictureGui()
    obj.show()

