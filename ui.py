# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mr_Crop_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Crop_Byte(object):
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
        self.label.setPixmap(QtGui.QPixmap("Crop_GIF.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 601, 101))
        font = QtGui.QFont()
        font.setFamily("Tarrget")
        font.setPointSize(60)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(480, 170, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(680, 180, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(430, 330, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(300, 330, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(160, 180, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 470, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Mechanismo")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(15, 190, 41);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(260, 550, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.textBrowser_8.setFont(font)
        self.textBrowser_8.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(255, 0, 0);\n"
"border: transparent;")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(330, 180, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_14.setObjectName("label_14")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(490, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(660, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 390, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(430, 390, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 260, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 210, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.label_2.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.pushButton.raise_()
        self.label_14.raise_()
        self.label_12.raise_()
        self.textBrowser_8.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_7.raise_()
        self.lineEdit_8.raise_()
        self.label_3.raise_()
        Crop_Byte.setCentralWidget(self.centralwidget)

        self.retranslateUi(Crop_Byte)
        QtCore.QMetaObject.connectSlotsByName(Crop_Byte)

    def retranslateUi(self, Crop_Byte):
        _translate = QtCore.QCoreApplication.translate
        Crop_Byte.setWindowTitle(_translate("Crop_Byte", "Crop Byte"))
        self.label_2.setText(_translate("Crop_Byte", "Crop Byte"))
        self.label_6.setText(_translate("Crop_Byte", "Nitrogen"))
        self.label_7.setText(_translate("Crop_Byte", "Temperature in"))
        self.label_8.setText(_translate("Crop_Byte", "Humidity"))
        self.label_9.setText(_translate("Crop_Byte", "Rainfall in mm"))
        self.label_10.setText(_translate("Crop_Byte", "PH"))
        self.label_12.setText(_translate("Crop_Byte", "Phosphorus"))
        self.pushButton.setText(_translate("Crop_Byte", "Submit"))
        self.label_14.setText(_translate("Crop_Byte", "Potassium"))
        self.label_3.setText(_translate("Crop_Byte", "*C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Crop_Byte = QtWidgets.QMainWindow()
    ui = Ui_Crop_Byte()
    ui.setupUi(Crop_Byte)
    Crop_Byte.show()
    sys.exit(app.exec_())