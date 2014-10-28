# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authDialog.ui'
#
# Created: Sun Oct 12 00:01:47 2014
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
        authDialog.resize(336, 243)
        authDialog.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111); color: white;"))
        authDialog.setModal(True)
        self.formLayoutWidget = QtGui.QWidget(authDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 80, 291, 61))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.usernameLabel = QtGui.QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.usernameLabel)
        self.adminUname = QtGui.QLineEdit(self.formLayoutWidget)
        self.adminUname.setStyleSheet(_fromUtf8("color:black; background: white;"))
        self.adminUname.setObjectName(_fromUtf8("adminUname"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.adminUname)
        self.adminPass = QtGui.QLineEdit(self.formLayoutWidget)
        self.adminPass.setStyleSheet(_fromUtf8("background: white; color: black;"))
        self.adminPass.setEchoMode(QtGui.QLineEdit.Password)
        self.adminPass.setObjectName(_fromUtf8("adminPass"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.adminPass)
        self.passwordLabel = QtGui.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.passwordLabel)
        self.Adminlabel = QtGui.QLabel(authDialog)
        self.Adminlabel.setGeometry(QtCore.QRect(20, 50, 261, 16))
        self.Adminlabel.setObjectName(_fromUtf8("Adminlabel"))
        self.errorDisplay = QtGui.QLabel(authDialog)
        self.errorDisplay.setGeometry(QtCore.QRect(80, 150, 171, 20))
        self.errorDisplay.setStyleSheet(_fromUtf8("color: red;"))
        self.errorDisplay.setText(_fromUtf8(""))
        self.errorDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.errorDisplay.setWordWrap(True)
        self.errorDisplay.setMargin(5)
        self.errorDisplay.setObjectName(_fromUtf8("errorDisplay"))
        self.logBtn = QtGui.QPushButton(authDialog)
        self.logBtn.setGeometry(QtCore.QRect(120, 160, 89, 23))
        self.logBtn.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111);"))
        self.logBtn.setObjectName(_fromUtf8("logBtn"))
        self.authError = QtGui.QLabel(authDialog)
        self.authError.setGeometry(QtCore.QRect(10, 200, 311, 21))
        self.authError.setStyleSheet(_fromUtf8("color: red;"))
        self.authError.setAlignment(QtCore.Qt.AlignCenter)
        self.authError.setObjectName(_fromUtf8("authError"))

        self.retranslateUi(authDialog)
        QtCore.QMetaObject.connectSlotsByName(authDialog)

    def retranslateUi(self, authDialog):
        authDialog.setWindowTitle(QtGui.QApplication.translate("authDialog", "Admin Authentication", None, QtGui.QApplication.UnicodeUTF8))
        self.usernameLabel.setText(QtGui.QApplication.translate("authDialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.passwordLabel.setText(QtGui.QApplication.translate("authDialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.Adminlabel.setText(QtGui.QApplication.translate("authDialog", "Administrator Log In", None, QtGui.QApplication.UnicodeUTF8))
        self.logBtn.setText(QtGui.QApplication.translate("authDialog", "Log In", None, QtGui.QApplication.UnicodeUTF8))
        self.authError.setText(QtGui.QApplication.translate("authDialog", "Wrong Authentication Credentials", None, QtGui.QApplication.UnicodeUTF8))

