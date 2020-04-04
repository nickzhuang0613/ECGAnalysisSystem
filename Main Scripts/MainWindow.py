from PyQt4 import QtCore, QtGui
import sys
from OtherWindow import Ui_OtherWindow
from GraphScript import GraphScript
from DetailScript import DetailScript


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

class Ui_MainWindow(object):
    def OpenWindow(self):
        time = self.txt_time.text()
        file = self.fileName
        DetailScript(file, time)
        self.window = QtGui.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(479, 386)
        MainWindow.setStyleSheet(_fromUtf8("background-image: url(:/resim/ecg.jpg);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.txt_time = QtGui.QLineEdit(self.centralwidget)
        self.txt_time.setGeometry(QtCore.QRect(90, 60, 113, 30))
        self.txt_time.setObjectName(_fromUtf8("txt_time"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 62, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.btn_analyze = QtGui.QPushButton(self.centralwidget)
        self.btn_analyze.setGeometry(QtCore.QRect(340, 60, 125, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_analyze.setFont(font)
        self.btn_analyze.setObjectName(_fromUtf8("btn_analyze"))
        self.btn_analyze.clicked.connect(self.OpenWindow)
        self.btn_quit = QtGui.QPushButton(self.centralwidget)
        self.btn_quit.setGeometry(QtCore.QRect(340, 100, 125, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_quit.setFont(font)
        self.btn_quit.setObjectName(_fromUtf8("btn_quit"))
        self.btn_file = QtGui.QPushButton(self.centralwidget)
        self.btn_file.setGeometry(QtCore.QRect(19, 300, 125, 28))
        self.btn_quit.clicked.connect(self.graph)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_file.setFont(font)
        self.btn_file.setObjectName(_fromUtf8("btn_file"))
        self.btn_file.clicked.connect(self.get_file)
        self.lbl_file = QtGui.QLabel(self.centralwidget)
        self.lbl_file.setGeometry(QtCore.QRect(180, 300, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_file.setFont(font)
        self.lbl_file.setText(_fromUtf8(""))
        self.lbl_file.setObjectName(_fromUtf8("lbl_file"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 479, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Akıllı Sinyal", None))
        self.label.setText(_translate("MainWindow", "Süre:", None))
        self.btn_analyze.setText(_translate("MainWindow", "Analiz Et", None))
        self.btn_quit.setText(_translate("MainWindow", "Grafik Göster", None))
        self.btn_file.setText(_translate("MainWindow", "Dosya Seç", None))
    def get_file(self):
        self.fileName = QtGui.QFileDialog.getOpenFileName()
        self.lbl_file.setText(self.fileName)
    def graph(self):
        time = self.txt_time.text()
        GraphScript(self.fileName,time)
    def Analiz(self):
        time= self.txt_time.text()
        DetailScript(self.fileName,time)


if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


