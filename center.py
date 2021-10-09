from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel,QPushButton,QTextEdit, QDesktopWidget
from PyQt5 import uic
import sys

class UI(QMainWindow):

	def initUI(self):
		self.setWindowTitle("Center the app")
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget.availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def __init__(self):
		super(UI, self).__init__()



		#loading UI file
		uic.loadUi("center.ui", self)
		

		#Define Widgets

		self.name = self.findChild(QLabel,"name")
		self.phone = self.findChild(QLabel,"phone")
		self.item = self.findChild(QLabel,"item")
		self.amount = self.findChild(QLabel,"amount")



		self.getName = self.findChild(QTextEdit, "getName")
		self.getPhone = self.findChild(QTextEdit, "getPhone")
		self.getItem = self.findChild(QTextEdit, "getItem")
		self.getAmount = self.findChild(QTextEdit, "getAmount")





		self.button = self.findChild(QPushButton,"pushButton")

		#Trying to check the activity

		self.button.clicked.connect(self.clicker)

		self.show()




	def clicker(self):
		self.name.setText(f'Name: {self.getName.toPlainText()}')
		self.phone.setText(f' Phone:{self.getPhone.toPlainText()}')
		self.item.setText(f'Item:{self.getItem.toPlainText()}')
		self.amount.setText(f' Amount:{self.getAmount.toPlainText()}')






app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()

