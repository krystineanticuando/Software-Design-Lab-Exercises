"""
Samuel II C. Imperial
Group03
GUI version of temperature converter
"""

from PyQt5 import QtCore, QtGui

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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(300, 300)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 40, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.fah = QtGui.QLineEdit(self.centralwidget)
        self.fah.setGeometry(QtCore.QRect(20, 80, 101, 33))
        self.fah.setObjectName(_fromUtf8("fah"))
        self.cel = QtGui.QLineEdit(self.centralwidget)
        self.cel.setGeometry(QtCore.QRect(150, 80, 113, 33))
        self.cel.setObjectName(_fromUtf8("cel"))
        self.ftoc = QtGui.QPushButton(self.centralwidget)
        self.ftoc.setGeometry(QtCore.QRect(90, 130, 98, 31))
        self.ftoc.setObjectName(_fromUtf8("ftoc"))
        self.ctof = QtGui.QPushButton(self.centralwidget)
        self.ctof.setGeometry(QtCore.QRect(90, 170, 98, 31))
        self.ctof.setObjectName(_fromUtf8("ctof"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.ftoc, QtCore.SIGNAL(_fromUtf8("clicked()")), self.fftocc)
        QtCore.QObject.connect(self.ctof, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cctoff)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def fftocc(self):
        cels = (float(self.fah.text()) - 32) * 5/9
        celss = round(cels, 2)
        self.cel.setText(str(celss))

    def cctoff(self):
        fahs = (float(self.cel.text()) * 9/5) + 32
        fahss = round(fahs, 2)
        self.fah.setText(str(fahss))


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Temperature Converter", None))
        self.label.setText(_translate("MainWindow", "Fahrenheit", None))
        self.label_2.setText(_translate("MainWindow", "Celsius", None))
        self.fah.setText(_translate("MainWindow", "32.0", None))
        self.cel.setText(_translate("MainWindow", "0.0", None))
        self.ftoc.setText(_translate("MainWindow", ">>>>", None))
        self.ctof.setText(_translate("MainWindow", "<<<<", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

