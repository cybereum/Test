# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'force1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QBrush, QPen
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import csv
import plotly.offline as po
import plotly.graph_objs as go
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
#import urllib2

class Ui_GANTT(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1200)
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
        self.horizontalScrollBar.setGeometry(QtCore.QRect(10, 740, 761, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(825, 480, 50, 51))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../../Blockchain_Schedule/Logos/circle2.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")


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
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.actionOpen_unsubmitted_Transaction = QtWidgets.QAction(MainWindow)
        self.actionOpen_unsubmitted_Transaction.setObjectName("actionOpen_unsubmitted_Transaction")
        self.actionNew_Transaction = QtWidgets.QAction(MainWindow)
        self.actionNew_Transaction.setObjectName("actionNew_Transaction")
        self.menuFile.addAction(self.actionOpen_unsubmitted_Transaction)
        self.menuFile.addAction(self.actionNew_Transaction)
        self.menubar.addAction(self.menuFile.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 500, 250))
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet("background-color: rgb(17, 50, 100);\n"
"color: rgb(205, 250, 255); ")
        self.groupBox_2.setObjectName("groupBox_2")

        self.fileName = 'gantt.csv'
        self.model = QtGui.QStandardItemModel(self.groupBox_2)
        self.tableView = QtWidgets.QTableView(self.groupBox_2)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.layoutVertical = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.layoutVertical.addWidget(self.tableView)
        self.loadCsv(self.fileName)



        



        ########################-Chart-########################
        #df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gantt_example.csv')
        df = pd.read_csv('gantt.csv')

        #fileName = 'gantt.csv'
        #loadCsv(self.fileName)

        colors = ['#7a0504', (0.2, 0.7, 0.3), 'rgb(205, 250, 255)']

        fig = ff.create_gantt(df, colors=['rgb(160, 240, 255)', 'rgb(15, 45, 80)'], index_col='Complete',
                      show_colorbar=True, bar_width=0.2, showgrid_x=True, showgrid_y=True)
        #fig = ff.create_gantt(df, colors=colors, index_col='Resource',     reverse_colors=True,show_colorbar=True)

        #py.offline.plot(fig, filename='gantt2')

        #fig = go.Figure(data=[{'type': 'scattergl', 'y': [2, 1, 3, 1]}])

    #######################Progress bars##############
        x1=1
        print('time')
        print(df.iloc[:,1])
        print(df.iloc[1:1])
        print(df.iloc[2:1])
        print('start')
        print(df.iloc[1]['Start'])
        print('finish')
        print(df.iloc[1]['Finish'])
        total_rows = len(df.index)
        print('rows')
        print(total_rows)
        print('time')

        self.scrollarea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollarea.setGeometry(QtCore.QRect(50, 260, 900, 700))
        #self.scrollarea.setFixedSize(250, 6000)
        self.scrollarea.setWidgetResizable(True)
        qtDate1 = QtCore.QDate.fromString(df.iloc[0]['Start'], 'yyyy-MM-dd') #get first date
        print(int(total_rows))
        qtDate2 = QtCore.QDate.fromString(df.iloc[int(total_rows)-1]['Finish'], 'yyyy-MM-dd') #get last date
        date2 = qtDate1.daysTo(qtDate2)
        print(date2)
        ra1 = 500/date2

        for i in range(total_rows):
            y1 = x1*30 + 60
            print(df.iloc[i]['Start'])
            print(df.iloc[i]['Finish'])
            qtDate3 = QtCore.QDate.fromString(df.iloc[i]['Start'], 'yyyy-MM-dd')
            qtDate4 = QtCore.QDate.fromString(df.iloc[i]['Finish'], 'yyyy-MM-dd')
            date3 = qtDate3.daysTo(qtDate4) #calculate length of progress bar
            date5 = qtDate1.daysTo(qtDate3) #calculate start of progress bar
            print(date3)

            xp1 = 550 + int(date5)
            print("ratio")
            print(int(date2)/500)
            #print(df.iloc[i]['Finish'] - df.iloc[i]['Start'])

            self.label_15 = QtWidgets.QLabel(self.centralwidget)
            self.label_15.setGeometry(QtCore.QRect(530, y1, 10, 20))
            font = QtGui.QFont()
            font.setKerning(True)
            self.label_15.setFont(font)
            self.label_15.setAutoFillBackground(False)
            self.label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.label_15.setText("|")
            self.label_15.setStyleSheet( "color: rgb(205, 250, 255); ")

            self.progressBar2 = QtWidgets.QProgressBar(self.centralwidget)
            self.progressBar2.setGeometry(QtCore.QRect(xp1, y1, int(date3)*ra1, 20))
            print(int(date3)*ra1)
            complete1 = int(df.iloc[i]['Complete'])



            self.progressBar2.setProperty("value", complete1)
            self.progressBar2.setObjectName("progressBar2")
            self.progressBar2.setStyleSheet("QProgressBar { border: 2px solid rgb(140, 230, 255); border-radius: 5px; color: rgb(255, 0, 25);}" "QProgressBar::chunk {background-color: rgb(205, 250, 255); color: rgb(255, 0, 25); width: 12px; margin: 0.5px;}")
            self.progressBar2.raise_()




            lines = QtGui.QPainter(self.centralwidget)
            #lines.setPen(QPen(Qt.green,  8, Qt.DashLine))
            lines.setPen(QtCore.Qt.red)
            lines.setBrush(QtCore.Qt.white)
            #lines.drawLine(500,y1+80,1000,y1+80)
            lines.drawLine(500,80,1000,80)
            x1 = x1 + 1
        
        self.paintEvent(self)
    #######################Progress bars##############

    #######################GANTT##############
        raw_html = '<html><head><meta charset="utf-8" />'
        raw_html += '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script></head>'
        raw_html += '<body>'
        raw_html += po.plot(fig, include_plotlyjs=False, output_type='div')
        raw_html += '</body></html>'

        #fig_view = QWebEngineView()
        #fig_view = QWebEngineView(self.groupBox_5)
        #fig_view = QWebEngineView(self.groupBox_5)
        fig_view = QWebEngineView(self.scrollarea)
        fig_view.setGeometry(QtCore.QRect(20, 20, 700, 700))
        self.scrollarea.setWidget(fig_view)
        # setHtml has a 2MB size limit, need to switch to setUrl on tmp file
        # for large figures.
        fig_view.setHtml(raw_html)
        fig_view.show()
        fig_view.raise_()

        #fig_view = show_qt(fig)

        ########################-Chart-########################



        #self.model = QtGui.QStandardItemModel(self)

        #self.tableView = QtWidgets.QTableView(self)
        #self.tableView.setModel(self.model)
        #self.tableView.horizontalHeader().setStretchLastSection(True)

        #target_url = "http://www.google.com")
        #data = urllib2.urlopen(target_url) # it's a file like object and works just like a file
        #for line in data: # files are iterable
            #print line

        #data = urllib2.urlopen("http://www.google.com").read(20000) # read only 20 000 chars
        #data = data.split("\n") # then split it into lines
        #for line in data:
            #print(line)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GANTT"))
        #self.groupBox_2.setTitle(_translate("MainWindow", "GANTT"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_unsubmitted_Transaction.setText(_translate("MainWindow", "Open unsubmitted Transaction"))
        self.actionNew_Transaction.setText(_translate("MainWindow", "New Transaction"))

#from QtWebEngineWidgets.QWebEngineView import QWebEngineView

    def loadCsv(self, fileName):
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

    def writeCsv(self, fileName):
        with open(fileName, "w") as fileOutput:
            writer = csv.writer(fileOutput)
            for rowNumber in range(self.model.rowCount()):
                fields = [
                    self.model.data(
                        self.model.index(rowNumber, columnNumber),
                        QtCore.Qt.DisplayRole
                    )
                    for columnNumber in range(self.model.columnCount())
                ]
                writer.writerow(fields)





    def addWidget(y):

        #self.y += 1
        y = 1
        y1 = y*25


        #self.widget = ExampleWidget(self.numAddWidget)
        #self.groupBox_6.addWidget(self.widget)


    def paintEvent(self, event):
        painter = QPainter()
        #painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QtCore.Qt.red)
        painter.setBrush(QtCore.Qt.white)
        painter.drawLine(550, 600, 1050, 600)
        painter.drawLine(550, 600, 550, 40)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_GANTT()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

