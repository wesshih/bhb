from Tkinter import Tk
from tkFileDialog import askopenfilename

def openFile():
	Tk().withdraw()
	filename = askopenfilename()
	print filename
	return filename

def test():
	print 'yo'