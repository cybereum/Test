from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter, QBrush, QPen
from Main1 import Ui_MainWindow
from Prop_Trans2 import Ui_PropWindow
from Proj1 import Ui_ProjWindow
from Part_Cert import Ui_PartCert
from pathlib import Path


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setStyleSheet("background-color: rgb(15, 45, 80);")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(100, 10, 111, 109))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("circle2.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")

        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(18, 120, 300, 16))
        self.label_14.setObjectName("label_16")
        self.label_14.setStyleSheet("color: rgb(185, 250, 255); ")

        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(50, 140, 220, 16))
        self.label_15.setObjectName("label_16")
        self.label_15.setStyleSheet("color: rgb(175, 250, 255); ")

        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(10, 205, 141, 16))
        self.label_16.setObjectName("label_16")
        self.label_16.setStyleSheet("color: rgb(205, 250, 255); ")
        self.textName = QtWidgets.QLineEdit(self)
        self.textName.setGeometry(QtCore.QRect(160, 200, 150, 22))
        self.textName.setStyleSheet("background-color: rgb(12, 30, 50);\n" 
"color: rgb(205, 250, 255); ")

        self.label_17 = QtWidgets.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(10, 245, 141, 16))
        self.label_17.setObjectName("label_16")
        self.label_17.setStyleSheet("color: rgb(205, 250, 255); ")       
        self.textPass = QtWidgets.QLineEdit(self)
        self.textPass.setGeometry(QtCore.QRect(160, 240, 150, 22))
        self.textPass.setStyleSheet("background-color: rgb(12, 30, 50);\n" 
"color: rgb(205, 250, 255); ")
        self.textPass.setEchoMode(QtGui.QLineEdit.Password)

        # self.Request = QtWidgets.QLabel(self)
        # self.Request.setGeometry(QtCore.QRect(85, 340, 150, 20))
        # self.Request.setObjectName("request")
        # self.Request.setStyleSheet("color: rgb(255, 0, 0); text-decoration: underline;")  
        # #self.Request.setAlignment(QtWidgets.AlignCenter)
        # self.Request.setAlignment(Qt.AlignCenter)
        # #self.Request.mousePressEvent = self.link_handler()

        self.paintEvent(self)

        font = QtGui.QFont()
        #font.setFamily("Baskerville")
        font.setFamily("orbitron")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(25)
        font.setLetterSpacing(font.AbsoluteSpacing, 5)
        font.setCapitalization(font.SmallCaps)

        self.Request = QtWidgets.QPushButton(self)
        self.Request.setGeometry(QtCore.QRect(85, 355, 150, 20))
        self.Request.setFont(font)
        self.Request.setStyleSheet("QPushButton { color: red }; text-decoration: underline; QPushButton:disabled {color: rgb(50, 145, 205)};")
        self.Request.setText("|  r e q u e s t  |")
        self.Request.setObjectName("request")
        self.Request.setDisabled(False)
    #    self.Request.clicked.connect(self.handleRequest)


        self.buttonLogin = QtWidgets.QPushButton('| LOGIN |', self)
        self.buttonLogin.setGeometry(QtCore.QRect(85, 285, 150, 57))
    
        self.buttonLogin.setFont(font)
        self.buttonLogin.setAutoFillBackground(False)
        #self.buttonLogin.setStyleSheet("border-image: url(But1.png) 0 0 0 0 stretch stretch;" "background-repeat: no-repeat;"  "background-position: center center;" "color: rgb(205, 250, 255)")
        self.buttonLogin.setStyleSheet("QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch; color: rgb(205, 250, 255)}" "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch; color: rgb(200, 0, 5)}" "QPushButton:disabled { border-image: url(But3.png) 0 0 0 0 stretch stretch; color: rgb(50, 145, 205)}" "background-repeat: no-repeat;"  "background-position: center center;" "background-repeat: no-repeat;"  "background-position: center center;")
        #self.buttonLogin.setStyleSheet("color: rgb(205, 250, 255)")
        #self.buttonLogin.setStyleSheet("border-image: url(But1.png) 0 0 0 0 stretch stretch;" :Pressed "border-image: url(But1.png) 0 0 0 0 stretch stretch;""} "background-repeat: no-repeat;"  "background-position: center center;" "color: rgb(205, 250, 255)")

        self.buttonLogin.clicked.connect(self.handleLogin)

        self.retranslateUi(self)

#        layout = QtWidgets.QVBoxLayout(self)
#        layout.addWidget(self.textName)
#        layout.addWidget(self.textPass)
#        layout.addWidget(self.buttonLogin)


#    def handleRequest(self):
#        window2 = Window2()
#        window2.show()
#        sys.exit(app.exec_())



    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        #painter.setPen(QtCore.Qt.red)
        painter.setPen(QtGui.QColor(90, 202, 252))
        #brush = QtGui.QBrush(QtGui.QColor(205, 250, 255))
        painter.setBrush(QtCore.Qt.white)
        painter.drawLine(10, 170, 315, 170)
        painter.drawLine(10, 350, 315, 350)

    def handleLogin(self):
        if (self.textName.text() == 'ananth' and
            self.textPass.text() == 'probloch'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        font2 = QtGui.QFont()
        font2.setFamily("Baskerville")
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(35)
        font2.setLetterSpacing(font2.AbsoluteSpacing, 5)
        font2.setCapitalization(font2.SmallCaps)
        self.label_15.setFont(font2)
        self.label_15.setText(_translate("MainWindow", "P r o  B l o  C h"))

        font = QtGui.QFont()
        #font.setFamily("Baskerville")
        font.setFamily("orbitron")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(25)
        font.setLetterSpacing(font.AbsoluteSpacing, 1)
        self.Request.setFont(font)
        self.label_14.setFont(font)
        self.label_16.setFont(font)
        self.label_17.setFont(font)
        #self.Request.setText(_translate("MainWindow", "|  r e q u e s t  |"))
        self.label_14.setText(_translate("MainWindow", "{ ' P l a t f o r m  '   :   c y b e r e u m . i o }"))
        font.setCapitalization(font.SmallCaps)
        self.label_16.setText(_translate("MainWindow", "| U s e r N a m e |"))
        self.label_17.setText(_translate("MainWindow", "| P a s s W o r d |"))



        
        #sys.exit(app.exec_())

class Window2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window2, self).__init__(parent)
        self.ui2 = Ui_PartCert()
        self.ui2.setupUi(self)  

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_ProjWindow()
        self.ui.setupUi(self)
        

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    my_file = Path("user_public.pem")
    if my_file.is_file():
        print('exists')
        login = Login()
        if login.exec_() == QtWidgets.QDialog.Accepted:
            window = Window()
            window.show()
            sys.exit(app.exec_())
    else:
        print('does not exist')
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_PartCert()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())