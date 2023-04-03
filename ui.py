# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Encode(object):
    def setupUi(self, Encode):
        Encode.setObjectName("Encode")
        Encode.resize(830, 608)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Encode.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Encode)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 30, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 110, 821, 481))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.encode = QtWidgets.QPushButton(self.tab)
        self.encode.setGeometry(QtCore.QRect(620, 190, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.encode.setFont(font)
        self.encode.setObjectName("encode")
        self.input_1 = QtWidgets.QTextEdit(self.tab)
        self.input_1.setGeometry(QtCore.QRect(10, 30, 801, 141))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.input_1.setFont(font)
        self.input_1.setObjectName("input_1")
        self.encoded = QtWidgets.QTextEdit(self.tab)
        self.encoded.setGeometry(QtCore.QRect(10, 300, 801, 131))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.encoded.setFont(font)
        self.encoded.setReadOnly(True)
        self.encoded.setObjectName("encoded")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 240, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.decode = QtWidgets.QPushButton(self.tab_2)
        self.decode.setGeometry(QtCore.QRect(620, 190, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.decode.setFont(font)
        self.decode.setObjectName("decode")
        self.input_2 = QtWidgets.QTextEdit(self.tab_2)
        self.input_2.setGeometry(QtCore.QRect(10, 30, 801, 141))
        self.input_2.setObjectName("input_2")
        self.decoded = QtWidgets.QTextEdit(self.tab_2)
        self.decoded.setGeometry(QtCore.QRect(10, 300, 801, 131))
        self.decoded.setReadOnly(True)
        self.decoded.setObjectName("decoded")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 240, 91, 41))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.key_matrix = QtWidgets.QLineEdit(self.centralwidget)
        self.key_matrix.setGeometry(QtCore.QRect(540, 30, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.key_matrix.setFont(font)
        self.key_matrix.setCursorPosition(7)
        self.key_matrix.setObjectName("key_matrix")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 411, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(21)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        Encode.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Encode)
        self.statusbar.setObjectName("statusbar")
        Encode.setStatusBar(self.statusbar)

        self.retranslateUi(Encode)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Encode)

    def retranslateUi(self, Encode):
        _translate = QtCore.QCoreApplication.translate
        Encode.setWindowTitle(_translate("Encode", "Teskari matritsa"))
        self.label.setText(_translate("Encode", "KALIT"))
        self.encode.setText(_translate("Encode", "Kodlash"))
        self.input_1.setHtml(_translate("Encode", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.input_1.setPlaceholderText(_translate("Encode", "Kodlash uchun matn kiriting"))
        self.encoded.setHtml(_translate("Encode", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Encode", "Natija:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Encode", "Kodlash"))
        self.decode.setText(_translate("Encode", "Dekodlash"))
        self.input_2.setHtml(_translate("Encode", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.input_2.setPlaceholderText(_translate("Encode", "Kodlangan xabarni bu yerga kiriting"))
        self.decoded.setHtml(_translate("Encode", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Rockwell\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.label_3.setText(_translate("Encode", "Natija:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Encode", "Dekodlash"))
        self.key_matrix.setText(_translate("Encode", "1 2 2 1"))
        self.label_4.setText(_translate("Encode", "Chiziqli algebra"))