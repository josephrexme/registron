# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentwindow.ui'
#
# Created: Fri Sep 19 01:42:31 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_studentWindow(object):
    def setupUi(self, studentWindow):
        studentWindow.setObjectName(_fromUtf8("studentWindow"))
        studentWindow.setEnabled(True)
        studentWindow.resize(746, 575)
        studentWindow.setMinimumSize(QtCore.QSize(329, 218))
        studentWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("resources/images/48x48/registron.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        studentWindow.setWindowIcon(icon)
        studentWindow.setWindowOpacity(1.0)
        studentWindow.setStyleSheet(_fromUtf8("background: rgb(10, 80, 111);"))
        self.centralwidget = QtGui.QWidget(studentWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.studentAvatar = QtGui.QLabel(self.centralwidget)
        self.studentAvatar.setGeometry(QtCore.QRect(20, 20, 128, 128))
        self.studentAvatar.setObjectName(_fromUtf8("studentAvatar"))
        self.schoolName = QtGui.QLabel(self.centralwidget)
        self.schoolName.setGeometry(QtCore.QRect(170, 20, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(37)
        self.schoolName.setFont(font)
        self.schoolName.setStyleSheet(_fromUtf8("color:white; font-size:20pt;font-weight:300;"))
        self.schoolName.setText(_fromUtf8(""))
        self.schoolName.setObjectName(_fromUtf8("schoolName"))
        self.studentName = QtGui.QLabel(self.centralwidget)
        self.studentName.setGeometry(QtCore.QRect(170, 60, 511, 41))
        self.studentName.setStyleSheet(_fromUtf8("color:white;font-size:25px;font-weight:280;"))
        self.studentName.setText(_fromUtf8(""))
        self.studentName.setObjectName(_fromUtf8("studentName"))
        self.matricLabel = QtGui.QLabel(self.centralwidget)
        self.matricLabel.setGeometry(QtCore.QRect(170, 110, 71, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.matricLabel.setFont(font)
        self.matricLabel.setStyleSheet(_fromUtf8("color: white;"))
        self.matricLabel.setObjectName(_fromUtf8("matricLabel"))
        self.studentID = QtGui.QLabel(self.centralwidget)
        self.studentID.setGeometry(QtCore.QRect(250, 110, 151, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.studentID.setFont(font)
        self.studentID.setStyleSheet(_fromUtf8("color: white;"))
        self.studentID.setText(_fromUtf8(""))
        self.studentID.setObjectName(_fromUtf8("studentID"))
        self.deptLabel = QtGui.QLabel(self.centralwidget)
        self.deptLabel.setGeometry(QtCore.QRect(420, 110, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.deptLabel.setFont(font)
        self.deptLabel.setStyleSheet(_fromUtf8("color: white;"))
        self.deptLabel.setObjectName(_fromUtf8("deptLabel"))
        self.studentDept = QtGui.QLabel(self.centralwidget)
        self.studentDept.setGeometry(QtCore.QRect(530, 110, 201, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.studentDept.setFont(font)
        self.studentDept.setStyleSheet(_fromUtf8("color: white;"))
        self.studentDept.setText(_fromUtf8(""))
        self.studentDept.setObjectName(_fromUtf8("studentDept"))
        self.coursesLabel = QtGui.QLabel(self.centralwidget)
        self.coursesLabel.setGeometry(QtCore.QRect(20, 160, 711, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.coursesLabel.setFont(font)
        self.coursesLabel.setStyleSheet(_fromUtf8("background:white;color:rgb(10, 80, 111);padding-right:50px;"))
        self.coursesLabel.setObjectName(_fromUtf8("coursesLabel"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(690, 0, 51, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.course1 = QtGui.QLabel(self.centralwidget)
        self.course1.setGeometry(QtCore.QRect(20, 200, 220, 50))
        self.course1.setAcceptDrops(False)
        self.course1.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course1.setFrameShadow(QtGui.QFrame.Raised)
        self.course1.setLineWidth(10)
        self.course1.setMidLineWidth(5)
        self.course1.setObjectName(_fromUtf8("course1"))
        self.course7 = QtGui.QLabel(self.centralwidget)
        self.course7.setGeometry(QtCore.QRect(20, 320, 220, 50))
        self.course7.setAcceptDrops(False)
        self.course7.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course7.setFrameShadow(QtGui.QFrame.Raised)
        self.course7.setLineWidth(10)
        self.course7.setMidLineWidth(5)
        self.course7.setObjectName(_fromUtf8("course7"))
        self.course4 = QtGui.QLabel(self.centralwidget)
        self.course4.setGeometry(QtCore.QRect(20, 260, 220, 50))
        self.course4.setAcceptDrops(False)
        self.course4.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course4.setFrameShadow(QtGui.QFrame.Raised)
        self.course4.setLineWidth(10)
        self.course4.setMidLineWidth(5)
        self.course4.setObjectName(_fromUtf8("course4"))
        self.course10 = QtGui.QLabel(self.centralwidget)
        self.course10.setGeometry(QtCore.QRect(20, 380, 220, 50))
        self.course10.setAcceptDrops(False)
        self.course10.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course10.setFrameShadow(QtGui.QFrame.Raised)
        self.course10.setLineWidth(10)
        self.course10.setMidLineWidth(5)
        self.course10.setObjectName(_fromUtf8("course10"))
        self.course2 = QtGui.QLabel(self.centralwidget)
        self.course2.setGeometry(QtCore.QRect(270, 200, 220, 50))
        self.course2.setAcceptDrops(False)
        self.course2.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course2.setFrameShadow(QtGui.QFrame.Raised)
        self.course2.setLineWidth(10)
        self.course2.setMidLineWidth(5)
        self.course2.setObjectName(_fromUtf8("course2"))
        self.course5 = QtGui.QLabel(self.centralwidget)
        self.course5.setGeometry(QtCore.QRect(270, 260, 220, 50))
        self.course5.setAcceptDrops(False)
        self.course5.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course5.setFrameShadow(QtGui.QFrame.Raised)
        self.course5.setLineWidth(10)
        self.course5.setMidLineWidth(5)
        self.course5.setObjectName(_fromUtf8("course5"))
        self.course8 = QtGui.QLabel(self.centralwidget)
        self.course8.setGeometry(QtCore.QRect(270, 320, 220, 50))
        self.course8.setAcceptDrops(False)
        self.course8.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course8.setFrameShadow(QtGui.QFrame.Raised)
        self.course8.setLineWidth(10)
        self.course8.setMidLineWidth(5)
        self.course8.setObjectName(_fromUtf8("course8"))
        self.course11 = QtGui.QLabel(self.centralwidget)
        self.course11.setGeometry(QtCore.QRect(270, 380, 220, 50))
        self.course11.setAcceptDrops(False)
        self.course11.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course11.setFrameShadow(QtGui.QFrame.Raised)
        self.course11.setLineWidth(10)
        self.course11.setMidLineWidth(5)
        self.course11.setObjectName(_fromUtf8("course11"))
        self.course3 = QtGui.QLabel(self.centralwidget)
        self.course3.setGeometry(QtCore.QRect(510, 200, 220, 50))
        self.course3.setAcceptDrops(False)
        self.course3.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course3.setFrameShadow(QtGui.QFrame.Raised)
        self.course3.setLineWidth(10)
        self.course3.setMidLineWidth(5)
        self.course3.setObjectName(_fromUtf8("course3"))
        self.course6 = QtGui.QLabel(self.centralwidget)
        self.course6.setGeometry(QtCore.QRect(510, 260, 220, 50))
        self.course6.setAcceptDrops(False)
        self.course6.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course6.setFrameShadow(QtGui.QFrame.Raised)
        self.course6.setLineWidth(10)
        self.course6.setMidLineWidth(5)
        self.course6.setObjectName(_fromUtf8("course6"))
        self.course9 = QtGui.QLabel(self.centralwidget)
        self.course9.setGeometry(QtCore.QRect(510, 320, 220, 50))
        self.course9.setAcceptDrops(False)
        self.course9.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course9.setFrameShadow(QtGui.QFrame.Raised)
        self.course9.setLineWidth(10)
        self.course9.setMidLineWidth(5)
        self.course9.setObjectName(_fromUtf8("course9"))
        self.course12 = QtGui.QLabel(self.centralwidget)
        self.course12.setGeometry(QtCore.QRect(510, 380, 220, 50))
        self.course12.setAcceptDrops(False)
        self.course12.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course12.setFrameShadow(QtGui.QFrame.Raised)
        self.course12.setLineWidth(10)
        self.course12.setMidLineWidth(5)
        self.course12.setObjectName(_fromUtf8("course12"))
        self.course13 = QtGui.QLabel(self.centralwidget)
        self.course13.setGeometry(QtCore.QRect(20, 440, 220, 50))
        self.course13.setAcceptDrops(False)
        self.course13.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course13.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course13.setFrameShadow(QtGui.QFrame.Raised)
        self.course13.setLineWidth(10)
        self.course13.setMidLineWidth(5)
        self.course13.setObjectName(_fromUtf8("course13"))
        self.course14 = QtGui.QLabel(self.centralwidget)
        self.course14.setGeometry(QtCore.QRect(270, 440, 220, 50))
        self.course14.setAcceptDrops(False)
        self.course14.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course14.setFrameShadow(QtGui.QFrame.Raised)
        self.course14.setLineWidth(10)
        self.course14.setMidLineWidth(5)
        self.course14.setObjectName(_fromUtf8("course14"))
        self.course15 = QtGui.QLabel(self.centralwidget)
        self.course15.setGeometry(QtCore.QRect(510, 440, 220, 50))
        self.course15.setAcceptDrops(False)
        self.course15.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); color: white;"))
        self.course15.setFrameShape(QtGui.QFrame.StyledPanel)
        self.course15.setFrameShadow(QtGui.QFrame.Raised)
        self.course15.setLineWidth(10)
        self.course15.setMidLineWidth(5)
        self.course15.setObjectName(_fromUtf8("course15"))
        self.verifyBtn = QtGui.QPushButton(self.centralwidget)
        self.verifyBtn.setGeometry(QtCore.QRect(530, 500, 181, 31))
        self.verifyBtn.setObjectName(_fromUtf8("verifyBtn"))
        self.courseCheck1 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck1.setGeometry(QtCore.QRect(220, 210, 16, 18))
        self.courseCheck1.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck1.setText(_fromUtf8(""))
        self.courseCheck1.setObjectName(_fromUtf8("courseCheck1"))
        self.courseCheck2 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck2.setGeometry(QtCore.QRect(470, 210, 16, 18))
        self.courseCheck2.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck2.setText(_fromUtf8(""))
        self.courseCheck2.setObjectName(_fromUtf8("courseCheck2"))
        self.courseCheck3 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck3.setGeometry(QtCore.QRect(710, 210, 16, 18))
        self.courseCheck3.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck3.setText(_fromUtf8(""))
        self.courseCheck3.setObjectName(_fromUtf8("courseCheck3"))
        self.courseCheck4 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck4.setGeometry(QtCore.QRect(220, 270, 16, 18))
        self.courseCheck4.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck4.setText(_fromUtf8(""))
        self.courseCheck4.setObjectName(_fromUtf8("courseCheck4"))
        self.courseCheck5 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck5.setGeometry(QtCore.QRect(470, 270, 16, 18))
        self.courseCheck5.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck5.setText(_fromUtf8(""))
        self.courseCheck5.setObjectName(_fromUtf8("courseCheck5"))
        self.courseCheck6 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck6.setGeometry(QtCore.QRect(710, 270, 16, 18))
        self.courseCheck6.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck6.setText(_fromUtf8(""))
        self.courseCheck6.setObjectName(_fromUtf8("courseCheck6"))
        self.courseCheck7 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck7.setGeometry(QtCore.QRect(220, 330, 16, 18))
        self.courseCheck7.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck7.setText(_fromUtf8(""))
        self.courseCheck7.setObjectName(_fromUtf8("courseCheck7"))
        self.courseCheck8 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck8.setGeometry(QtCore.QRect(470, 330, 16, 18))
        self.courseCheck8.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck8.setText(_fromUtf8(""))
        self.courseCheck8.setObjectName(_fromUtf8("courseCheck8"))
        self.courseCheck9 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck9.setGeometry(QtCore.QRect(710, 330, 16, 18))
        self.courseCheck9.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck9.setText(_fromUtf8(""))
        self.courseCheck9.setObjectName(_fromUtf8("courseCheck9"))
        self.courseCheck10 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck10.setGeometry(QtCore.QRect(220, 390, 16, 18))
        self.courseCheck10.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck10.setText(_fromUtf8(""))
        self.courseCheck10.setObjectName(_fromUtf8("courseCheck10"))
        self.courseCheck11 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck11.setGeometry(QtCore.QRect(470, 390, 16, 18))
        self.courseCheck11.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck11.setText(_fromUtf8(""))
        self.courseCheck11.setObjectName(_fromUtf8("courseCheck11"))
        self.courseCheck12 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck12.setGeometry(QtCore.QRect(710, 390, 16, 18))
        self.courseCheck12.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck12.setText(_fromUtf8(""))
        self.courseCheck12.setObjectName(_fromUtf8("courseCheck12"))
        self.courseCheck13 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck13.setGeometry(QtCore.QRect(220, 450, 16, 18))
        self.courseCheck13.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck13.setText(_fromUtf8(""))
        self.courseCheck13.setObjectName(_fromUtf8("courseCheck13"))
        self.courseCheck14 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck14.setGeometry(QtCore.QRect(470, 450, 16, 18))
        self.courseCheck14.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck14.setText(_fromUtf8(""))
        self.courseCheck14.setObjectName(_fromUtf8("courseCheck14"))
        self.courseCheck15 = QtGui.QCheckBox(self.centralwidget)
        self.courseCheck15.setGeometry(QtCore.QRect(710, 450, 16, 18))
        self.courseCheck15.setStyleSheet(_fromUtf8("background: rgb(20, 90, 131); "))
        self.courseCheck15.setText(_fromUtf8(""))
        self.courseCheck15.setObjectName(_fromUtf8("courseCheck15"))
        self.courseStatus = QtGui.QLabel(self.centralwidget)
        self.courseStatus.setGeometry(QtCore.QRect(20, 490, 331, 41))
        self.courseStatus.setStyleSheet(_fromUtf8("color: white;"))
        self.courseStatus.setObjectName(_fromUtf8("courseStatus"))
        studentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(studentWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 746, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuAdministrators = QtGui.QMenu(self.menubar)
        self.menuAdministrators.setObjectName(_fromUtf8("menuAdministrators"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        studentWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(studentWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        studentWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(studentWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionDocumentation = QtGui.QAction(studentWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionAbout = QtGui.QAction(studentWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionCredits = QtGui.QAction(studentWindow)
        self.actionCredits.setObjectName(_fromUtf8("actionCredits"))
        self.actionSignIn = QtGui.QAction(studentWindow)
        self.actionSignIn.setObjectName(_fromUtf8("actionSignIn"))
        self.actionLicense = QtGui.QAction(studentWindow)
        self.actionLicense.setObjectName(_fromUtf8("actionLicense"))
        self.actionLog_out = QtGui.QAction(studentWindow)
        self.actionLog_out.setObjectName(_fromUtf8("actionLog_out"))
        self.menuMenu.addAction(self.actionLog_out)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menuAdministrators.addAction(self.actionSignIn)
        self.menuAdministrators.addSeparator()
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionCredits)
        self.menuHelp.addAction(self.actionLicense)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAdministrators.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(studentWindow)
        QtCore.QMetaObject.connectSlotsByName(studentWindow)

    def retranslateUi(self, studentWindow):
        studentWindow.setWindowTitle(QtGui.QApplication.translate("studentWindow", "Registron", None, QtGui.QApplication.UnicodeUTF8))
        self.studentAvatar.setText(QtGui.QApplication.translate("studentWindow", "<html><head/><body><p><img src=\":/images/resources/images/128x128/joerex.jpg\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.matricLabel.setText(QtGui.QApplication.translate("studentWindow", "Matric/ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.deptLabel.setText(QtGui.QApplication.translate("studentWindow", "Department:", None, QtGui.QApplication.UnicodeUTF8))
        self.coursesLabel.setText(QtGui.QApplication.translate("studentWindow", "Courses:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("studentWindow", "<html><head/><body><p><img src=\":/images/resources/images/48x48/registron.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.course1.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course7.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course4.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course10.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course2.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course5.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course8.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course11.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course3.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course6.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course9.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course12.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course13.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course14.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.course15.setText(QtGui.QApplication.translate("studentWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.verifyBtn.setText(QtGui.QApplication.translate("studentWindow", "Save Courses", None, QtGui.QApplication.UnicodeUTF8))
        self.courseStatus.setText(QtGui.QApplication.translate("studentWindow", "Check the courses you want to offer this semester", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("studentWindow", "Application", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdministrators.setTitle(QtGui.QApplication.translate("studentWindow", "Administrator", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("studentWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("studentWindow", "Quit registron", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setStatusTip(QtGui.QApplication.translate("studentWindow", "Exit this program", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("studentWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDocumentation.setText(QtGui.QApplication.translate("studentWindow", "Online Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDocumentation.setShortcut(QtGui.QApplication.translate("studentWindow", "Ctrl+?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("studentWindow", "About Registron", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setShortcut(QtGui.QApplication.translate("studentWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCredits.setText(QtGui.QApplication.translate("studentWindow", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCredits.setShortcut(QtGui.QApplication.translate("studentWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSignIn.setText(QtGui.QApplication.translate("studentWindow", "Manage Accounts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLicense.setText(QtGui.QApplication.translate("studentWindow", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLog_out.setText(QtGui.QApplication.translate("studentWindow", "Log out", None, QtGui.QApplication.UnicodeUTF8))

import app_rc
