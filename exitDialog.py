# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exitDialog.ui'
#
# Created: Thu Sep 11 13:35:36 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_exitDialog(object):
    def setupUi(self, exitDialog):
        exitDialog.setObjectName(_fromUtf8("exitDialog"))
        exitDialog.resize(384, 168)
        exitDialog.setModal(True)
        self.exitConfirm = QtGui.QLabel(exitDialog)
        self.exitConfirm.setGeometry(QtCore.QRect(30, 60, 331, 31))
        self.exitConfirm.setStyleSheet(_fromUtf8("color:white;"))
        self.exitConfirm.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.exitConfirm.setObjectName(_fromUtf8("exitConfirm"))
        self.yesExit = QtGui.QDialogButtonBox(exitDialog)
        self.yesExit.setGeometry(QtCore.QRect(200, 130, 81, 27))
        self.yesExit.setStandardButtons(QtGui.QDialogButtonBox.Yes)
        self.yesExit.setObjectName(_fromUtf8("yesExit"))
        self.noExit = QtGui.QDialogButtonBox(exitDialog)
        self.noExit.setGeometry(QtCore.QRect(290, 130, 81, 27))
        self.noExit.setStandardButtons(QtGui.QDialogButtonBox.No)
        self.noExit.setObjectName(_fromUtf8("noExit"))

        self.retranslateUi(exitDialog)
        QtCore.QObject.connect(self.noExit, QtCore.SIGNAL(_fromUtf8("rejected()")), exitDialog.close)
        QtCore.QMetaObject.connectSlotsByName(exitDialog)

    def retranslateUi(self, exitDialog):
        exitDialog.setWindowTitle(QtGui.QApplication.translate("exitDialog", "Exit Application", None, QtGui.QApplication.UnicodeUTF8))
        self.exitConfirm.setText(QtGui.QApplication.translate("exitDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Are you sure you want to exit?</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

