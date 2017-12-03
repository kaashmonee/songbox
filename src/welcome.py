# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import picture as picGui
import sys

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


### Instatiating global variables; they are necessary here so that the app can 
### multiple windows


class Ui_Form(QtGui.QMainWindow):
    def setupUiMain(self, Form):
        self.Form = Form
        # Form = self.Form
        # sets the object name. Form is the QWidget that is passed in.
        # QWidgets is just the thing that everyhing is added to, kind of like 
        # a canvas.
        print("Form type: ", type(Form))
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(753, 508)
        font = QtGui.QFont()
        font.setPointSize(28)
        Form.setFont(font)

        # vertical layout widget
        print("Getting to vertical layout part")
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 751, 511))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        # this is kind of weird; puts a vertical layout widget on a label...
        # investiage further

        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        # setting font sizes and font families and what have you
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Mono L"))
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)

        # not sure what this line does.
        self.label.setMouseTracking(True)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0)\n"
"\n"
""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)


        # get started button being initialized here
        self.getStartedButton = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Mono L"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.getStartedButton.setFont(font)
        self.getStartedButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 238, 0)"))
        self.getStartedButton.setObjectName(_fromUtf8("getStartedButton"))
        self.verticalLayout.addWidget(self.getStartedButton)
        # adding listener upon button click
        self.getStartedButton.clicked.connect(self.getStartedClick)

        # help button being initialized here
        self.helpButton = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Mono L"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.helpButton.setFont(font)
        self.helpButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 238, 0)"))
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.verticalLayout.addWidget(self.helpButton)

        # how done button being initialized here
        self.howDoneButton = QtGui.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Mono L"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.howDoneButton.setFont(font)
        self.howDoneButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 238, 0)"))
        self.howDoneButton.setObjectName(_fromUtf8("howDoneButton"))
        self.verticalLayout.addWidget(self.howDoneButton)

        self.retranslateMainUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateMainUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffffff;\">songbox</span></p></body></html>", None))
        self.getStartedButton.setText(_translate("Form", "Get Started", None))
        self.helpButton.setText(_translate("Form", "Help", None))
        self.howDoneButton.setText(_translate("Form", "How Was It Done?", None))

    def getStartedClick(self):
        # pictureGui = picGui.PictureGui()
        # pictureGui.show()
        # self.hide()
        self.Form = QtGui.QWidget()
        self.setupUiPictureGui(self.Form)
        # self.Form.show()

    def setupUiPictureGui(self, Form):
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
        self.takePictureButton.setStyleSheet(
            _fromUtf8("background-color: rgb(255, 238, 0)"))
        self.takePictureButton.setObjectName(_fromUtf8("takePictureButton"))

        self.Form = Form
        self.takePictureButton.clicked.connect(self.takePicture)

        self.retranslatePictureUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslatePictureUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.takePictureButton.setText(
            _translate("Form", "Take Picture", None))

    def retranslateEmotionUi(self, Form):
        # code to add the labels for the emotion pane
        pass

    def takePicture(self):
        import pygame.camera
        # init the camera
        pygame.camera.init()
        # taking the picture by init the camera location 
        # i suspect once i get opencv working, this function will become obsolet
        cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
        # sleeping -- giving time for the camera to warm upon
        time.sleep()
        cam.start()
        # grabbing hte image
        img = cam.get_image()
        import pygame.image
        pygame.image.save(img, "./src/assets/captured.png")
        cam.stop()

        self.insertImage()

        self.bringUpImageAndFacialFeatures(self)

        self.bringUpEmotionWindow()

    def bringUpEmotionWindow(self):
        emotionWindow = emotion.EmotionGui()
        emotionWindow.show()

    def bringUpImageAndFacialFeatures(self):
        retriever = getlandmarks.LandmarksRetriever()
        retriever.showImage()

    def runWhichForm(self, Form):
        import sys
        global app
        app = QtGui.QApplication(sys.argv)
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exe_())




if __name__ == "__main__":
    import sys
    global app 
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUiMain(Form)
    Form.show()
    sys.exit(app.exec_())

