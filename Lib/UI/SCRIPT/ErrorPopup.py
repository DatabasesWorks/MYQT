# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Lib\UI\LAYOUT\ErrorPopup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(339, 126)
        self.ok = QtWidgets.QPushButton(Error)
        self.ok.setGeometry(QtCore.QRect(240, 88, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        self.console_out = QtWidgets.QTextBrowser(Error)
        self.console_out.setGeometry(QtCore.QRect(0, 0, 340, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.console_out.setFont(font)
        self.console_out.setStyleSheet("padding:10;background-color:white;color:red;")
        self.console_out.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.console_out.setObjectName("console_out")

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)
        Error.setTabOrder(self.console_out, self.ok)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "Erro"))
        self.ok.setText(_translate("Error", "Ok"))
        self.console_out.setHtml(_translate("Error", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Error = QtWidgets.QWidget()
    ui = Ui_Error()
    ui.setupUi(Error)
    Error.show()
    sys.exit(app.exec_())

