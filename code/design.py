from PyQt6 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1168, 958)
        MainWindow.setMinimumSize(QtCore.QSize(1168, 958))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(247, 248, 251);")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setStyleSheet("font: 18pt \"PT Sans\";\n"
                                      "border: 1px solid rgb(180, 180, 180);\n"
                                      "border-radius: 20px;\n"
                                      "background-color: rgb(214, 214, 214);\n"
                                      "padding-right: 100px;\n"
                                      "padding-left: 100px;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.total_time = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.total_time.setStyleSheet("font: 18pt \"PT Sans\";\n"
                                      "background-color: rgb(235, 235, 235);")
        self.total_time.setObjectName("total_time")
        self.gridLayout.addWidget(self.total_time, 0, 1, 1, 1)

        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setStyleSheet("border: 2px solid #000;\n"
                                "margin-top: 50px;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 2)

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.power = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.power.setStyleSheet("font: 18pt \"PT Sans\";\n"
                                 "background-color: rgb(235, 235, 235);")
        self.power.setObjectName("power")
        self.gridLayout.addWidget(self.power, 2, 1, 1, 1)

        self.planet = QtWidgets.QComboBox(parent=self.centralwidget)
        self.planet.setStyleSheet("font: 16pt \"PT Sans\";\n"
                                  "text-decoration: underline;\n"
                                  "border: 1px solid  rgb(171, 171, 171);\n"
                                  "background-color: #FFF;")
        self.planet.setObjectName("planet")
        self.gridLayout.addWidget(self.planet, 5, 1, 1, 1)

        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.height_n = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.height_n.setStyleSheet("font: 16pt \"PT Sans\";\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border: 1px solid  rgb(171, 171, 171);")
        self.height_n.setObjectName("height_n")
        self.gridLayout.addWidget(self.height_n, 7, 1, 1, 1)

        self.weight = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.weight.setStyleSheet("font: 16pt \"PT Sans\";\n"
                                  "background-color: rgb(255, 255, 255);\n"
                                  "border: 1px solid  rgb(171, 171, 171);")
        self.weight.setText("")
        self.weight.setObjectName("weight")
        self.gridLayout.addWidget(self.weight, 6, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)

        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.weight_n = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.weight_n.setStyleSheet("font: 18pt \"PT Sans\";\n"
                                    "background-color: rgb(235, 235, 235);")
        self.weight_n.setObjectName("weight_n")
        self.gridLayout.addWidget(self.weight_n, 3, 1, 1, 1)

        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.max_speed = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.max_speed.setStyleSheet("font: 18pt \"PT Sans\";\n"
                                     "background-color: rgb(235, 235, 235);")
        self.max_speed.setObjectName("max_speed")
        self.gridLayout.addWidget(self.max_speed, 1, 1, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.speed = PlotWidget(parent=self.centralwidget)
        self.speed.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.speed.setObjectName("speed")
        self.gridLayout_3.addWidget(self.speed, 1, 0, 1, 1)

        self.length = PlotWidget(parent=self.centralwidget)
        self.length.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.length.setObjectName("length")
        self.gridLayout_3.addWidget(self.length, 1, 1, 1, 1)

        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 1, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gravity calculator"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))
        self.label_4.setText(_translate("MainWindow", "Сила тяготения на высоте, Н"))
        self.label.setText(_translate("MainWindow", "Введите массу, кг *"))
        self.label_3.setText(_translate("MainWindow", "Общее время падения, с"))
        self.label_5.setText(_translate("MainWindow", "Выберите место *"))
        self.label_2.setText(_translate("MainWindow", "Введите высоту, м"))
        self.label_6.setText(_translate("MainWindow", "Сила тяготения на поверхносте, Н"))
        self.label_9.setText(_translate("MainWindow", "Максимальная скорость, м/c"))
        self.label_7.setText(_translate("MainWindow", "График скорости"))
        self.label_8.setText(_translate("MainWindow", "График расстояния"))
