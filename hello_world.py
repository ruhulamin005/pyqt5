# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helloqt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.click_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it())
        self.click_button.setGeometry(QtCore.QRect(50, 290, 741, 281))
        self.click_button.setObjectName("click_button")
        self.hello_label = QtWidgets.QLabel(self.centralwidget)
        self.hello_label.setGeometry(QtCore.QRect(240, 80, 421, 121))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.hello_label.setFont(font)
        self.hello_label.setObjectName("hello_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 21))
        self.menubar.setObjectName("menubar")
        self.menuHello = QtWidgets.QMenu(self.menubar)
        self.menuHello.setObjectName("menuHello")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHello.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.click_button.setText(_translate("MainWindow", "Click me"))
        self.hello_label.setText(_translate("MainWindow", "Hello QT"))
        self.menuHello.setTitle(_translate("MainWindow", "Hello"))

        #In pressing button
    def press_it(self):
        self.hello_label.setText("It changed!!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
