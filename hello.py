import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Hello there!!")
		self.setLayout(qtw.QVBoxLayout())

		

		my_label = qtw.QLabel("Hello World!!")
		self.layout().addWidget(my_label)
		self.show()



app = qtw.QApplication([])
mw = MainWindow()


#Run the App
app.exec_()