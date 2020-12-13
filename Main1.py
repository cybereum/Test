# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Trans1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

# Prefix coding of JSON files
# 1- Participant certificate request 
# 2- Participant certificate 
# 3- Project certificate request 
# 4- Project certificate 
# 5- Proposed Baseline Transaction
# 6- Approved Baseline Transaction
# 7- Proposed Realized Transaction
# 8- Approved Realized Transaction
# U- Participants on Platform
# V- Participants specific to project
# P- Projects on Platform
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAbstractItemView, QApplication, QListWidget, QListWidgetItem, QVBoxLayout, QWidget
import json
import ecdsa
from ecdsa import SigningKey, VerifyingKey
from ecdsa.util import sigencode_der, sigdecode_der
from ecdsa import BadSignatureError
#from ellipticcurve.ecdsa import Ecdsa
#from ellipticcurve.privateKey import PrivateKey
#from ellipticcurve.publicKey import PublicKey

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 762)
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
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 700, 761, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(390, 42, 350, 135))
        self.calendarWidget.setStyleSheet("background-color: rgb(17, 50, 100);\n" "color: rgb(205, 250, 255); ")
        self.calendarWidget.setObjectName("calendarWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 42, 350, 255))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("background-color: rgb(17, 50, 100);\n" 
"color: rgb(205, 250, 255); ")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 32, 150, 21))
        self.label.setStyleSheet("color: rgb(205, 250, 255); ")
        self.label.setObjectName("label")
        self.Trans_Tim = QtWidgets.QDateTimeEdit(self.groupBox)
        self.Trans_Tim.setGeometry(QtCore.QRect(200, 32, 150, 30))
        self.Trans_Tim.setObjectName("Trans_Tim")
        self.Trans_Tim.setCalendarPopup(True)
        self.Trans_Tim.setDateTime(QtCore.QDateTime.currentDateTime())

        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 155, 131, 16))
        self.label_8.setObjectName("label_8")

        self.Prev_Milestones = QtWidgets.QListWidget(self.groupBox)
        self.Prev_Milestones.setGeometry(QtCore.QRect(200, 155, 120, 74))
        self.Prev_Milestones.setObjectName("Prev_Milestones")
        self.Prev_Milestones.setSelectionMode(QAbstractItemView.MultiSelection)
        self.Prev_Milestones.setSelectionMode(QAbstractItemView.MultiSelection)

        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(10, 70, 150, 20))
        self.label_1.setObjectName("label_1")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(200, 70, 80, 28))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.textChanged.connect(self.on_Dur_changed)
        self.comboBox_8 = QtWidgets.QListWidget(self.groupBox)
        self.comboBox_8.setGeometry(QtCore.QRect(290, 71, 60, 40))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.setStyleSheet("background-color: rgb(15, 45, 80);\n" "color: rgb(205, 250, 255); \n""")
        self.comboBox_8.setSelectionMode(QAbstractItemView.MultiSelection)
        self.comboBox_8.addItem('days')
        self.comboBox_8.addItem('hours')
        self.comboBox_8.addItem('weeks')
        self.comboBox_8.setCurrentRow(0)

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 115, 150, 20))
        self.label_2.setObjectName("label_2")
        self.Fin_Tim = QtWidgets.QDateTimeEdit(self.groupBox)
        self.Fin_Tim.setGeometry(QtCore.QRect(200, 105, 150, 50))
        self.Fin_Tim.setObjectName("Fin_Tim") 
        self.Fin_Tim.dateTimeChanged.connect(self.on_tim2_changed)   
        self.Fin_Tim.setCalendarPopup(True)
        self.Fin_Tim.setDateTime(QtCore.QDateTime.currentDateTime())
        self.Fin_Tim.setReadOnly(True)

        self.Trans_Tim.dateTimeChanged.connect(self.on_tim_changed)  



        self.T_Sub_But1 = QtWidgets.QPushButton(self.centralwidget)
        self.T_Sub_But1.setGeometry(QtCore.QRect(310, 533, 150, 57))
        
        font = QtGui.QFont()
        #font.setFamily("Baskerville")
        font.setFamily("orbitron")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(25)
        font.setLetterSpacing(font.AbsoluteSpacing, 5)
        font.setCapitalization(font.SmallCaps)

        self.T_Sub_But1.setFont(font)
        self.T_Sub_But1.setAutoFillBackground(False)
        self.T_Sub_But1.setStyleSheet("QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch; color: rgb(205, 250, 255)}" "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch; color: rgb(200, 0, 5)}" "QPushButton:disabled { border-image: url(But3.png) 0 0 0 0 stretch stretch; color: rgb(50, 145, 205)}" "background-repeat: no-repeat;"  "background-position: center center;" "background-repeat: no-repeat;"  "background-position: center center;" )
        self.T_Sub_But1.setText("|SUBMIT|")
        self.T_Sub_But1.setIconSize(QtCore.QSize(150, 57))
        self.T_Sub_But1.setCheckable(False)
        self.T_Sub_But1.setAutoRepeat(False)
        self.T_Sub_But1.setAutoExclusive(False)
        self.T_Sub_But1.setAutoDefault(False)
        self.T_Sub_But1.setDefault(False)
        self.T_Sub_But1.setFlat(False)
        self.T_Sub_But1.setObjectName("T_Sub_But1")
        self.T_Sub_But1.clicked.connect(self.on_T_Sub_But1_clicked)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 602, 150, 148))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("circle2.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")

        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)   # Transaction id Groupbox
        self.groupBox_4.setGeometry(QtCore.QRect(390, 180, 350, 120))
        self.groupBox_4.setAutoFillBackground(False)
        self.groupBox_4.setStyleSheet("background-color: rgb(17, 50, 100);\n" "color: rgb(205, 250, 255); \n"
"")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(10, 30, 141, 16))
        self.label_20.setObjectName("label_20")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_20.setGeometry(QtCore.QRect(200, 30, 120, 28))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(10, 70, 151, 16))
        self.label_21.setObjectName("label_21")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_21.setGeometry(QtCore.QRect(200, 70, 120, 28))
        self.lineEdit_21.setObjectName("lineEdit_21")



        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 311, 350, 216))
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet("background-color: rgb(17, 50, 100);\n" "color: rgb(205, 250, 255); \n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(10, 32, 91, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 133, 111, 16))
        self.label_13.setObjectName("label_13")
        self.comboBox_4 = QtWidgets.QListWidget(self.groupBox_2)
        self.comboBox_4.setGeometry(QtCore.QRect(200, 133, 120, 74))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.setStyleSheet("background-color: rgb(15, 45, 80);\n" "color: rgb(205, 250, 255); \n""")
        self.comboBox_4.setSelectionMode(QAbstractItemView.MultiSelection)

        self.comboBox_5 = QtWidgets.QListWidget(self.groupBox_2)
        self.comboBox_5.setGeometry(QtCore.QRect(200, 32, 120, 74))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.setStyleSheet("background-color: rgb(15, 45, 80);\n" "color: rgb(205, 250, 255); \n""")
        self.comboBox_5.setSelectionMode(QAbstractItemView.MultiSelection)

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 311, 350, 216))
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setStyleSheet("background-color: rgb(17, 50, 100);\n" "color: rgb(205, 250, 255); \n"
"")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(10, 30, 141, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 30, 120, 28))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(10, 70, 151, 16))
        self.label_17.setObjectName("label_17")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 70, 120, 28))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(10, 110, 151, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setGeometry(QtCore.QRect(10, 150, 151, 16))
        self.label_19.setObjectName("label_19")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(200, 110, 120, 28))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(200, 150, 120, 28))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(200, 10, 150, 20))
        self.radioButton.setStyleSheet("color: rgb(50, 145, 205); ")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 10, 150, 20))
        self.radioButton_2.setStyleSheet("color: rgb(205, 250, 255); ")
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
   
  
        self.groupBox.raise_()
        self.horizontalScrollBar.raise_()
        self.calendarWidget.raise_()
        self.T_Sub_But1.raise_()
        self.label_7.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()


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

