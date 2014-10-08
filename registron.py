#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Joseph Rex
# @website: http://josephrex.me
# @repository: http://github.com/bl4ckdu5t/registron
# @twitter: joerex101
# # #
import sys, json, string
import utils as function
from PyQt4 import QtGui, QtCore
from ui_registron import Ui_MainWindow
from aboutDialog import Ui_AboutDialog
from creditDialog import Ui_creditDialog
from authDialog import Ui_authDialog
from licenseDialog import Ui_licenseDialog
from studentWindow import Ui_studentWindow
from adminArea import Ui_adminWindow

class Main(QtGui.QMainWindow):
	"""Main class for registron"""
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.proceedBtn.clicked.connect(self.checkCampusID)
		self.ui.invalidID.hide()
		self.setGeometry(300, 100, 750, 500)

		#Menu Actions
		self.ui.actionQuit.triggered.connect(self.close)
		self.ui.actionDocumentation.triggered.connect(function.openGitPage)
		self.ui.actionAbout.triggered.connect(about.show)
		self.ui.actionCredits.triggered.connect(credits.show)
		self.ui.actionSignIn.triggered.connect(authentication.show)
		self.ui.actionLicense.triggered.connect(license.show)
	def greetWelcome(self):
		function.talk("Welcome to Registron")
	def checkCampusID(self):
		databag = function.dict_object('data.json')
		campusID = str(self.ui.matricInput.text())
		if campusID != '':
			if databag['students'].has_key(campusID):
				self.ui.invalidID.hide()
				studentName = databag['students'][campusID][0]
				function.talk("Hello %s, let us register your courses" % studentName)
				self.hide()
				manageCourse.grab(campusID)
			else:
				self.ui.invalidID.show()
				function.talk("There is no student with that campus ID in our records")
		else:
			self.ui.invalidID.show()
			function.talk("Your input is empty. Please type your campus ID to log in as a student")

class AboutBox(QtGui.QDialog):
	"""Displays about dialog"""
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.ui = Ui_AboutDialog()
		self.ui.setupUi(self)

class CreditBox(QtGui.QDialog):
	"""Displays Credit dialog"""
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.ui = Ui_creditDialog()
		self.ui.setupUi(self)

class Authentication(QtGui.QDialog):
	"""Displays authentication dialog"""
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.ui = Ui_authDialog()
		self.ui.setupUi(self)
		self.ui.authError.hide()
		self.ui.logBtn.clicked.connect(self.verify)
	def verify(self):
		__user__ = str(self.ui.adminUname.text())
		__pass__ = str(self.ui.adminPass.text())
		databag = function.dict_object('data.json')
		__spass__ = databag['auth']
		if __user__ == 'admin' and function.computeHash(__pass__) == __spass__:
			self.ui.authError.hide()
			self.close()
			window.hide()
			manageCourse.hide()
			administration.show()
		else:
			function.talk("Invalid authentication")
			self.ui.authError.show()

class LicenseDisp(QtGui.QDialog):
	"""Displays license dialog"""
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.ui = Ui_licenseDialog()
		self.ui.setupUi(self)

