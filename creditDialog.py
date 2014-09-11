# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creditDialog.ui'
#
# Created: Thu Sep 11 11:23:36 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_creditDialog(object):
    def setupUi(self, creditDialog):
        creditDialog.setObjectName(_fromUtf8("creditDialog"))
        creditDialog.resize(416, 260)
        creditDialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(creditDialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 220, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.creditInfo = QtGui.QLabel(creditDialog)
        self.creditInfo.setGeometry(QtCore.QRect(20, 50, 371, 141))
        self.creditInfo.setStyleSheet(_fromUtf8("color:white;"))
        self.creditInfo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.creditInfo.setObjectName(_fromUtf8("creditInfo"))

        self.retranslateUi(creditDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), creditDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), creditDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(creditDialog)

    def retranslateUi(self, creditDialog):
        creditDialog.setWindowTitle(QtGui.QApplication.translate("creditDialog", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.creditInfo.setText(QtGui.QApplication.translate("creditDialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Credits</span></p><p align=\"center\"><span style=\" font-weight:600;\">Project Lead:</span> James Olanipekun</p><p align=\"center\"><span style=\" font-weight:600;\">Project Supervisor:</span> Mr. Fagbolu</p><p align=\"center\"><span style=\" font-weight:600;\">Developer:</span> Joseph Rex</p><p align=\"center\"><span style=\" font-weight:600;\">Development Machine Name:</span> noxiux<br/></p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

