# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prop_Trans.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from Main1 import Ui_MainWindow
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import json
import sys
import pandas as pd
import numpy as np
#import altair as alt
##from matplotlibwidget import MatplotlibWidget
#import matplotlib
#matplotlib.use("Qt5Agg")
from PyQt5.QtCore import QUrl
##from PyQt5.QtWebEngineWidgets import QWebEngineView
##import PyQtWebEngine
##from PyQtWebEngine import QWebEngineView
import plotly.offline as po
import plotly.graph_objs as go
import plotly.figure_factory as ff
#******************************************************************

import random


from force1 import Ui_Force
from GANTT2 import Ui_GANTT

class Ui_PropWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
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
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 1100, 761, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(750, 10, 250, 181))
        self.calendarWidget.setStyleSheet("color: rgb(205, 250, 255); ")
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setAutoFillBackground(True)

        self.hbox1 = QHBoxLayout(self.centralwidget)
        #self.hbox1.addStretch(0.1)

        self.vbox1 = QVBoxLayout(self.centralwidget)
        self.vbox1.addStretch(1)
        self.vbox1.addLayout(self.hbox1)


        #self.groupBox = QtWidgets.QGroupBox()
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 678, 99))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("background-color: rgb(17, 55, 100);\n"
"color: rgb(205, 250, 255); ")
        self.groupBox.setObjectName("groupBox")

        #self.hbox1.addWidget(self.groupBox)

        self.T_Cr_But1 = QtWidgets.QPushButton(self.groupBox)
        self.T_Cr_But1.setGeometry(QtCore.QRect(57, 30, 150, 57))
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

        self.T_Ed_But1 = QtWidgets.QPushButton(self.groupBox)
        self.T_Ed_But1.setGeometry(QtCore.QRect(264, 30, 150, 57))
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

        self.T_Ap_But1 = QtWidgets.QPushButton(self.groupBox)
        self.T_Ap_But1.setGeometry(QtCore.QRect(471, 30, 150, 57))
        self.T_Ap_But1.setFont(font)
        self.T_Ap_But1.setStyleSheet("QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch; color: rgb(205, 250, 255)}" "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch; color: rgb(200, 0, 5)}" "QPushButton:disabled { border-image: url(But3.png) 0 0 0 0 stretch stretch; color: rgb(50, 145, 205)}" "background-repeat: no-repeat;"  "background-position: center center;" "background-repeat: no-repeat;"  "background-position: center center;" )
        self.T_Ap_But1.setDisabled(True)
        self.T_Ap_But1.setText("|REVIEW|")
        self.T_Ap_But1.setIconSize(QtCore.QSize(150, 57))
        self.T_Ap_But1.setCheckable(False)
        self.T_Ap_But1.setAutoRepeat(False)
        self.T_Ap_But1.setAutoExclusive(False)
        self.T_Ap_But1.setAutoDefault(False)
        self.T_Ap_But1.setDefault(False)
        self.T_Ap_But1.setFlat(False)
        self.T_Ap_But1.setObjectName("T_Ap_But1")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 118, 678, 99))
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet("background-color: rgb(17, 55, 100);\n"
"color: rgb(205, 250, 255); ")
        self.groupBox_2.setObjectName("groupBox_2")
        self.T_Cr_But2 = QtWidgets.QPushButton(self.groupBox_2)
        self.T_Cr_But2.setGeometry(QtCore.QRect(57, 30, 150, 57))

        self.T_Cr_But2.setFont(font)
        self.T_Cr_But2.setAutoFillBackground(False)
        self.T_Cr_But2.setStyleSheet("QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch; color: rgb(205, 250, 255)}" "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch; color: rgb(200, 0, 5)}" "QPushButton:disabled { border-image: url(But3.png) 0 0 0 0 stretch stretch; color: rgb(50, 145, 205)}" "background-repeat: no-repeat;"  "background-position: center center;" "background-repeat: no-repeat;"  "background-position: center center;" )
        self.T_Cr_But2.setText("|CREATE|")
        self.T_Cr_But2.setIconSize(QtCore.QSize(150, 57))
        self.T_Cr_But2.setCheckable(False)
        self.T_Cr_But2.setAutoRepeat(False)
        self.T_Cr_But2.setAutoExclusive(False)
        self.T_Cr_But2.setAutoDefault(False)
        self.T_Cr_But2.setDefault(False)
        self.T_Cr_But2.setFlat(False)
        self.T_Cr_But2.setObjectName("T_Cr_But2")
        self.T_Ed_But2 = QtWidgets.QPushButton(self.groupBox_2)
        self.T_Ed_But2.setGeometry(QtCore.QRect(264, 30, 150, 57))


        self.T_Ed_But2.setFont(font)
        self.T_Ed_But2.setAutoFillBackground(False)
        self.T_Ed_But2.setStyleSheet("QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch; color: rgb(205, 250, 255)}" "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch; color: rgb(200, 0, 5)}" "QPushButton:disabled { border-image: url(But3.png) 0 0 0 0 stretch stretch; color: rgb(50, 145, 205)}" "background-repeat: no-repeat;"  "background-position: center center;" "background-repeat: no-repeat;"  "background-position: center center;" )
        self.T_Ed_But2.setText("|EDIT|")
        self.T_Ed_But2.setIconSize(QtCore.QSize(150, 57))
        self.T_Ed_But2.setCheckable(False)
        self.T_Ed_But2.setAutoRepeat(False)
        self.T_Ed_But2.setAutoExclusive(False)
        self.T_Ed_But2.setAutoDefault(False)
        self.T_Ed_But2.setDefault(False)
        self.T_Ed_But2.setFlat(False)
        self.T_Ed_But2.setObjectName("T_Ed_But2")
        self.T_Ed_But2.clicked.connect(self.on_T_Ed_But2_clicked)
        

        self.T_Ap_But2 = QtWidgets.QPushButton(self.groupBox_2)
        self.T_Ap_But2.setGeometry(QtCore.QRect(471, 30, 150, 57))
        self.T_Ap_But2.setFont(font)

        self.T_Ap_But2.setStyleSheet("QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch; color: rgb(205, 250, 255)}" "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch; color: rgb(200, 0, 5)}" "QPushButton:disabled { border-image: url(But3.png) 0 0 0 0 stretch stretch; color: rgb(50, 145, 205)}" "background-repeat: no-repeat;"  "background-position: center center;" "background-repeat: no-repeat;"  "background-position: center center;" )
        self.T_Ap_But2.setDisabled(True)
        self.T_Ap_But2.setText("|REVIEW|")
        self.T_Ap_But2.setIconSize(QtCore.QSize(150, 57))
        self.T_Ap_But2.setCheckable(False)
        self.T_Ap_But2.setAutoRepeat(False)
        self.T_Ap_But2.setAutoExclusive(False)
        self.T_Ap_But2.setAutoDefault(False)
        self.T_Ap_But2.setDefault(False)
        self.T_Ap_But2.setFlat(False)
        self.T_Ap_But2.setObjectName("T_Ap_But2")

        self.groupBox.raise_()
        self.horizontalScrollBar.raise_()
        self.groupBox_2.raise_()
        self.calendarWidget.raise_()
        
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