class courseManage(QtGui.QMainWindow):
	"""Displays course management window"""
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_studentWindow()
		self.ui.setupUi(self)
		self.setGeometry(300, 100, 750, 600)

		#Menu Actions
		self.ui.actionQuit.triggered.connect(self.close)
		self.ui.actionDocumentation.triggered.connect(function.openGitPage)
		self.ui.actionAbout.triggered.connect(about.show)
		self.ui.actionCredits.triggered.connect(credits.show)
		self.ui.actionSignIn.triggered.connect(authentication.show)
		self.ui.actionLicense.triggered.connect(license.show)
		self.ui.actionLog_out.triggered.connect(self.logout)
		self.ui.verifyBtn.clicked.connect(self.courseUpdates)
		for x in xrange(1,16,1):
			# close course by default
			getattr(self.ui, 'course{}'.format(x)).hide()
			# close course checkbox by default
			getattr(self.ui, 'courseCheck{}'.format(x)).hide()
	def grab(self, id):
		databag = function.dict_object('data.json')
		studentName = databag['students'][id][0]
		studentDept = databag['students'][id][1]
		studentAvi = databag['students'][id][2]
		studentCourses = databag['students'][id][3]
		self.setWindowTitle('Registron - %s' %studentName)
		self.ui.studentName.setText(studentName)
		self.ui.studentID.setText(id)
		self.ui.studentDept.setText(studentDept)
		if len(databag['school']) > 34:
			truncated = databag['school'][:32] + '...'
			self.ui.schoolName.setText(truncated)
			self.ui.schoolName.setToolTip(databag['school'])
		else:
			self.ui.schoolName.setText(databag['school'])
		avatar = self.ui.studentAvatar
		if studentAvi == '':
			avatar.setPixmap(QtGui.QPixmap('resources/images/128x128/default.jpg'))
		else:
			avatar.setPixmap(QtGui.QPixmap('resources/images/128x128/%s' % studentAvi))
		__courses__ = len(databag['departments'][studentDept])
		# Show the student's department courses
		for x, course in enumerate(databag['departments'][studentDept]):
			getattr(self.ui, 'course{}'.format(x + 1)).setText(' %s' %course)
			getattr(self.ui, 'course{}'.format(x + 1)).show()
			getattr(self.ui, 'courseCheck{}'.format(x + 1)).show()
		# check the courses offered by the student
		if studentCourses.split(':') != ['']: # check in cases of students with no registered courses
			for x, registered in enumerate(studentCourses.split(':')):
				getattr(self.ui, 'courseCheck{}'.format(registered)).setCheckState(2)
		self.show()
	def courseUpdates(self):
		offered = ''
		for x in xrange(1,16,1):
			if getattr(self.ui, 'courseCheck{}'.format(x)).checkState() == 2:
				offered += str(x) + ':'
		offered = offered.rstrip(':')
		studentIndex = str(self.ui.studentID.text())
		databag = function.dict_object('data.json')
		databag['students'][studentIndex][3] = offered
		function.dump_data(databag)
		function.talk('Your courses have been updated')
		self.ui.courseStatus.setText('Courses updated')
	def logout(self):
		# say goodbye
		function.talk("Logging out")
		for x in xrange(1,16,1):
			# uncheck all checked boxes from session
			getattr(self.ui, 'courseCheck{}'.format(x)).setCheckState(0)
			# close course by default
			getattr(self.ui, 'course{}'.format(x)).hide()
			# close course checkbox by default
			getattr(self.ui, 'courseCheck{}'.format(x)).hide()
		self.ui.courseStatus.setText('Check the courses you want to offer this semester')
		self.hide()
		window.show()

