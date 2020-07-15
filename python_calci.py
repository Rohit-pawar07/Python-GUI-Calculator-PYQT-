# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calci.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import background
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(539, 545)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/JVI FINAL PROJECT/logoicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:#1C2833;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Textfield = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Textfield.setGeometry(QtCore.QRect(20, 30, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Textfield.setFont(font)
        self.Textfield.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Textfield.setStyleSheet("background-color:#FBFCFC;")
        self.Textfield.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Textfield.setPlainText("")
        self.Textfield.setOverwriteMode(True)
        self.Textfield.setObjectName("Textfield")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(20, 160, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.button_7.setFont(font)
        self.button_7.setAutoFillBackground(False)
        self.button_7.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_7.setObjectName("button_7")
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(150, 160, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.button_8.setFont(font)
        self.button_8.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_8.setFlat(False)
        self.button_8.setObjectName("button_8")
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(280, 160, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.button_9.setFont(font)
        self.button_9.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_9.setObjectName("button_9")
        self.button_div = QtWidgets.QPushButton(self.centralwidget)
        self.button_div.setGeometry(QtCore.QRect(420, 160, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.button_div.setFont(font)
        self.button_div.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"\n"
"")
        self.button_div.setObjectName("button_div")
        self.button_multi = QtWidgets.QPushButton(self.centralwidget)
        self.button_multi.setGeometry(QtCore.QRect(422, 260, 91, 61))
        self.button_multi.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_multi.setObjectName("button_multi")
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(280, 260, 91, 61))
        self.button_6.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_6.setObjectName("button_6")
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(150, 260, 93, 61))
        self.button_5.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_5.setObjectName("button_5")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(20, 260, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.button_4.setFont(font)
        self.button_4.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_4.setObjectName("button_4")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(20, 360, 93, 61))
        self.button_1.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"\n"
"")
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(150, 360, 93, 61))
        self.button_2.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(280, 360, 93, 61))
        self.button_3.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_3.setObjectName("button_3")
        self.button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.button_minus.setGeometry(QtCore.QRect(420, 360, 93, 61))
        self.button_minus.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_minus.setObjectName("button_minus")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(20, 460, 93, 61))
        self.button_0.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_0.setObjectName("button_0")
        self.button_dot = QtWidgets.QPushButton(self.centralwidget)
        self.button_dot.setGeometry(QtCore.QRect(150, 460, 93, 61))
        self.button_dot.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_dot.setObjectName("button_dot")
        self.button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.button_plus.setGeometry(QtCore.QRect(280, 460, 93, 61))
        self.button_plus.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_plus.setObjectName("button_plus")
        self.button_equal = QtWidgets.QPushButton(self.centralwidget)
        self.button_equal.setGeometry(QtCore.QRect(420, 460, 93, 61))
        self.button_equal.setStyleSheet("box-shadow:inset 0px 1px 3px 0px #91b8b3;\n"
"    background:linear-gradient(to bottom, #768d87 5%, #6c7c7c 100%);\n"
"    background-color:#768d87;\n"
"    border-radius:10px;\n"
"    border:2px solid #566963;\n"
"    display:inline-block;\n"
"    cursor:pointer;\n"
"    color:#ffffff;\n"
"    font-family:Arial;\n"
"    font-size:25px;\n"
"    font-weight:bold;\n"
"    padding:14px 0px;\n"
"    text-decoration:none;\n"
"    text-shadow:0px -1px 10px #2b665e;\n"
"}\n"
".myButton:hover {\n"
"    background:linear-gradient(to bottom, #6c7c7c 5%, #768d87 100%);\n"
"    background-color:#6c7c7c;\n"
"}\n"
".myButton:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"")
        self.button_equal.setObjectName("button_equal")
        self.label_back = QtWidgets.QLabel(self.centralwidget)
        self.label_back.setGeometry(QtCore.QRect(-10, -10, 551, 631))
        self.label_back.setStyleSheet("background-image:url(:/newPrefix/backgroun2.jpg)\n"
"")
        self.label_back.setObjectName("label_back")
        self.label_back.raise_()
        self.Textfield.raise_()
        self.button_7.raise_()
        self.button_8.raise_()
        self.button_9.raise_()
        self.button_div.raise_()
        self.button_multi.raise_()
        self.button_6.raise_()
        self.button_5.raise_()
        self.button_4.raise_()
        self.button_1.raise_()
        self.button_2.raise_()
        self.button_3.raise_()
        self.button_minus.raise_()
        self.button_0.raise_()
        self.button_dot.raise_()
        self.button_plus.raise_()
        self.button_equal.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Calculator Application"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_div.setText(_translate("MainWindow", "/"))
        self.button_multi.setText(_translate("MainWindow", "*"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_dot.setText(_translate("MainWindow", "."))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_equal.setText(_translate("MainWindow", "="))
        self.label_back.setText(_translate("MainWindow", "TextLabel"))
 #import background-image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
