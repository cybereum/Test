from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui, QtCore, QtWidgets
from Main1 import Ui_MainWindow
from Prop_Trans2 import Ui_PropWindow
from Proj1 import Ui_ProjWindow
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from PySide2 import QtXml

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setStyleSheet("background-color: rgb(15, 45, 80);")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(101, 10, 111, 109))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../../Blockchain_Schedule/Logos/circle2.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")

        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(66, 120, 220, 16))
        self.label_14.setObjectName("label_16")
        self.label_14.setStyleSheet("color: rgb(205, 250, 255); ")

        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(104, 140, 220, 16))
        self.label_15.setObjectName("label_16")
        self.label_15.setStyleSheet("color: rgb(205, 250, 255); ")

        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(10, 170, 141, 16))
        self.label_16.setObjectName("label_16")
        self.label_16.setStyleSheet("color: rgb(205, 250, 255); ")
        self.textName = QtWidgets.QLineEdit(self)
        self.textName.setGeometry(QtCore.QRect(160, 170, 150, 22))
        self.textName.setStyleSheet("background-color: rgb(12, 30, 50);\n"
"color: rgb(205, 250, 255); ")

        self.label_17 = QtWidgets.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(10, 210, 141, 16))
        self.label_17.setObjectName("label_16")
        self.label_17.setStyleSheet("color: rgb(205, 250, 255); ")
        self.textPass = QtWidgets.QLineEdit(self)
        self.textPass.setGeometry(QtCore.QRect(160, 210, 150, 22))
        self.textPass.setStyleSheet("background-color: rgb(12, 30, 50);\n"
"color: rgb(205, 250, 255); ")
        self.textPass.setEchoMode(QtGui.QLineEdit.Password)

        self.buttonLogin = QtWidgets.QPushButton('| L O G I N |', self)
        self.buttonLogin.setGeometry(QtCore.QRect(85, 250, 150, 57))
    
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.buttonLogin.setFont(font)
        self.buttonLogin.setAutoFillBackground(False)
        #self.buttonLogin.setStyleSheet("border-image: url(But1.png) 0 0 0 0 stretch stretch;" "background-repeat: no-repeat;"  "background-position: center center;" "color: rgb(205, 250, 255)")
        self.buttonLogin.setStyleSheet("QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch; color: rgb(205, 250, 255)}" "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch; color: rgb(50, 145, 205)}" "background-repeat: no-repeat;"  "background-position: center center;" "color: rgb(205, 250, 255)")
        #self.buttonLogin.setStyleSheet("color: rgb(205, 250, 255)")
        #self.buttonLogin.setStyleSheet("border-image: url(But1.png) 0 0 0 0 stretch stretch;" :Pressed "border-image: url(But1.png) 0 0 0 0 stretch stretch;""} "background-repeat: no-repeat;"  "background-position: center center;" "color: rgb(205, 250, 255)")

        self.buttonLogin.clicked.connect(self.handleLogin)

        self.retranslateUi(self)

#        layout = QtWidgets.QVBoxLayout(self)
#        layout.addWidget(self.textName)
#        layout.addWidget(self.textPass)
#        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if (self.textName.text() == 'ananth' and
            self.textPass.text() == 'probloch'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        font = QtGui.QFont()
        font.setFamily("Baskerville")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setText(_translate("MainWindow", "P r o  B l o  C h"))
        self.label_14.setText(_translate("MainWindow", "p l a t f o r m   |   c y b e r e u m . i o"))
        self.label_16.setText(_translate("MainWindow", "| u s e r n a m e |"))
        self.label_17.setText(_translate("MainWindow", "| p a s s w o r d |"))

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_ProjWindow()
        self.ui.setupUi(self)
        



import sys

if __name__ == '__main__':
    #appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    #window = QMainWindow()
    #window.resize(250, 150)
    #window.show()
    #exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    #sys.exit(exit_code)
    
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    login = Login()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        #window = QMainWindow()
        window = Window()
        #window.resize(250, 150)
        window.show()
        exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
        sys.exit(exit_code)
