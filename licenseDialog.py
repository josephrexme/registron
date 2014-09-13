# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'licenseDialog.ui'
#
# Created: Sat Sep 13 15:55:14 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_licenseDialog(object):
    def setupUi(self, licenseDialog):
        licenseDialog.setObjectName(_fromUtf8("licenseDialog"))
        licenseDialog.resize(591, 550)
        licenseDialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(licenseDialog)
        self.buttonBox.setGeometry(QtCore.QRect(240, 510, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.licenseInfo = QtGui.QLabel(licenseDialog)
        self.licenseInfo.setGeometry(QtCore.QRect(10, 30, 571, 471))
        self.licenseInfo.setStyleSheet(_fromUtf8("color:white;"))
        self.licenseInfo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.licenseInfo.setObjectName(_fromUtf8("licenseInfo"))

        self.retranslateUi(licenseDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), licenseDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), licenseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(licenseDialog)

    def retranslateUi(self, licenseDialog):
        licenseDialog.setWindowTitle(QtGui.QApplication.translate("licenseDialog", "MIT License", None, QtGui.QApplication.UnicodeUTF8))
        self.licenseInfo.setText(QtGui.QApplication.translate("licenseDialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">The MIT License (MIT)</span></p><p align=\"center\">Copyright (c) 2014 Registron</p><p align=\"center\">Permission is hereby granted, free of charge, to any person obtaining a copy</p><p align=\"center\">of this software and associated documentation files (the &quot;Software&quot;), to deal</p><p align=\"center\">in the Software without restriction, including without limitation the rights</p><p align=\"center\">to use, copy, modify, merge, publish, distribute, sublicense, and/or sell</p><p align=\"center\">copies of the Software, and to permit persons to whom the Software is</p><p align=\"center\">furnished to do so, subject to the following conditions:</p><p align=\"center\">The above copyright notice and this permission notice shall be included in all</p><p align=\"center\">copies or substantial portions of the Software.</p><p align=\"center\"><br/></p><p align=\"center\">THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR</p><p align=\"center\">IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,</p><p align=\"center\">FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE</p><p align=\"center\">AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER</p><p align=\"center\">LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,</p><p align=\"center\">OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE</p><p align=\"center\">SOFTWARE.<br/></p><p align=\"center\"><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

