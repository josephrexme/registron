# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authDialog.ui'
#
# Created: Thu Sep 11 11:57:06 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_authDialog(object):
    def setupUi(self, authDialog):
        authDialog.setObjectName(_fromUtf8("authDialog"))
        authDialog.resize(416, 260)
        authDialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(authDialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 220, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.adminUser = QtGui.QTextEdit(authDialog)
        self.adminUser.setGeometry(QtCore.QRect(50, 70, 321, 31))
        self.adminUser.setObjectName(_fromUtf8("adminUser"))
        self.adminPass = QtGui.QTextEdit(authDialog)
        self.adminPass.setGeometry(QtCore.QRect(50, 140, 321, 31))
        self.adminPass.setObjectName(_fromUtf8("adminPass"))
        self.userLabel = QtGui.QLabel(authDialog)
        self.userLabel.setGeometry(QtCore.QRect(50, 50, 121, 16))
        self.userLabel.setObjectName(_fromUtf8("userLabel"))
        self.passLabel = QtGui.QLabel(authDialog)
        self.passLabel.setGeometry(QtCore.QRect(50, 120, 71, 16))
        self.passLabel.setObjectName(_fromUtf8("passLabel"))

        self.retranslateUi(authDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), authDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), authDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(authDialog)

    def retranslateUi(self, authDialog):
        authDialog.setWindowTitle(QtGui.QApplication.translate("authDialog", "Admin Authentication", None, QtGui.QApplication.UnicodeUTF8))
        self.userLabel.setText(QtGui.QApplication.translate("authDialog", "Admin Username", None, QtGui.QApplication.UnicodeUTF8))
        self.passLabel.setText(QtGui.QApplication.translate("authDialog", "Password", None, QtGui.QApplication.UnicodeUTF8))

