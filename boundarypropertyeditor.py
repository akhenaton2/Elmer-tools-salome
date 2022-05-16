from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
import sys


class UI(QDialog):
	def __init__(self):
		super(UI, self).__init__()		
		# Load the ui file
		uic.loadUi("boundarypropertyeditor.ui", self)

	# Show The App
		self.show()

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
