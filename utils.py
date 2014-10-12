import webbrowser, json, os, sys
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
def dump_data(data):
	"""Dumps dictionary data back to JSON file format"""
	f = open('data.json', 'w')
	f.write(json.dumps(data))
def openGitPage():
	"""Opens project github repository in browser"""
	webbrowser.open('https://github.com/bl4ckdu5t/registron')
def resource_path(relative_path):
	""" PyInstaller resource path"""
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)