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

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QListWidget, QListWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import json
import ecdsa
from ecdsa import SigningKey, VerifyingKey
from ecdsa.util import sigencode_der, sigdecode_der
from ecdsa import BadSignatureError
#from ellipticcurve.ecdsa import Ecdsa
#from ellipticcurve.privateKey import PrivateKey
#from ellipticcurve.publicKey import PublicKey
#import urllib2

class Ui_ProjCert(object):
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
        self.calendarWidget.setGeometry(QtCore.QRect(530, 10, 220, 181))
        self.calendarWidget.setStyleSheet("background-color: rgb(17, 50, 100);\n" "color: rgb(205, 250, 255); ")
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setAutoFillBackground(True)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 250, 350, 175))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("background-color: rgb(17, 50, 100);\n" 
"color: rgb(205, 250, 255); ")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 33, 150, 29))
        self.label.setStyleSheet("color: rgb(205, 250, 255); ")
        self.label.setObjectName("label")
        self.Trans_Tim = QtWidgets.QDateTimeEdit(self.groupBox)
        self.Trans_Tim.setGeometry(QtCore.QRect(190, 28, 150, 50))
        self.Trans_Tim.setObjectName("Trans_Tim")       
        self.Trans_Tim.setCalendarPopup(True)
        self.Trans_Tim.setDateTime(QtCore.QDateTime.currentDateTime())
        

        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(10, 75, 150, 20))
        self.label_1.setObjectName("label_1")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(200, 76, 80, 28))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.textChanged.connect(self.on_Dur_changed)
        self.comboBox_8 = QtWidgets.QListWidget(self.groupBox)
        self.comboBox_8.setGeometry(QtCore.QRect(290, 73, 60, 40))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.setStyleSheet("background-color: rgb(15, 45, 80);\n" "color: rgb(205, 250, 255); \n""")
        self.comboBox_8.setSelectionMode(QAbstractItemView.MultiSelection)
        self.comboBox_8.addItem('days')
        self.comboBox_8.addItem('hours')
        self.comboBox_8.addItem('weeks')
        #self.comboBox_8.setCurrentIndex(1)
        self.comboBox_8.setCurrentRow(0)
        #self.comboBox_8.setCurrentText('hourr')
        #index = self.comboBox_8.findText('hours', QtCore.Qt.MatchFixedString)
        #if index >= 0:
        #    self.comboBox_8.setCurrentIndex(index)
        #self.comboBox_8.currentTextChanged.connect(self.on_tim_changed) 
        
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 115, 150, 20))
        self.label_2.setObjectName("label_2")
        self.Fin_Tim = QtWidgets.QDateTimeEdit(self.groupBox)
        self.Fin_Tim.setGeometry(QtCore.QRect(190, 105, 150, 50))
        self.Fin_Tim.setObjectName("Fin_Tim") 
        self.Fin_Tim.dateTimeChanged.connect(self.on_tim2_changed)   
        self.Fin_Tim.setCalendarPopup(True)
        self.Fin_Tim.setDateTime(QtCore.QDateTime.currentDateTime())
        self.Fin_Tim.setReadOnly(True)

        self.Trans_Tim.dateTimeChanged.connect(self.on_tim_changed)  
        


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

        self.T_Sub_But1.setFont(font)
        self.T_Sub_But1.setAutoFillBackground(False)
        #self.T_Sub_But1.setStyleSheet("QPushButton { border-image: url(But1.png) 0 0 0 0 stretch stretch; color: rgb(205, 250, 255)}" "QPushButton:pressed { border-image: url(But2-2.png) 0 0 0 0 stretch stretch; color: rgb(50, 145, 205)}" "background-repeat: no-repeat;"  "background-position: center center;")
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
        self.label_7.setGeometry(QtCore.QRect(310, 582, 150, 148))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("circle2.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 250, 350, 175))
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet("background-color: rgb(17, 50, 100);\n" "color: rgb(205, 250, 255); \n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(10, 40, 150, 16))
        self.label_12.setObjectName("label_12")

        self.comboBox_5 = QtWidgets.QListWidget(self.groupBox_2)
        self.comboBox_5.setGeometry(QtCore.QRect(200, 32, 120, 120))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.setStyleSheet("background-color: rgb(15, 45, 80);\n" "color: rgb(205, 250, 255); \n""")
        self.comboBox_5.setSelectionMode(QAbstractItemView.MultiSelection)

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 40, 350, 200))
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setStyleSheet("background-color: rgb(17, 50, 100);\n" "color: rgb(205, 250, 255); \n"
"")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(10, 30, 141, 16))
        self.label_15.setObjectName("label_15")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(200, 30, 120, 28))
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(10, 70, 141, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 70, 120, 28))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(10, 110, 151, 16))
        self.label_17.setObjectName("label_17")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 110, 120, 28))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(10, 150, 151, 16))
        self.label_18.setObjectName("label_18")
        self.Location = QtWidgets.QComboBox(self.groupBox_3)
        self.Location.setGeometry(QtCore.QRect(200, 150, 120, 45))
        self.Location.setObjectName("Location")


   
  
        self.groupBox.raise_()
        self.horizontalScrollBar.raise_()
        self.T_Sub_But1.raise_()
        self.label_7.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()


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
       # for line in urllib2.urlopen(target_url):
            #print line


        filename_out = 'participants.txt'
        prt_read = open(filename_out,'r') 
        for i in prt_read:
            self.comboBox_5.addItem(i)

        filename_out = 'locations.txt'
        prt_read = open(filename_out,'r') 
        for i in prt_read:
            self.Location.addItem(i)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Transaction Entry"))
        self.groupBox.setFont(font)
        self.groupBox.setTitle(_translate("MainWindow", "Planned Timeline"))
        self.label.setText(_translate("MainWindow", "Time of commencement"))
        self.label_1.setText(_translate("MainWindow", "Duration"))
        self.label_2.setText(_translate("MainWindow", "Time of completion"))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle(_translate("MainWindow", "Participants"))
        self.label_12.setText(_translate("MainWindow", "Project Participants"))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setTitle(_translate("MainWindow", "Project Identity"))
        self.label_15.setText(_translate("MainWindow", "Project ID"))
        self.label_16.setText(_translate("MainWindow", "Project Name"))
        self.label_17.setText(_translate("MainWindow", "Project Field"))
        self.label_18.setText(_translate("MainWindow", "Location"))
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
        Location1 = self.Location.currentText()
        #Creaters1 = self.comboBox_5.selectedItems()
        Creaters1 = []
        #Endorsers1 = self.comboBox_4.currentText()
        #Endorsers1 = []
        Val_Cr = [self.lineEdit_5.text]
        #[Creaters1.append(item.text() for item in self.comboBox_5.selectedItems())]
        for item in self.comboBox_5.selectedItems():
            Creaters1.append(item.text())
        #[Endorsers1.append(item.text() for item in self.comboBox_5.selectedItems())]

        pk_pr = VerifyingKey.from_pem(open("user_public.pem").read()) # Get Project Promoter public key from their participant pem
        pk_pr = pk_pr.to_string().hex()
        pk_pr = str(pk_pr)
    
        with open('test.txt', 'w') as f:
            for item in Creaters1:
                f.write("%s\n" % "1")
                f.write("%s\n" % str(item))
                f.write(str(len(Creaters1)))
                f.write("%s\n" % "2")
        body = {"Start Time": str(self.Trans_Tim.text()), "Duration": self.lineEdit_7.text(), "Project Location": Location1,  "Project Name": str(self.lineEdit_5.text()),"Project Field": str(self.lineEdit_6.text()),"Participants": Creaters1}# Sorted Degree Centrality
 #       dcent2 = {"Time of attainment": str(self.Trans_Tim.text),  "Planned Value Created": str(self.lineEdit_5.text), "Preceding Milestones": Predecessors}
        #dcent2 = {"Time": str(self.Trans_Tim.text()), "Project Location": Location1,  "Project Name": str(self.lineEdit_5.text()),"Project Field": str(self.lineEdit_6.text())}#

        json_prep = {"Proj_info":body}
        json_prep.keys()
        json_dump = json.dumps(json_prep, indent=1, sort_keys=True)
        #filename_out2 = '3-Proj-cert_req.json'
        filename_out2 = '3-Proj-cert_req-' + str(self.lineEdit_9.text()) + '.json'
        json_out = open(filename_out2,'w')
        json_out.write(json_dump)
        json_out.close()

        #####-Key_Gen-######
        # Public key (ECDSA)
        sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) 
        

        vk = sk.get_verifying_key()
        #vkk = ecdsa.verifying_key()
        print('private_key_sk')
        sk_string = sk.to_string()
        print(sk)       
        print(sk_string.hex())
        sk_proj_pem = sk.to_pem()    # private key pem
        print('public_key_vk')
        vk_string = vk.to_string()
        print(vk)
        print(vk_string.hex())
        vk_proj_pem = vk.to_pem()    # public key pem
        print("uncompressed: {0}".format(vk.to_string("uncompressed").hex()))
        print("compressed: {0}".format(vk.to_string("compressed").hex()))

        proj_no = str(self.lineEdit_9.text()) # project counter
        proj_cert_pr = str(proj_no) + '-proj_private.pem' # project certificate indicates project number
        proj_cert_pu = str(proj_no) + '-proj_public.pem'

        ##-Write pem files
        with open(proj_cert_pr, "wb") as f:
            f.write(sk_proj_pem)
        with open(proj_cert_pu, "wb") as f:
            f.write(vk_proj_pem)
        ##-Write pem files

        #####-Key_Gen-######

        puk_proj = VerifyingKey.from_pem(open(proj_cert_pu).read()) # Get Project Promoter public key from their participant pem
        puk_proj = puk_proj.to_string().hex()
        puk_proj = str(puk_proj)

        #####SIGN######
        with open("user_private.pem") as f: # Get Project Promoter private key from their participant pem
            sk_pr = SigningKey.from_pem(f.read())
        with open(proj_cert_pr) as f: # Get Project Promoter private key from their participant pem
            sk_proj = SigningKey.from_pem(f.read())
        with open(filename_out2, "rb") as f:
            message = f.read()
        sig = sk_pr.sign(message)
        sig4 = sk_pr.sign(message)
        sig2 = sk_proj.sign(message)
        print('signature')
        print(sig)
        with open("signature", "wb") as f:
            f.write(sig)
        print(sig)
        with open("signature", "rb") as f:
            sig2 = f.read()
        print(sig2)
        sig = str(sk_pr.sign(message))
        sig2 = str(sk_proj.sign(message))
        print(sig)
        print('signature')
        #sig = sig.to_string().hex()
        #####SIGN######

        Header = {"Project ID:": str(self.lineEdit_9.text()), "Time:": QtCore.QDateTime.currentDateTime().toString(), "Project Promotor Pub-Key": pk_pr, "Promotor Signature": sig, "Project Pub-Key": puk_proj, "Project Signature": sig2}
        json_prep = {"Proj_info":body, "Header": Header}
        json_prep.keys()
        json_dump = json.dumps(json_prep, indent=1, sort_keys=True)
        #filename_out2 = '3-Proj-cert_req.json'
        json_out = open(filename_out2,'w')
        json_out.write(json_dump)
        json_out.close()

        #####VERIFY######
        # test code to verify signature - will be deployed at server or peer 
        vk = VerifyingKey.from_pem(open("user_public.pem").read())
        with open(filename_out2, "rb") as f:
            message = f.read()
            sig3 = json.loads(message)
            print(sig3['Header']['Promotor Signature'])
        try:
            vk.verify(sig4, message)
            print('good signature')
            x1 = vk.verify(sig4, message)
            print(x1)
        except BadSignatureError:
            print('BAD SIGNATURE')
        #####VERIFY######

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ProjCert()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