class administrationView(QtGui.QMainWindow):
	"""Displays administrator window"""
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_adminWindow()
		self.ui.setupUi(self)
		self.setGeometry(300, 100, 750, 520)
		self.ui.schoolSaved.hide()
		self.ui.studentSaved.hide()
		self.ui.courseAdded.hide()
		self.ui.passwordChanged.hide()
		self.databag = function.dict_object('data.json')
		school = self.databag['school']
		self.ui.schoolName.setText(school)
		self.ui.schoolNameBtn.clicked.connect(self.addSchool)
		self.ui.changePassBtn.clicked.connect(self.changePass)
		self.ui.addDeptBtn.clicked.connect(self.addDepartment)
		self.ui.addStudentBtn.clicked.connect(self.addStudent)

		# Student ID Listings
		for x, id in enumerate(self.databag['students']):
			pass #print x, id
		self.studentIndex1 = QtGui.QLabel(self.ui.scrollAreaWidgetContents)
		self.studentIndex1.setGeometry(QtCore.QRect(0, 0, 195, 30))
		self.studentIndex1.setFrameShape(QtGui.QFrame.Panel)
		self.studentIndex1.setStyleSheet('color: rgb(0,0,0);background: rgb(255, 255, 255)')
		self.studentIndex1.setText("I am numbra one")
		self.studentIndex1.setObjectName(QtCore.QString.fromUtf8("studentIndex1"))
		# Departments Combo Box
		for x, department in enumerate(self.databag['departments']):
			self.ui.courseAddDeptList.addItem('')
			self.ui.studentDept.addItem('')
			self.ui.courseAddDeptList.setItemText(x, department)
			self.ui.studentDept.setItemText(x, department)
		self.ui.addCourseBtn.clicked.connect(self.addCourses)
		#Menu Actions
		self.ui.actionQuit.triggered.connect(self.close)
		self.ui.actionDocumentation.triggered.connect(function.openGitPage)
		self.ui.actionAbout.triggered.connect(about.show)
		self.ui.actionCredits.triggered.connect(credits.show)
		self.ui.actionLicense.triggered.connect(license.show)
		self.ui.actionAdmin_Logout.triggered.connect(self.closeAdmin)

	def addSchool(self):
		self.databag['school'] = str( self.ui.schoolName.text() )
		function.dump_data(self.databag)
		self.ui.schoolSaved.show()
		QtCore.QTimer.singleShot(1000 * 5, self.ui.schoolSaved.hide)
		function.talk('School name saved')
	def addDepartment(self):
		deptInput = str( self.ui.addDept.text() )
		if deptInput == '':
			self.ui.addDeptNotice.setText("Empty Input")
			function.talk('Empty Input')
		else:
			self.databag['departments'][deptInput] = []
			function.dump_data(self.databag)
			self.ui.addDeptNotice.setText('Department Saved')
			self.ui.addDept.clear()
			# self.ui.courseAddDeptList.repaint()
			function.talk("Department saved")
	def addCourses(self):
		courseName = str( self.ui.addCourse.text() )
		if courseName == '':
			function.talk('Empty Input')
		else:
			selectedDepartment = str( self.ui.courseAddDeptList.currentText() )
			self.databag['departments'][selectedDepartment].append(courseName)
			function.dump_data(self.databag)
			self.ui.addCourse.clear()
			self.ui.courseAdded.show()
			function.talk("Course added")
			QtCore.QTimer.singleShot(1000 * 3, self.ui.courseAdded.hide)
	def addStudent(self):
		surname = str( self.ui.surname.text() )
		others = str( self.ui.othernames.text() )
		department = str( self.ui.studentDept.currentText() )
		campusID = str( self.ui.campusID.text() )
		avatar = str( self.ui.studentImage.text() )
		# Form Validation
		if surname == '':
			self.ui.studentSaved.setText("Surname field is required")
			self.ui.studentSaved.show()
		elif others == '':
			self.ui.studentSaved.setText("Other names field is required")
			self.ui.studentSaved.show()
		elif campusID == '':
			self.ui.studentSaved.setText("Campus ID is required")
			self.ui.studentSaved.show()
		elif campusID in self.databag['students']:
			self.ui.studentSaved.setText("A student exists with that ID")
			self.ui.studentSaved.show()
		else:
			self.databag['students'][campusID] = [ surname + ' ' + others, department,avatar,'']
			function.talk('Student has been added')
			self.ui.studentSaved.setText("Student Saved")
			self.ui.studentSaved.show()
			function.dump_data(self.databag)
			self.ui.surname.clear()
			self.ui.othernames.clear()
			self.ui.campusID.clear()
			self.ui.studentImage.clear()
			QtCore.QTimer.singleShot(1000 * 3, self.ui.studentSaved.hide)
	def changePass(self):
		"""Changes administrator's password"""
		newpass = str( self.ui.passwordChange.text() )
		if newpass == '':
			self.ui.passwordChanged.setText('Password Field cannot be left blank')
			self.ui.passwordChanged.show()
			function.talk('password empty!')
		else:
			self.databag['auth'] = str(function.computeHash(newpass))
			function.dump_data(self.databag)
			self.ui.passwordChanged.setText('Password Updated')
			self.ui.passwordChanged.show()
			self.ui.passwordChange.clear()
			function.talk('password updated')
	def closeAdmin(self):
		self.hide()
		window.show()

app = QtGui.QApplication(sys.argv)
about = AboutBox()
credits = CreditBox()
authentication = Authentication()
license = LicenseDisp()
manageCourse = courseManage()
administration = administrationView()
window = Main()

if __name__ == '__main__':
	window.show()
	QtCore.QTimer.singleShot(500, window.greetWelcome) # Greet after 500 milliseconds
	sys.exit(app.exec_())