#        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Create first tab

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 250, 1000, 480))
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setStyleSheet("pane { border: 1px; background: rgb(205, 250, 255)} tab-bar:top {top: 1px} QTabBar::tab:selected {background: rgb(17, 50, 100)} QTabBar::tab:!selected {background: rgb(50, 145, 205)} ;")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setFont(font)

        self.layout = QVBoxLayout(self.groupBox_3)
        #label1 = QLabel("Widget in Tab 1.")
        self.tabwidget = QTabWidget()
        self.tabwidget.setStyleSheet("background-color: rgb(17, 50, 100);\n"
"color: rgb(205, 250, 255); ")
        self.tabwidget.setFont(font)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabwidget.addTab(self.tab1,"|Progress|")
        self.tabwidget.addTab(self.tab2,"|GANTT|")
        self.tabwidget.addTab(self.tab3,"|Network|")
        #self.tabwidget.addTab(label1, "Tab 1")
        self.layout.addWidget(self.tabwidget)

        #self.graphWidget = pg.PlotWidget(self.groupBox_3)
        self.graphWidget = pg.PlotWidget(self.tab1)
        self.graphWidget.setGeometry(QtCore.QRect(10, 20, 900, 400))
#        self.setCentralWidget(self.graphWidget)
        time = [1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        PV = [2.4, 3.48, 5, 7.14, 10.1, 14.1, 19.34, 26, 33.86, 42.8, 52, 61.5, 70, 77.3, 83.28, 88, 91.4, 94, 95.8, 97]
        EV = [2.23, 3.18, 4.5, 6.33, 8.84, 12.2, 16.56, 22, 28.64, 36, 44, 52, 60, 66.8, 72.5, 77, 80.6, 83.25, 85.2, 86.6]
        #Add Background colour
        #self.graphWidget.setBackground('rgb(17, 50, 100)')
        self.graphWidget.setBackground(None)
        #Add Title
        self.graphWidget.setTitle("Progress Curve")
        #Add Axis Labels
        self.graphWidget.setLabel('left', 'Project Value', color='red', size=30)
        self.graphWidget.setLabel('bottom', 'Time', color='red', size=30)
        #Add legend
        self.graphWidget.addLegend()
        #Add grid
        self.graphWidget.showGrid(x=True, y=True)
        #Set Range
        self.graphWidget.setXRange(0, 10, padding=0)
        self.graphWidget.setYRange(0, 100, padding=0)
        self.graphWidget.showGrid(x=True, y=True)
        
#        self.plot(time, PV, "PV", 'r')
#        self.plot(time, EV, "EV", 'b')
#######Graph Tab########
#        df = pd.read_csv('gantt.csv')

#        colors = ['#7a0504', (0.2, 0.7, 0.3), 'rgb(205, 250, 255)']




#######Graph Tab########

        self.T_force1 = QtWidgets.QPushButton(self.centralwidget)
        self.T_force1.setGeometry(QtCore.QRect(50, 720, 150, 57))
        self.T_force1.setFont(font)
        self.T_force1.setAutoFillBackground(False)
        self.T_force1.setStyleSheet("QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch; color: rgb(205, 250, 255)}" "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch; color: rgb(200, 0, 5)}" "QPushButton:disabled { border-image: url(But3.png) 0 0 0 0 stretch stretch; color: rgb(50, 145, 205)}" "background-repeat: no-repeat;"  "background-position: center center;" "background-repeat: no-repeat;"  "background-position: center center;" )
        self.T_force1.setText("|NETWORK|")
        self.T_force1.setIconSize(QtCore.QSize(150, 57))
        self.T_force1.setCheckable(False)
        self.T_force1.setAutoRepeat(False)
        self.T_force1.setAutoExclusive(False)
        self.T_force1.setAutoDefault(False)
        self.T_force1.setDefault(False)
        self.T_force1.setFlat(False)
        self.T_force1.setObjectName("T_force1")
        self.T_force1.clicked.connect(self.on_T_force1_clicked)
        
        self.T_GANTT1 = QtWidgets.QPushButton(self.centralwidget)
        self.T_GANTT1.setGeometry(QtCore.QRect(250, 720, 150, 57))
        self.T_GANTT1.setFont(font)
        self.T_GANTT1.setAutoFillBackground(False)
        self.T_GANTT1.setStyleSheet("QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch; color: rgb(205, 250, 255)}" "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch; color: rgb(200, 0, 5)}" "QPushButton:disabled { border-image: url(But3.png) 0 0 0 0 stretch stretch; color: rgb(50, 145, 205)}" "background-repeat: no-repeat;"  "background-position: center center;" "background-repeat: no-repeat;"  "background-position: center center;" )
        self.T_GANTT1.setText("|GANTT|")
        self.T_GANTT1.setIconSize(QtCore.QSize(150, 57))
        self.T_GANTT1.setCheckable(False)
        self.T_GANTT1.setAutoRepeat(False)
        self.T_GANTT1.setAutoExclusive(False)
        self.T_GANTT1.setAutoDefault(False)
        self.T_GANTT1.setDefault(False)
        self.T_GANTT1.setFlat(False)
        self.T_GANTT1.setObjectName("T_GANTT1")
        self.T_GANTT1.clicked.connect(self.on_T_GANTT1_clicked)


        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1100, 10, 80, 78))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("circle2.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        
        # create list of floats
        y1 = np.linspace(0, 20, num=20)
        # create horizontal list
        x = np.arange(20)

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=10, symbolBrush=(color))

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
        self.groupBox.setTitle(_translate("MainWindow", "Baseline Transaction"))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle(_translate("MainWindow", "Realized Transaction"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_unsubmitted_Transaction.setText(_translate("MainWindow", "Open unsubmitted Transaction"))
        self.actionNew_Transaction.setText(_translate("MainWindow", "New Transaction"))

    def on_T_Cr_But1_clicked(self):
        import sys
 #       app = QtWidgets.QApplication(sys.argv)
 #       window = Window()
 #       window.show()
        self.window = Window()
        self.window.show()

    def on_T_force1_clicked(self):
        import sys
 #       app = QtWidgets.QApplication(sys.argv)
 #       window = Window()
 #       window.show()
        self.window = Net2()
        self.window.show()

    def on_T_GANTT1_clicked(self):
        import sys
        self.window = GANTT2()
        self.window.show()

    def on_T_Ed_But2_clicked(self):
        import sys
        self.openFileNameDialog()
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
    
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class Net2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Net2, self).__init__(parent)
        self.ui = Ui_Force()
        self.ui.setupUi(self)

class GANTT2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(GANTT2, self).__init__(parent)
        self.ui = Ui_GANTT()
        self.ui.setupUi(self)
        
if __name__ == "__main__":
#    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_PropWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
 #   sys.exit(app.exec_())


