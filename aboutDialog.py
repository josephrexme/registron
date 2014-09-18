# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutDialog.ui'
#
# Created: Thu Sep 18 10:30:16 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(416, 260)
        AboutDialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 220, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.aboutInfo = QtGui.QLabel(AboutDialog)
        self.aboutInfo.setGeometry(QtCore.QRect(20, 50, 371, 141))
        self.aboutInfo.setStyleSheet(_fromUtf8("color:white;"))
        self.aboutInfo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.aboutInfo.setObjectName(_fromUtf8("aboutInfo"))

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AboutDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About Registron", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutInfo.setText(QtGui.QApplication.translate("AboutDialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">About Registron</span></p><p align=\"center\">Registron is a speech based student registration system.</p><p align=\"center\">It uses the Python pyttsx module for providing a voice.</p><p align=\"center\">Graphical Interface built with Qt4</p><p align=\"center\">Website: https://bl4ckdu5t.github.io/registron</p><p align=\"center\">© 2014 ostrich-dev works<br/></p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

