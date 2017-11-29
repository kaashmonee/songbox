# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emotion.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import songplayer

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

class EmotionGui(QtGui.QMainWindow):
    def setupUi(self, songAndEmotionPanel):
        songAndEmotionPanel.setObjectName(_fromUtf8("songAndEmotionPanel"))
        songAndEmotionPanel.resize(661, 498)
        songAndEmotionPanel.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0)"))
        self.label = QtGui.QLabel(songAndEmotionPanel)
        self.label.setGeometry(QtCore.QRect(10, 0, 641, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Mono L"))
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(songAndEmotionPanel)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 311, 271))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("./src/assets/emojis/happy.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(songAndEmotionPanel)
        self.label_3.setGeometry(QtCore.QRect(20, 340, 621, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Mono L"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.checkBox = QtGui.QCheckBox(songAndEmotionPanel)
        self.checkBox.setGeometry(QtCore.QRect(350, 390, 61, 41))
        self.checkBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255)"))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.pushButton = QtGui.QPushButton(songAndEmotionPanel)
        self.pushButton.setGeometry(QtCore.QRect(370, 460, 271, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: \"red\";\n"
"color: \"white\";\n"
"font: \"nimbus mono\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        # adding listener
        self.pushButton.clicked.connect(self.playSong)

        self.retranslateUi(songAndEmotionPanel)
        QtCore.QMetaObject.connectSlotsByName(songAndEmotionPanel)

    def retranslateUi(self, songAndEmotionPanel):
        songAndEmotionPanel.setWindowTitle(_translate("songAndEmotionPanel", "Form", None))
        self.label.setText(_translate("songAndEmotionPanel", "<html><head/><body><p align=\"center\"><span style=\" font-style:normal; color:#ffffff;\">You are feeling: </span><span style=\" font-style:normal; color:#ff0000;\">Happy</span></p></body></html>", None))
        self.label_3.setText(_translate("songAndEmotionPanel", "<html><head/><body><p><span style=\" font-style:normal; color:#ffffff;\">Songs in Your Playlist:</span></p><p><span style=\" font-style:normal; color:#ffffff;\">1. Happy - Pharrell Williams</span></p></body></html>", None))
        self.checkBox.setText(_translate("songAndEmotionPanel", "Play", None))
        self.pushButton.setText(_translate("songAndEmotionPanel", "Click to Play Selected", None))

    def show(self):
        Form = QtGui.QWidget()
        ui = self
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())

    def playSong(self):
        songPath = "./src/assets/songs/happy/pharrelhappy.wav"
        player = songplayer.SongPlayer(songPath)
        player.play()

if __name__ == "__main__":
    # import sys
    # app = QtGui.QApplication(sys.argv)
    # songAndEmotionPanel = QtGui.QWidget()
    # ui = Ui_songAndEmotionPanel()
    # ui.setupUi(songAndEmotionPanel)
    # songAndEmotionPanel.show()
    # sys.exit(app.exec_())
    import sys
    global app
    app = QtGui.QApplication(sys.argv)

    obj = EmotionGui()
    obj.show()

