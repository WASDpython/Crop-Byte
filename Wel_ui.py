from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Crop_Bytee(object):
    def setupUi(self, Crop_Byte):
        Crop_Byte.setObjectName("Crop_Byte")
        Crop_Byte.resize(800, 617)
        self.centralwidget = QtWidgets.QWidget(Crop_Byte)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 621))
        self.label.setStyleSheet("background-color: rgb(62, 0, 188);\n"
"border: transparent;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 260, 721, 141))
        font = QtGui.QFont()
        font.setFamily("Tarrget")
        font.setPointSize(72)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 500, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Mechanismo")
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 10, 401, 241))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        # self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        # self.progressBar.setGeometry(QtCore.QRect(350, 450, 118, 23))
        # self.progressBar.setProperty("value", 0)
        # self.progressBar.setInvertedAppearance(False)
        # self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        # self.progressBar.setObjectName("progressBar")
        Crop_Byte.setCentralWidget(self.centralwidget)

        self.retranslateUi(Crop_Byte)
        QtCore.QMetaObject.connectSlotsByName(Crop_Byte)

    def retranslateUi(self, Crop_Byte):
        _translate = QtCore.QCoreApplication.translate
        Crop_Byte.setWindowTitle(_translate("Crop_Byte", "Crop Byte"))
        self.label_2.setText(_translate("Crop_Byte", "Crop Byte"))
        self.pushButton.setText(_translate("Crop_Byte", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Crop_Byte = QtWidgets.QMainWindow()
    ui = Ui_Crop_Bytee()
    ui.setupUi(Crop_Byte)
    Crop_Byte.show()
    sys.exit(app.exec_())
