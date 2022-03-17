# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sobre.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class sobre(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(394, 362)
        Form.setMinimumSize(QtCore.QSize(394, 362))
        Form.setMaximumSize(QtCore.QSize(394, 362))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/hacker.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.551, y1:1, x2:0.546, y2:0, stop:0 rgba(206, 190, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 43))
        font = QtGui.QFont()
        font.setFamily("Noto Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 161))
        self.label.setMaximumSize(QtCore.QSize(16777215, 161))
        self.label.setStyleSheet("image: url(:/newPrefix/img/aguia.svg);\n"
"background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setEnabled(True)
        self.textEdit.setStyleSheet("background-color: rgb(234, 223, 105);")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MathJax_Math")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BUSCA EMPREGO CAMPINAS - GREGÓRIO HONORATO"))
        self.label_6.setText(_translate("Form", "SOBRE O SISTEMA"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p>GREGÓRIO HONORATO</p><p>DESENVOLVIMENTO DE SISTEMAS</p><p>TELEGRAM: @GREGHONO</p><p>WHATS: (19) 99250-9913</p></body></html>"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">SOFTWARE PARA AUXILIAR NA BUSCA DE EMPREGO NA REGIÃO DE CAMPINAS.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">GREGÓRIO HONORATO</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "SISTEMA DESENVOLVIDO POR:\n"
"GREGHONO@GMAIL.COM"))

import recursos

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = sobre()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
