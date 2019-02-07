# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\assets\UI\Layout\DB_Creator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Creator(object):
    def setupUi(self, Creator):
        Creator.setObjectName("Creator")
        Creator.setWindowModality(QtCore.Qt.ApplicationModal)
        Creator.resize(873, 602)
        Creator.setMinimumSize(QtCore.QSize(644, 602))
        self.centralwidget = QtWidgets.QWidget(Creator)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.f_collection = QtWidgets.QLineEdit(self.centralwidget)
        self.f_collection.setMinimumSize(QtCore.QSize(280, 30))
        self.f_collection.setMaximumSize(QtCore.QSize(290, 30))
        self.f_collection.setObjectName("f_collection")
        self.gridLayout.addWidget(self.f_collection, 12, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(280, 20))
        self.label_5.setMaximumSize(QtCore.QSize(280, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(280, 20))
        self.label_6.setMaximumSize(QtCore.QSize(280, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(280, 20))
        self.label_7.setMaximumSize(QtCore.QSize(280, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 11, 1, 1, 2)
        self.pattern_combo = QtWidgets.QComboBox(self.centralwidget)
        self.pattern_combo.setMinimumSize(QtCore.QSize(280, 30))
        self.pattern_combo.setMaximumSize(QtCore.QSize(290, 30))
        self.pattern_combo.setObjectName("pattern_combo")
        self.pattern_combo.addItem("")
        self.pattern_combo.addItem("")
        self.gridLayout.addWidget(self.pattern_combo, 8, 1, 1, 2)
        self.f_comment = QtWidgets.QLineEdit(self.centralwidget)
        self.f_comment.setMinimumSize(QtCore.QSize(280, 30))
        self.f_comment.setMaximumSize(QtCore.QSize(290, 30))
        self.f_comment.setObjectName("f_comment")
        self.gridLayout.addWidget(self.f_comment, 10, 1, 1, 2)
        self.execute = QtWidgets.QPushButton(self.centralwidget)
        self.execute.setMinimumSize(QtCore.QSize(330, 50))
        self.execute.setObjectName("execute")
        self.gridLayout.addWidget(self.execute, 13, 0, 1, 1)
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setMinimumSize(QtCore.QSize(280, 50))
        self.create.setMaximumSize(QtCore.QSize(290, 50))
        self.create.setObjectName("create")
        self.gridLayout.addWidget(self.create, 13, 1, 1, 2, QtCore.Qt.AlignVCenter)
        self.table_name = QtWidgets.QLineEdit(self.centralwidget)
        self.table_name.setMinimumSize(QtCore.QSize(281, 30))
        self.table_name.setMaximumSize(QtCore.QSize(290, 30))
        self.table_name.setObjectName("table_name")
        self.gridLayout.addWidget(self.table_name, 1, 1, 1, 2)
        self.code_preview = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.code_preview.setMinimumSize(QtCore.QSize(330, 480))
        self.code_preview.setObjectName("code_preview")
        self.gridLayout.addWidget(self.code_preview, 0, 0, 13, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(280, 30))
        self.label_2.setMaximumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(280, 30))
        self.label.setMaximumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 2)
        self.field_name = QtWidgets.QLineEdit(self.centralwidget)
        self.field_name.setMinimumSize(QtCore.QSize(280, 30))
        self.field_name.setMaximumSize(QtCore.QSize(290, 30))
        self.field_name.setObjectName("field_name")
        self.gridLayout.addWidget(self.field_name, 3, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(160, 30))
        self.label_3.setMaximumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.databox = QtWidgets.QComboBox(self.centralwidget)
        self.databox.setMinimumSize(QtCore.QSize(160, 30))
        self.databox.setMaximumSize(QtCore.QSize(160, 30))
        self.databox.setObjectName("databox")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.databox.addItem("")
        self.gridLayout.addWidget(self.databox, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(124, 30))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.datavalue = QtWidgets.QLineEdit(self.centralwidget)
        self.datavalue.setMinimumSize(QtCore.QSize(110, 30))
        self.datavalue.setMaximumSize(QtCore.QSize(124, 30))
        self.datavalue.setObjectName("datavalue")
        self.gridLayout.addWidget(self.datavalue, 5, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(290, 126))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.unsigned_2 = QtWidgets.QCheckBox(self.groupBox)
        self.unsigned_2.setGeometry(QtCore.QRect(10, 20, 270, 30))
        self.unsigned_2.setMaximumSize(QtCore.QSize(270, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.unsigned_2.setFont(font)
        self.unsigned_2.setIconSize(QtCore.QSize(25, 25))
        self.unsigned_2.setTristate(False)
        self.unsigned_2.setObjectName("unsigned_2")
        self.allownull = QtWidgets.QCheckBox(self.groupBox)
        self.allownull.setGeometry(QtCore.QRect(10, 50, 270, 30))
        self.allownull.setMaximumSize(QtCore.QSize(270, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.allownull.setFont(font)
        self.allownull.setIconSize(QtCore.QSize(25, 25))
        self.allownull.setTristate(False)
        self.allownull.setObjectName("allownull")
        self.zerofill = QtWidgets.QCheckBox(self.groupBox)
        self.zerofill.setGeometry(QtCore.QRect(10, 80, 270, 30))
        self.zerofill.setMaximumSize(QtCore.QSize(270, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.zerofill.setFont(font)
        self.zerofill.setIconSize(QtCore.QSize(25, 25))
        self.zerofill.setTristate(False)
        self.zerofill.setObjectName("zerofill")
        self.gridLayout.addWidget(self.groupBox, 6, 1, 1, 2)
        self.groupBox.raise_()
        self.table_name.raise_()
        self.field_name.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.databox.raise_()
        self.label_4.raise_()
        self.datavalue.raise_()
        self.pattern_combo.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.f_comment.raise_()
        self.f_collection.raise_()
        self.label_7.raise_()
        self.code_preview.raise_()
        self.create.raise_()
        self.execute.raise_()
        Creator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Creator)
        QtCore.QMetaObject.connectSlotsByName(Creator)
        Creator.setTabOrder(self.code_preview, self.table_name)
        Creator.setTabOrder(self.table_name, self.field_name)
        Creator.setTabOrder(self.field_name, self.databox)
        Creator.setTabOrder(self.databox, self.datavalue)
        Creator.setTabOrder(self.datavalue, self.unsigned_2)
        Creator.setTabOrder(self.unsigned_2, self.allownull)
        Creator.setTabOrder(self.allownull, self.zerofill)
        Creator.setTabOrder(self.zerofill, self.pattern_combo)
        Creator.setTabOrder(self.pattern_combo, self.f_comment)
        Creator.setTabOrder(self.f_comment, self.f_collection)
        Creator.setTabOrder(self.f_collection, self.create)
        Creator.setTabOrder(self.create, self.execute)

    def retranslateUi(self, Creator):
        _translate = QtCore.QCoreApplication.translate
        Creator.setWindowTitle(_translate("Creator", "MainWindow"))
        self.f_collection.setText(_translate("Creator", "utf8_general_ci"))
        self.label_5.setText(_translate("Creator", "Pattern:"))
        self.label_6.setText(_translate("Creator", "Comment:"))
        self.label_7.setText(_translate("Creator", "Collection"))
        self.pattern_combo.setItemText(0, _translate("Creator", "N/A"))
        self.pattern_combo.setItemText(1, _translate("Creator", "AUTO_INCREMENT"))
        self.execute.setText(_translate("Creator", "EXECUTE CREATE CODE"))
        self.execute.setShortcut(_translate("Creator", "F9"))
        self.create.setText(_translate("Creator", "CREATE CODE"))
        self.create.setShortcut(_translate("Creator", "Return"))
        self.label_2.setText(_translate("Creator", "Table name:"))
        self.label.setText(_translate("Creator", "Field name:"))
        self.label_3.setText(_translate("Creator", "Data type:"))
        self.databox.setItemText(0, _translate("Creator", "TINYINT"))
        self.databox.setItemText(1, _translate("Creator", "SMALLINT"))
        self.databox.setItemText(2, _translate("Creator", "MEDIUMINT"))
        self.databox.setItemText(3, _translate("Creator", "INT"))
        self.databox.setItemText(4, _translate("Creator", "BIGINT"))
        self.databox.setItemText(5, _translate("Creator", "BIT"))
        self.databox.setItemText(6, _translate("Creator", "FLOAT"))
        self.databox.setItemText(7, _translate("Creator", "DOUBLE"))
        self.databox.setItemText(8, _translate("Creator", "DECIMAL"))
        self.databox.setItemText(9, _translate("Creator", "CHAR"))
        self.databox.setItemText(10, _translate("Creator", "VARCHAR"))
        self.databox.setItemText(11, _translate("Creator", "TINYTEXT"))
        self.databox.setItemText(12, _translate("Creator", "MEDIUMTEXT"))
        self.databox.setItemText(13, _translate("Creator", "LONGTEXT"))
        self.databox.setItemText(14, _translate("Creator", "JSON"))
        self.databox.setItemText(15, _translate("Creator", "BINARY"))
        self.databox.setItemText(16, _translate("Creator", "VARBINARY"))
        self.databox.setItemText(17, _translate("Creator", "BLOB"))
        self.databox.setItemText(18, _translate("Creator", "MEDIUMBLOB"))
        self.databox.setItemText(19, _translate("Creator", "LONGBLOB"))
        self.databox.setItemText(20, _translate("Creator", "DATE"))
        self.databox.setItemText(21, _translate("Creator", "TIME"))
        self.databox.setItemText(22, _translate("Creator", "YEAR"))
        self.databox.setItemText(23, _translate("Creator", "DATETIME"))
        self.databox.setItemText(24, _translate("Creator", "TIMESTAMP"))
        self.databox.setItemText(25, _translate("Creator", "POINT"))
        self.databox.setItemText(26, _translate("Creator", "LINESTRING"))
        self.databox.setItemText(27, _translate("Creator", "POLYGON"))
        self.databox.setItemText(28, _translate("Creator", "GEOMETRY"))
        self.databox.setItemText(29, _translate("Creator", "MULTIPOINT"))
        self.databox.setItemText(30, _translate("Creator", "MULTILINESTRING"))
        self.databox.setItemText(31, _translate("Creator", "MULTIPOLYGON"))
        self.databox.setItemText(32, _translate("Creator", "GEOMETRYCOLLECTION"))
        self.databox.setItemText(33, _translate("Creator", "ENUM"))
        self.databox.setItemText(34, _translate("Creator", "SET"))
        self.label_4.setText(_translate("Creator", "Value:"))
        self.groupBox.setTitle(_translate("Creator", "Booleans"))
        self.unsigned_2.setText(_translate("Creator", "Unsigned"))
        self.allownull.setText(_translate("Creator", "Allow NULL"))
        self.zerofill.setText(_translate("Creator", "ZEROFILL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Creator = QtWidgets.QMainWindow()
    ui = Ui_Creator()
    ui.setupUi(Creator)
    Creator.show()
    sys.exit(app.exec_())

