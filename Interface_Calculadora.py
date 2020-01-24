# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_interface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Janela_inteira(object):
    def setupUi(self, Janela_inteira):
        Janela_inteira.setObjectName("Janela_inteira")
        Janela_inteira.setEnabled(True)
        Janela_inteira.resize(236, 328)
        self.label = QtWidgets.QLabel(Janela_inteira)
        self.label.setGeometry(QtCore.QRect(20, 10, 200, 50))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setStyleSheet("QLabel {\n"
                                 "  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
                                 "  border: 1px solid gray;\n"
                                 "}\n"
                                 "background-color : white;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 50, 50))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "  background-color: rgb(215, 215, 215);\n"
                                      "  border: 1px solid gray;\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 70, 50, 50))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "  background-color: rgb(215, 215, 215);\n"
                                        "  border: 1px solid gray;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 70, 50, 50))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "  background-color: rgb(215, 215, 215);\n"
                                        "  border: 1px solid gray;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 120, 50, 50))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "  background-color: rgb(0,255,255);\n"
                                        "  color: black; \n"
                                        "  border: 1px solid gray;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 120, 50, 50))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
                                        "   border: 1px solid gray;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                        "}\n"
                                        "")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 120, 50, 50))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
                                        "   border: 1px solid gray;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                        "}\n"
                                        "")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 120, 50, 50))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
                                        "   border: 1px solid gray;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                        "}\n"
                                        "")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_8.setGeometry(QtCore.QRect(170, 170, 50, 50))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
                                        "  background-color: rgb(0,255,255);\n"
                                        "  color: black; \n"
                                        "  border: 1px solid gray;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
                                        "}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 170, 50, 50))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
                                        "   border: 1px solid gray;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                        "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                        "}\n"
                                        "")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_10.setGeometry(QtCore.QRect(70, 170, 50, 50))
        self.pushButton_10.setStyleSheet("QPushButton {\n"
                                         "   border: 1px solid gray;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                         "}\n"
                                         "")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_11.setGeometry(QtCore.QRect(120, 170, 50, 50))
        self.pushButton_11.setStyleSheet("QPushButton {\n"
                                         "   border: 1px solid gray;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                         "}\n"
                                         "")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_12.setGeometry(QtCore.QRect(170, 220, 50, 50))
        self.pushButton_12.setStyleSheet("QPushButton {\n"
                                         "  background-color: rgb(0,255,255);\n"
                                         "  color: black; \n"
                                         "  border: 1px solid gray;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
                                         "}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 220, 50, 50))
        self.pushButton_13.setStyleSheet("QPushButton {\n"
                                         "   border: 1px solid gray;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                         "}\n"
                                         "")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_14.setGeometry(QtCore.QRect(70, 220, 50, 50))
        self.pushButton_14.setStyleSheet("QPushButton {\n"
                                         "   border: 1px solid gray;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                         "}\n"
                                         "")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_15.setGeometry(QtCore.QRect(120, 220, 50, 50))
        self.pushButton_15.setStyleSheet("QPushButton {\n"
                                         "   border: 1px solid gray;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                         "}\n"
                                         "")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_17 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_17.setGeometry(QtCore.QRect(20, 270, 100, 50))
        self.pushButton_17.setStyleSheet("QPushButton {\n"
                                         "   border: 1px solid gray;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                         "}\n"
                                         "")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_19 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_19.setGeometry(QtCore.QRect(120, 270, 50, 50))
        self.pushButton_19.setStyleSheet("QPushButton {\n"
                                         "  background-color: rgb(215, 215, 215);\n"
                                         "  border: 1px solid gray;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
                                         "}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_20.setGeometry(QtCore.QRect(170, 270, 50, 50))
        self.pushButton_20.setStyleSheet("QPushButton {\n"
                                         "  background-color: rgb(0,255,255);\n"
                                         "  color: black; \n"
                                         "  border: 1px solid gray;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
                                         "}")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_16 = QtWidgets.QPushButton(Janela_inteira)
        self.pushButton_16.setGeometry(QtCore.QRect(170, 70, 50, 50))
        self.pushButton_16.setStyleSheet("QPushButton {\n"
                                         "  background-color: rgb(0,255,255);\n"
                                         "  color: black; \n"
                                         "  border: 1px solid gray;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                         "                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
                                         "}")
        self.pushButton_16.setObjectName("pushButton_16")

        self.retranslateUi(Janela_inteira)
        QtCore.QMetaObject.connectSlotsByName(Janela_inteira)

    def retranslateUi(self, Janela_inteira):
        _translate = QtCore.QCoreApplication.translate
        Janela_inteira.setWindowTitle(_translate("Janela_inteira", "Calculadora"))
        self.setWindowIcon(QIcon('img/icon.png'))

        self.label.setText(_translate("Janela_inteira", "0"))
        self.pushButton.setText(_translate("Janela_inteira", "C"))
        self.pushButton_2.setText(_translate("Janela_inteira", "+/-"))
        self.pushButton_3.setText(_translate("Janela_inteira", "%"))
        self.pushButton_4.setText(_translate("Janela_inteira", "x"))
        self.pushButton_5.setText(_translate("Janela_inteira", "9"))
        self.pushButton_6.setText(_translate("Janela_inteira", "8"))
        self.pushButton_7.setText(_translate("Janela_inteira", "7"))
        self.pushButton_8.setText(_translate("Janela_inteira", "+"))
        self.pushButton_9.setText(_translate("Janela_inteira", "4"))
        self.pushButton_10.setText(_translate("Janela_inteira", "5"))
        self.pushButton_11.setText(_translate("Janela_inteira", "6"))
        self.pushButton_12.setText(_translate("Janela_inteira", "-"))
        self.pushButton_13.setText(_translate("Janela_inteira", "1"))
        self.pushButton_14.setText(_translate("Janela_inteira", "2"))
        self.pushButton_15.setText(_translate("Janela_inteira", "3"))
        self.pushButton_17.setText(_translate("Janela_inteira", "0"))
        self.pushButton_19.setText(_translate("Janela_inteira", "."))
        self.pushButton_20.setText(_translate("Janela_inteira", "="))
        self.pushButton_16.setText(_translate("Janela_inteira", "÷"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Janela_inteira = QtWidgets.QWidget()
    ui = Ui_Janela_inteira()
    ui.setupUi(Janela_inteira)
    Janela_inteira.show()
    sys.exit(app.exec_())
