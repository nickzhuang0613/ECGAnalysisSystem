from PyQt4 import QtCore, QtGui
import sys
from biosppy import ecg
import matplotlib.pyplot as plt


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def details(qrscount,ptcount,qrstime,hamveri,Fs):
    global QRScount
    global PTcount
    global QRStime
    global veri
    global samp_rate
    samp_rate = Fs
    veri = hamveri
    QRScount = qrscount
    QRStime = qrstime
    PTcount = ptcount

class Ui_OtherWindow(QtGui.QWidget):
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName(_fromUtf8("OtherWindow"))
        OtherWindow.resize(475, 235)
        self.centralwidget = QtGui.QWidget(OtherWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.lbl_qrscount = QtGui.QLabel(self.centralwidget)
        self.lbl_qrscount.setGeometry(QtCore.QRect(160, 40, 62, 20))
        self.lbl_qrscount.setObjectName(_fromUtf8("lbl_qrscount"))
        self.lbl_qrscount.setText(str(QRScount))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 141, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 81, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lbl_ptcount = QtGui.QLabel(self.centralwidget)
        self.lbl_ptcount.setGeometry(QtCore.QRect(160, 70, 62, 20))
        self.lbl_ptcount.setObjectName(_fromUtf8("lbl_ptcount"))
        self.lbl_ptcount.setText(str(PTcount))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 100, 62, 20))
        self.label_5.setObjectName(_fromUtf8("lbl_qrstime"))
        self.label_5.setText(str(QRStime))
        self.btn_ayrinti = QtGui.QPushButton(self.centralwidget)
        self.btn_ayrinti.setGeometry(QtCore.QRect(340, 125, 125, 28))
        self.btn_ayrinti.clicked.connect(self.get_temps)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ayrinti.setFont(font)
        self.btn_ayrinti.setObjectName(_fromUtf8("btn_analyze"))
        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(OtherWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Ayrıntılar", None))
        self.label.setText(_translate("OtherWindow", "QRS Sayısı:", None))
        self.label_3.setText(_translate("OtherWindow", "QRS Ortalama Süresi:", None))
        self.label_6.setText(_translate("OtherWindow", "PT Sayısı:", None))
        self.btn_ayrinti.setText(_translate("OtherWindow","Ayrıntı Göster",None))

    def get_temps(self):
        ts, filtered, rpeaks, ts_tmpl, templates, ts_hr, hr = ecg.ecg(signal=veri, sampling_rate=samp_rate, show=False)
        plt.subplot(2,1,1)
        plt.plot(ts_tmpl,templates.T)
        plt.xlabel("Zaman(sn)")
        plt.ylabel("Genlik")
        plt.title("Sinyal Taslağı")
        plt.subplots_adjust(hspace=0.5)
        plt.subplot(2,1,2)
        plt.plot(ts_hr,hr)
        plt.xlabel("Zaman(sn)")
        plt.ylabel("Kalp Atış(BPM)")
        plt.title("Kalp Atım")
        plt.show()



if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    OtherWindow = QtGui.QMainWindow()
    ui=Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())

