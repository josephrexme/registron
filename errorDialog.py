# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errorDialog.ui'
#
# Created: Sun Oct 12 00:36:55 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_errorDialog(object):
    def setupUi(self, errorDialog):
        errorDialog.setObjectName(_fromUtf8("errorDialog"))
        errorDialog.resize(416, 192)
        errorDialog.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111);"))
        errorDialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(errorDialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.databox = QtGui.QLabel(errorDialog)
        self.databox.setGeometry(QtCore.QRect(20, 50, 371, 91))
        self.databox.setStyleSheet(_fromUtf8("color:white;background: rgb(10, 80, 111);"))
        self.databox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.databox.setObjectName(_fromUtf8("databox"))

        self.retranslateUi(errorDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), errorDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), errorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(errorDialog)

    def retranslateUi(self, errorDialog):
        errorDialog.setWindowTitle(QtGui.QApplication.translate("errorDialog", "Program Error", None, QtGui.QApplication.UnicodeUTF8))
        self.databox.setText(QtGui.QApplication.translate("errorDialog", "<html><head/><body><p align=\"center\"><img src=\":/images/resources/images/48x48/registron.png\"/></p><p align=\"center\"><span style=\" font-weight:600;\">REGISTRON DATA FILE IS MISSING</span></p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import app_rc
