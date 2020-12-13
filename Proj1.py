# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prop_Trans.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Prop_Trans2 import Ui_PropWindow
from Proj_Cert import Ui_ProjCert
import json
import sys

class Ui_ProjWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(15, 45, 80);\n"
"QPushButton { color: red }\n"
"QLineEdit { color: red }\n"
"QComboBox { color: red }\n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        MainWindow.setAnimated(True)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 530, 761, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 10, 678, 160))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("background-color: rgb(17, 50, 100);\n"
"color: rgb(205, 250, 255); ")
        self.groupBox.setObjectName("groupBox")
        self.T_Cr_But1 = QtWidgets.QPushButton(self.groupBox)
        self.T_Cr_But1.setGeometry(QtCore.QRect(57, 57, 150, 57))
        self.T_Sub_But1 = QtWidgets.QPushButton(self.centralwidget)
        self.T_Sub_But1.setGeometry(QtCore.QRect(305, 513, 150, 57))
        font = QtGui.QFont()
        #font.setFamily("Baskerville")
        font.setFamily("orbitron")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(25)
        font.setLetterSpacing(font.AbsoluteSpacing, 5)
        font.setCapitalization(font.SmallCaps)
        self.T_Cr_But1.setFont(font)
        self.T_Cr_But1.setStyleSheet("QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch; color: rgb(205, 250, 255)}" "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch; color: rgb(200, 0, 5)}" "QPushButton:disabled { border-image: url(But3.png) 0 0 0 0 stretch stretch; color: rgb(50, 145, 205)}" "background-repeat: no-repeat;"  "background-position: center center;" "background-repeat: no-repeat;"  "background-position: center center;" )
        self.T_Cr_But1.setText("|CREATE|")
        self.T_Cr_But1.setIconSize(QtCore.QSize(150, 57))
        self.T_Cr_But1.setCheckable(False)
        self.T_Cr_But1.setAutoRepeat(False)
        self.T_Cr_But1.setAutoExclusive(False)
        self.T_Cr_But1.setAutoDefault(False)
        self.T_Cr_But1.setDefault(False)
        self.T_Cr_But1.setFlat(False)
        self.T_Cr_But1.setObjectName("T_Cr_But1")
        self.T_Cr_But1.clicked.connect(self.on_T_Cr_But1_clicked)
#        self.setCentralWidget(self.T_Cr_But1)

            
        self.T_En_But1 = QtWidgets.QPushButton(self.groupBox)
        self.T_En_But1.setGeometry(QtCore.QRect(264, 57, 150, 57))
        self.T_En_But1.setFont(font)
        self.T_En_But1.setStyleSheet("QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch; color: rgb(205, 250, 255)}" "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch; color: rgb(200, 0, 5)}" "QPushButton:disabled { border-image: url(But3.png) 0 0 0 0 stretch stretch; color: rgb(50, 145, 205)}" "background-repeat: no-repeat;"  "background-position: center center;" "background-repeat: no-repeat;"  "background-position: center center;" )
        self.T_En_But1.setText("|ENTER|")
        self.T_En_But1.setIconSize(QtCore.QSize(150, 57))
        self.T_En_But1.setCheckable(False)
        self.T_En_But1.setAutoRepeat(False)
        self.T_En_But1.setAutoExclusive(False)
        self.T_En_But1.setAutoDefault(False)
        self.T_En_But1.setDefault(False)
        self.T_En_But1.setFlat(False)
        self.T_En_But1.setObjectName("T_Ed_But1")
        self.T_En_But1.clicked.connect(self.on_T_En_But1_clicked)

        self.T_Ed_But1 = QtWidgets.QPushButton(self.groupBox)
        self.T_Ed_But1.setGeometry(QtCore.QRect(471, 57, 150, 57))
        self.T_Ed_But1.setFont(font)
        self.T_Ed_But1.setStyleSheet("QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch; color: rgb(205, 250, 255)}" "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch; color: rgb(200, 0, 5)}" "QPushButton:disabled { border-image: url(But3.png) 0 0 0 0 stretch stretch; color: rgb(50, 145, 205)}" "background-repeat: no-repeat;"  "background-position: center center;" "background-repeat: no-repeat;"  "background-position: center center;" )
        self.T_Ed_But1.setText("|EDIT|")
        self.T_Ed_But1.setIconSize(QtCore.QSize(150, 57))
        self.T_Ed_But1.setCheckable(False)
        self.T_Ed_But1.setAutoRepeat(False)
        self.T_Ed_But1.setAutoExclusive(False)
        self.T_Ed_But1.setAutoDefault(False)
        self.T_Ed_But1.setDefault(False)
        self.T_Ed_But1.setFlat(False)
        self.T_Ed_But1.setObjectName("T_Ed_But1")
 #       self.T_Ed_But1.clicked.connect(self.on_T_Ed_But1_clicked)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 400, 150, 155))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("circle2.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")


        self.groupBox.raise_()
        self.horizontalScrollBar.raise_()
        self.label_7.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_unsubmitted_Transaction = QtWidgets.QAction(MainWindow)
        self.actionOpen_unsubmitted_Transaction.setObjectName("actionOpen_unsubmitted_Transaction")
        self.actionNew_Transaction = QtWidgets.QAction(MainWindow)
        self.actionNew_Transaction.setObjectName("actionNew_Transaction")
        self.menuFile.addAction(self.actionOpen_unsubmitted_Transaction)
        self.menuFile.addAction(self.actionNew_Transaction)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Transaction Entry"))
        font = QtGui.QFont()
        #font.setFamily("Baskerville")
        font.setFamily("orbitron")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(25)
        font.setLetterSpacing(font.AbsoluteSpacing, 5)
        font.setCapitalization(font.SmallCaps)
        self.groupBox.setFont(font)
        self.groupBox.setTitle(_translate("MainWindow", "Project"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_unsubmitted_Transaction.setText(_translate("MainWindow", "Open unsubmitted Transaction"))
        self.actionNew_Transaction.setText(_translate("MainWindow", "New Transaction"))

    def on_T_En_But1_clicked(self):
        import sys
 #       app = QtWidgets.QApplication(sys.argv)
 #       window = Window()
 #       window.show()
        self.window = Window()
        self.window.show()
#        self.MainWindow.hide()
#        self.hide()
 #       sys.exit(app.exec_())

#        self.dialog.show()
#        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
#            'Enter your name:')
        
#        if ok:
#            self.le.setText(str(text))

    def on_T_Cr_But1_clicked(self):
        import sys
 #       app = QtWidgets.QApplication(sys.argv)
 #       window = Window()
 #       window.show()
        self.window = Window2()
        self.window.show()

#class Second(Ui_MainWindow(object)):
#    def __init__(self, parent=None):
#        super(Second, self).__init__(parent)

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_PropWindow()
        self.ui.setupUi(self)    

class Window2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window2, self).__init__(parent)
        self.ui = Ui_ProjCert()
        self.ui.setupUi(self)    
    
if __name__ == "__main__":
#    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ProjWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
 #   sys.exit(app.exec_())



