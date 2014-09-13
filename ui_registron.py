# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Sep 13 14:13:07 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(747, 516)
        MainWindow.setMinimumSize(QtCore.QSize(329, 218))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("resources/images/48x48/registron.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.registronLabel = QtGui.QLabel(self.centralwidget)
        self.registronLabel.setGeometry(QtCore.QRect(250, 50, 261, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.registronLabel.setFont(font)
        self.registronLabel.setStyleSheet(_fromUtf8("color: white;"))
        self.registronLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.registronLabel.setObjectName(_fromUtf8("registronLabel"))
        self.registronDesc = QtGui.QLabel(self.centralwidget)
        self.registronDesc.setGeometry(QtCore.QRect(220, 140, 331, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.registronDesc.setFont(font)
        self.registronDesc.setStyleSheet(_fromUtf8("color: white"))
        self.registronDesc.setAlignment(QtCore.Qt.AlignCenter)
        self.registronDesc.setObjectName(_fromUtf8("registronDesc"))
        self.enterMatricLabel = QtGui.QLabel(self.centralwidget)
        self.enterMatricLabel.setGeometry(QtCore.QRect(210, 230, 341, 31))
        self.enterMatricLabel.setStyleSheet(_fromUtf8("color:white"))
        self.enterMatricLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.enterMatricLabel.setObjectName(_fromUtf8("enterMatricLabel"))
        self.proceedBtn = QtGui.QPushButton(self.centralwidget)
        self.proceedBtn.setGeometry(QtCore.QRect(270, 330, 231, 41))
        self.proceedBtn.setObjectName(_fromUtf8("proceedBtn"))
        self.matricInput = QtGui.QTextEdit(self.centralwidget)
        self.matricInput.setGeometry(QtCore.QRect(230, 280, 301, 31))
        self.matricInput.setStyleSheet(_fromUtf8("background:white;color: black;"))
        self.matricInput.setObjectName(_fromUtf8("matricInput"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 747, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuAdministrators = QtGui.QMenu(self.menubar)
        self.menuAdministrators.setObjectName(_fromUtf8("menuAdministrators"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionCredits = QtGui.QAction(MainWindow)
        self.actionCredits.setObjectName(_fromUtf8("actionCredits"))
        self.actionSignIn = QtGui.QAction(MainWindow)
        self.actionSignIn.setObjectName(_fromUtf8("actionSignIn"))
        self.menuMenu.addAction(self.actionQuit)
        self.menuMenu.addSeparator()
        self.menuAdministrators.addAction(self.actionSignIn)
        self.menuAdministrators.addSeparator()
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionCredits)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAdministrators.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Registron", None, QtGui.QApplication.UnicodeUTF8))
        self.registronLabel.setToolTip(QtGui.QApplication.translate("MainWindow", "Registron student program", None, QtGui.QApplication.UnicodeUTF8))
        self.registronLabel.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Registron</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.registronDesc.setText(QtGui.QApplication.translate("MainWindow", "Student\'s course registration program", None, QtGui.QApplication.UnicodeUTF8))
        self.enterMatricLabel.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Enter your Matriculation Number/Campus ID:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.proceedBtn.setText(QtGui.QApplication.translate("MainWindow", "Proceed to course registration", None, QtGui.QApplication.UnicodeUTF8))
        self.matricInput.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Application", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdministrators.setTitle(QtGui.QApplication.translate("MainWindow", "Administrator", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit registron", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Exit this program", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDocumentation.setText(QtGui.QApplication.translate("MainWindow", "Online Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDocumentation.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About Registron", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCredits.setText(QtGui.QApplication.translate("MainWindow", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCredits.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSignIn.setText(QtGui.QApplication.translate("MainWindow", "Manage Accounts", None, QtGui.QApplication.UnicodeUTF8))