###Populate textboxes
        filename_out = 'participants.txt'
        prt_read = open(filename_out,'r') 
        for i in prt_read:
            self.comboBox_5.addItem(i)
            self.comboBox_4.addItem(i)

        filename_out = 'predecessors.txt'
        prt_read = open(filename_out,'r') 
        for i in prt_read:
            self.Prev_Milestones.addItem(i)
###Populate textboxes

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
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
        self.groupBox_2.setFont(font)
        self.groupBox_3.setFont(font)
        self.groupBox_4.setFont(font)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle(_translate("MainWindow", "Transaction Entry"))
        self.groupBox.setTitle(_translate("MainWindow", "Time/Schedule"))
        self.label.setText(_translate("MainWindow", "Time of commencement"))
        self.label_8.setText(_translate("MainWindow", "Preceding Milestones"))
        self.label_1.setText(_translate("MainWindow", "Duration"))
        self.label_2.setText(_translate("MainWindow", "Time of completion"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Participants"))
        self.label_12.setText(_translate("MainWindow", "Value Creaters"))
        self.label_13.setText(_translate("MainWindow", "Endorsers"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Value/Cost"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Transaction id"))
        self.label_16.setText(_translate("MainWindow", "Planned Value Created"))
        self.label_17.setText(_translate("MainWindow", "Cost/Price"))
        self.label_18.setText(_translate("MainWindow", "Incentive/day"))
        self.label_19.setText(_translate("MainWindow", "Penalty/day"))
        self.label_20.setText(_translate("MainWindow", "Milestone ID"))
        self.label_21.setText(_translate("MainWindow", "Milestone name"))
        self.radioButton.setText(_translate("MainWindow", "Realized Transaction"))
        self.radioButton_2.setText(_translate("MainWindow", "Baseline Transaction"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_unsubmitted_Transaction.setText(_translate("MainWindow", "Open unsubmitted Transaction"))
        self.actionNew_Transaction.setText(_translate("MainWindow", "New Transaction"))


    def on_Dur_changed(self):
        print('dur changed')
        #qtDate3 = QtCore.QDate.fromString
        #self.Fin_Tim
        #self.Fin_Tim.addDays(2)
        # self.Fin_Tim.setDateTime.addDays(2)
        # currentTime = QDateTime.currentDateTime()
        # dateTimeBegin.setDateTime(currentTime.addDays(7))
        # self.Fin_Tim.setDateTime(self.dt.addDays(7))
        # self.Fin_Tim = self.Fin_Tim.addDays(7)
        # self.Fin_Tim.setDateTime(QtCore.QDateTime.currentDateTime())

        #self.Fin_Tim = QtWidgets.QDateTimeEdit(self.groupBox)
        if self.lineEdit_7.text() != '':
            print(int(self.lineEdit_7.text()))
            dur1 = int(self.lineEdit_7.text())
            self.dt = self.Trans_Tim.dateTime()
            self.Fin_Tim.setDateTime(self.dt.addDays(dur1))



        # self.dateTimeBegin = QDateTimeEdit()
        # self.dt = self.dateTimeBegin.dateTime().currentDateTime()
        # self.dateTimeBegin.setDateTime(self.dt.addDays(7))
        # self.dt = self.dt.addDays(7)

    def on_tim_changed(self):
        print('tim changed')
        #qtDate3 = QtCore.QDate.fromString
        #self.Fin_Tim       
        if self.lineEdit_7.text() != '':
            print(int(self.lineEdit_7.text()))
            dur1 = int(self.lineEdit_7.text())
            self.dt = self.Trans_Tim.dateTime()
            self.Fin_Tim.setDateTime(self.dt.addDays(dur1))

        if self.lineEdit_7.text() == '':
            print('xx')
            dur1 = 0
            self.dt = self.Trans_Tim.dateTime()
            self.Fin_Tim.setDateTime(self.dt)
    
    def on_tim2_changed(self):
        print('tim changed')



    def on_T_Sub_But1_clicked(self):
        print('auth called')
        filename_out = 'test.txt'
        csv_out = open(filename_out,'w') 
        csv_out = open(filename_out,'a')
        csv_out.write('Hi')
        a2 = str(self.Trans_Tim.text)
        csv_out.write(a2)
        #Predecessors = self.Prev_Milestones.currentText()
        #Creaters1 = self.comboBox_5.selectedItems()
        Predecessors = []
        for item in self.Prev_Milestones.selectedItems():
            Predecessors.append(item.text())
        Creaters1 = []
        for item in self.comboBox_5.selectedItems():
            Creaters1.append(item.text())
        Endorsers1 = []
        for item in self.comboBox_4.selectedItems():
            Endorsers1.append(item.text())

        #Endorsers1 = self.comboBox_4.currentText()
        Val_Cr = [self.lineEdit_5.text]

        pk_pr = VerifyingKey.from_pem(open("user_public.pem").read()) # Get Project Promoter public key from their participant pem
        pk_pr = pk_pr.to_string().hex()
        pk_pr = str(pk_pr)

        with open('test.txt', 'w') as f:
            for item in Creaters1:
                f.write("%s\n" % "1")
                f.write("%s\n" % str(item))
                f.write(str(len(Creaters1)))
                f.write("%s\n" % "2")
        dcent2 = {"Time of commencement": str(self.Trans_Tim.text()), "Duration": self.lineEdit_7.text(), "Time of attainment": str(self.Fin_Tim.text()), "Preceding Milestones": Predecessors,  "Planned Value Created": str(self.lineEdit_5.text()),"Cost/Price": str(self.lineEdit_6.text()),"Value Creaters": Creaters1, "Endorsers": Endorsers1}# Sorted Degree Centrality
 #       dcent2 = {"Time of attainment": str(self.Trans_Tim.text),  "Planned Value Created": str(self.lineEdit_5.text), "Preceding Milestones": Predecessors}
        json_prep = {"Time/Schedule":dcent2}
        json_prep.keys()
        json_dump = json.dumps(json_prep, indent=1, sort_keys=True)
        filename_out2 = '5-base-trans_prop-' + str(self.lineEdit_20.text()) + '.json'
        print('fname', filename_out2)
        json_out = open(filename_out2,'w')
        json_out.write(json_dump)
        json_out.close()

        #####SIGN######
        with open("user_private.pem") as f: # Get Project Promoter private key from their participant pem
            sk_pr = SigningKey.from_pem(f.read())
        with open(filename_out2, "rb") as f:
            message = f.read()
        sig = sk_pr.sign(message)
        sig2 = sk_pr.sign(message)
        print('signature')
        print(sig)
        with open("signature2", "wb") as f:
            f.write(sig)
        print(sig)
        with open("signature", "rb") as f:
            sig2 = f.read()
        print(sig2)
        sig = str(sk_pr.sign(message))
        print(sig)
        print('signature')
        #sig = sig.to_string().hex()
        #####SIGN######


        Header = {"Milestone ID:": str(self.lineEdit_20.text()), "Milestone Name:": str(self.lineEdit_21.text()), "Time:": QtCore.QDateTime.currentDateTime().toString(), "Project Promotor Pub-Key": pk_pr, "Promotor Signature": sig}
        json_prep = {"Transaction_info":dcent2, "Header": Header}
        json_prep.keys()
        json_dump = json.dumps(json_prep, indent=1, sort_keys=True)
        json_out = open(filename_out2,'w')
        json_out.write(json_dump)
        json_out.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

