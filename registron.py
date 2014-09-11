#!/usr/bin/env python
# 
# @author: Joseph Rex
# @website: http://josephrex.me
# @repository: http://github.com/bl4ckdu5t/registron
# @twitter: @joerex101
# @contributors: [James Olanipekun]
# # #
import sys, webbrowser
from PyQt4 import QtGui, QtCore
from ui_registron import Ui_MainWindow
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
		self.ui.connect(self.greetWelcome)
		self.ui.proceedBtn.clicked.connect(self.checkCampusID)

		#Menu Actions
		self.ui.actionQuit.triggered.connect(self.close)
		self.ui.actionDocumentation.triggered.connect(self.openGitPage)
		# self.ui.actionAbout.triggered.connect(self.aboutProgram)
		# self.ui.actionCredits.triggered.connect(self.showCredits)
		# self.ui.actionNewWindow.triggered.connect(self.cloneWindow)
		# self.ui.actionSignIn.triggered.connect(self.adminAuth)
	def greetWelcome(self):
		function.talk("Welcome to Registron")
	def checkCampusID(self):
		campusID = self.ui.matricInput.toPlainText()
	def openGitPage(self):
		webbrowser.open('http://github.com/bl4ckdu5t/registron')
	

class programFunctions:
	"""Core functions for registron"""
	def talk(self, speech):
		"""Uses pyttsx module for speech"""
		engine = pyttsx.init()
		engine.say(speech)
		engine.runAndWait()

function = programFunctions()
		

if __name__ == '__main__':	
	app = QtGui.QApplication(sys.argv)
	window = Main()

	window.show()
	sys.exit(app.exec_())

