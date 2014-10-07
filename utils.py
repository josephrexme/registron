import webbrowser, json
from PyQt4 import QtCore
try:
	import pyttsx
except ImportError:
	raise ImportError, "pyttsx module is required for speech features of registron"

"""Core functions for registron"""
def talk(speech):
	"""Uses pyttsx module for speech"""
	engine = pyttsx.init()
	engine.say(speech)
	engine.runAndWait()
def computeHash(original):
	"""Hashes passwords in MD5 (Message Digest Algorithm 5)"""
	return QtCore.QCryptographicHash.hash(original, QtCore.QCryptographicHash.Md5).toHex()
def dict_object(filename):
	"""Opens json file and converts to python dictionary object"""
	name = open(filename,'r')
	json_string = name.read()
	json_loaded = json.loads(json_string)
	return json_loaded
def openGitPage():
	"""Opens project github repository in browser"""
	webbrowser.open('https://github.com/bl4ckdu5t/registron')