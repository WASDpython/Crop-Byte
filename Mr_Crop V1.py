import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import sys
from ui import Ui_Crop_Byte
from Wel_ui import Ui_Crop_Bytee
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class UI_WC(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Crop_Bytee()
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.showCropp)

    def showCropp(self):
        self.mw = Ui()
        self.mw.show()
        self.hide()

class Ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Crop_Byte()
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.ui.setupUi(self)
        self.ui.movie = QtGui.QMovie("Crop_GIF.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.pushButton.clicked.connect(self.showCrop)

    def showCrop(self):
        excel = pd.read_excel('Crop_Data.xlsx', header = 0)
        le = preprocessing.LabelEncoder()
        crop = le.fit_transform(list(excel["CROP"]))                                                      
        NITROGEN = list(excel["NITROGEN"])
        PHOSPHORUS = list(excel["PHOSPHORUS"])
        POTASSIUM = list(excel["POTASSIUM"])
        TEMPERATURE = list(excel["TEMPERATURE"])
        HUMIDITY = list(excel["HUMIDITY"])
        PH = list(excel["PH"])
        RAINFALL = list(excel["RAINFALL"])

        self.features = list(zip(NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL))
        self.features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL])
        self.features = self.features.transpose()
        self.model = KNeighborsClassifier(n_neighbors=3)
        self.model.fit(self.features, crop)

        predict = np.array([int(self.ui.lineEdit_8.text()),int(self.ui.lineEdit_2.text()),int(self.ui.lineEdit_3.text()),int(self.ui.lineEdit_4.text()),
        int(self.ui.lineEdit_5.text()),float(self.ui.lineEdit_6.text()),int(self.ui.lineEdit_7.text())]) 
        print(predict)
        predict = predict.reshape(1,-1)
        print(predict) 
        predict = self.model.predict(predict)
        print(predict)

        crop_name = str()
        if predict == 0:
            crop_name = 'Apple'
        elif predict == 1:
            crop_name = 'Banana'
        elif predict == 2:
            crop_name = 'Blackgram'
        elif predict == 3:
            crop_name = 'Chickpea'
        elif predict == 4:
            crop_name = 'Coconut'
        elif predict == 5:
            crop_name = 'Coffee'
        elif predict == 6:
            crop_name = 'Cotton'
        elif predict == 7:
            crop_name = 'Grapes'
        elif predict == 8:
            crop_name = 'Jute'
        elif predict == 9:
            crop_name = 'Kidneybeans'
        elif predict == 10:
            crop_name = 'Lentil'
        elif predict == 11:
            crop_name = 'Maize'
        elif predict == 12:
            crop_name = 'Mango'
        elif predict == 13:
            crop_name = 'Mothbeans'
        elif predict == 14:
            crop_name = 'Mungbeans'
        elif predict == 15:
            crop_name = 'Muskmelon'
        elif predict == 16:
            crop_name = 'Orange'
        elif predict == 17:
            crop_name = 'Papaya'
        elif predict == 18:
            crop_name = 'Pigeonpeas'
        elif predict == 19:
            crop_name = 'Pomegranate'
        elif predict == 20:
            crop_name = 'Rice'
        elif predict == 21:
            crop_name = 'Watermelon'

        self.ui.textBrowser_8.setText(crop_name)


app = QApplication(sys.argv)
project = UI_WC()
project.show()
exit(app.exec_())