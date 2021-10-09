# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 822)
        MainWindow.setStyleSheet("\n"
"QFrame{\n"
"\n"
"background:#333;\n"
"background:url(:/newPrefix/bg.jpg);\n"
"border-radius:20px;\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit{\n"
"\n"
"background:white;\n"
"border:none;\n"
"color:#717071;\n"
"font-size:24px;\n"
"border-radius:15px;\n"
"boder-button:1px soild #717072;\n"
"}\n"
"QLabel{\n"
"\n"
"font-family:century gothic;\n"
"font-size:24px;\n"
"    \n"
"}\n"
"\n"
"Qframe\n"
"{\n"
" background:pink\n"
"\n"
"}\n"
"\n"
"#Form{\n"
"\n"
"    background:url(:/newPrefix/bg1.jpg);\n"
"}\n"
"\n"
"QLabel{\n"
" \n"
"background:none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"color:black;\n"
"border-radius:15px;\n"
"background:pink;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"background-color:white;\n"
"font-size:24px;\n"
"border-radius:15px;\n"
"color:black;\n"
"\n"
"\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(190, 70, 561, 601))
        self.frame.setStyleSheet("\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 50, 171, 51))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(110, 220, 371, 51))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setText("")
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 290, 371, 51))
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 530, 541, 51))
        self.pushButton.setStyleSheet("")
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(440, 30, 81, 81))
        self.toolButton.setStyleSheet("border-radius:30px;\n"
"background-color:pink;\n"
"")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/businessman.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(64, 64))
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ADMIN LOGIN"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
