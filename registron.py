#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Joseph Rex
# @website: http://josephrex.me
# @repository: http://github.com/bl4ckdu5t/registron
# @twitter: @joerex101
# @contributors: ['James Olanipekun', 'Joseph Rex']
# # #
import sys, webbrowser, json, string
from PyQt4 import QtGui, QtCore
from ui_registron import Ui_MainWindow
from aboutDialog import Ui_AboutDialog
from creditDialog import Ui_creditDialog
from authDialog import Ui_authDialog
from licenseDialog import Ui_licenseDialog
from studentWindow import Ui_studentWindow
try:
	import pyttsx
except ImportError:
	raise ImportError, "pyttsx module is required for speech features of registron"

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
		databag = function.dict_object('list.json')
		campusID = str(self.ui.matricInput.toPlainText())
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
		databag = function.dict_object('list.json')
		studentName = databag['students'][id][0]
		studentDept = databag['students'][id][1]
		studentAvi = databag['students'][id][2]
		self.setWindowTitle('Registron - %s' %studentName)
		self.ui.studentName.setText(studentName)
		self.ui.studentID.setText(id)
		self.ui.studentDept.setText(studentDept)
		self.ui.schoolName.setText(databag['school'])
		avatar = self.ui.studentAvatar
		avatar.setText('<html><head/><body><p><img src=":/images/resources/images/128x128/%s"/></p></body></html>' % studentAvi)
		__courses__ = len(databag[studentDept])
		for x, course in enumerate(databag[studentDept]):
			getattr(self.ui, 'course{}'.format(x + 1)).setText(' %s' %course)
			getattr(self.ui, 'course{}'.format(x + 1)).show()
			getattr(self.ui, 'courseCheck{}'.format(x + 1)).show()
		self.show()
	def courseUpdates(self):
		self.ui.courseStatus.setText('Courses updated')
	def logout(self):
		for x in xrange(1,16,1):
			# close course by default
			getattr(self.ui, 'course{}'.format(x)).hide()
			# close course checkbox by default
			getattr(self.ui, 'courseCheck{}'.format(x)).hide()
		self.hide()
		window.show()

class programFunctions:
	"""Core functions for registron"""
	def talk(self, speech):
		"""Uses pyttsx module for speech"""
		engine = pyttsx.init()
		engine.say(speech)
		engine.runAndWait()
	def computeHash(self, original):
		"""Hashes passwords in MD5 (Message Digest Algorithm 5)"""
		return QtCore.QCryptographicHash.hash(original, QtCore.QCryptographicHash.Md5).toHex()
	def dict_object(self, filename):
		"""Opens json file and converts to python dictionary object"""
		name = open(filename,'r')
		json_string = name.read()
		json_loaded = json.loads(json_string)
		return json_loaded
	def openGitPage(self):
		webbrowser.open('https://github.com/bl4ckdu5t/registron')

# Core program functions called from this object
function = programFunctions()

app = QtGui.QApplication(sys.argv)
about = AboutBox()
credits = CreditBox()
authentication = Authentication()
license = LicenseDisp()
manageCourse = courseManage()
window = Main()

if __name__ == '__main__':
	window.show()
	QtCore.QTimer.singleShot(0, window.greetWelcome)
	sys.exit(app.exec_())

