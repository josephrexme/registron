#!/usr/bin/env python
# 
# @author: Joseph Rex
# @website: http://josephrex.me
# @repository: http://github.com/bl4ckdu5t/registron
# @twitter: @joerex101
# @contributors: ['James Olanipekun', 'Joseph Rex']
# # #
import sys, webbrowser
from PyQt4 import QtGui, QtCore
from ui_registron import Ui_MainWindow
from aboutDialog import Ui_AboutDialog
from creditDialog import Ui_creditDialog
from authDialog import Ui_authDialog
from licenseDialog import Ui_licenseDialog
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

		#Menu Actions
		self.ui.actionQuit.triggered.connect(self.close)
		self.ui.actionDocumentation.triggered.connect(self.openGitPage)
		self.ui.actionAbout.triggered.connect(about.show)
		self.ui.actionCredits.triggered.connect(credits.show)
		self.ui.actionSignIn.triggered.connect(authentication.show)
		self.ui.actionLicense.triggered.connect(license.show)
	def greetWelcome(self):
		function.talk("Welcome to Registron")
	def checkCampusID(self):
		campusID = self.ui.matricInput.toPlainText()
		if campusID != '':
			self.hide()
			self.show()
		else:
			function.talk("Your input is empty. Please type your campus ID to log in as a student")
	def openGitPage(self):
		webbrowser.open('https://github.com/bl4ckdu5t/registron')

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

class programFunctions:
	"""Core functions for registron"""
	def talk(self, speech):
		"""Uses pyttsx module for speech"""
		engine = pyttsx.init()
		engine.say(speech)
		engine.runAndWait()

function = programFunctions()

app = QtGui.QApplication(sys.argv)
about = AboutBox()
credits = CreditBox()
authentication = Authentication()
license = LicenseDisp()

if __name__ == '__main__':
	window = Main()
	window.show()
	QtCore.QTimer.singleShot(0, window.greetWelcome)
	sys.exit(app.exec_())

