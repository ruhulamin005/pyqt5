from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
import sys
import sqlite3


class UI(QMainWindow):
	def __init__(self):
		super(UI,self).__init__()

		#Here We will load UIc file
		uic.loadUi("paperprint.ui",self)


		#Loading Widgets
		self.text = self.findChild(QTextEdit, "textEdit")

		
		self.printPreview = self.findChild(QPushButton,"pushButton")
		self.printthis = self.findChild(QPushButton,"pushButton_2")



		#connecting button
		self.printthis.clicked.connect(self.print_file)
		self.printPreview.clicked.connect(self.print_preview_dialog)

	
		self.show()

	def print_file(self):
		printer = QPrinter(QPrinter.HighResolution)
		dialog = QPrintDialog(printer, self)

		if dialog.exec_() == QPrintDialog.Accepted:
			self.textEdit.print_(printer)

	def print_preview_dialog(self):
		printer = QPrinter(QPrinter.HighResolution)
		previewDialog = QPrintPreviewDialog(printer,self)
		previewDialog.paintRequested.connect(self.preview)
		previewDialog.exec_()

	def preview(self, printer):
		self.textEdit.print_(printer)










#Initializing the app

app = QApplication(sys.argv)
UiWindow = UI()
app.exec()
