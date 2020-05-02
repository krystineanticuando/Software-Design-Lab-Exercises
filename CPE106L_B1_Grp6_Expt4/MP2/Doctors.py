"""
Samuel Imperial
Group03
GUI version of Doctor class
"""

from PyQt4 import QtCore, QtGui
import random
import os.path
from os import path

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

class Ui_Doctor(object):
	
	history = []
	hedges = ("Please tell me more.","Many of my patients tell me the same thing.","Please coninue.")
	qualifiers = ("Why do you say that ",
                  "You seem to think that ",
                  "Can you explain why ")
	replacements = {"I": "you", "me": "you", "my": "your",
                    "we": "you", "us": "you", "mine": "yours",
                    "you": "I", "your": "my", "yours": "mine", "am" : "are",
							"i": "you"}

	def __init__(self, patientn):
		self.patientn = patientn

	def reply(self):
		self.patientn = open(self.searchpatient.text(), "a")
		probability = random.randint(1, 5)
		if probability in (1, 2):
			answer = random.choice(Ui_Doctor.hedges)
		elif probability == 3 and len(Ui_Doctor.history) > 3:
			answer = "Earlier you said that " + \
				self.changePerson(random.choice(Ui_Doctor.history))
		else:
			answer = random.choice(Ui_Doctor.qualifiers) + \
				self.changePerson(self.replyyou.text())
		Ui_Doctor.history.append(self.replyyou.text())
		self.patientn.write(self.replyyou.text())
		self.patientn.close()
		textread = open(self.searchpatient.text(), "r+")
		self.history.setPlainText(textread.read())
		self.doc.setText(answer)
		if self.replyyou.text() == "bye" or self.replyyou.text() == "Bye":
			self.doc.setText("Have a nice day!")
		self.replyyou.clear()

	def changePerson(self, sentence):
		words = sentence.split()
		replyWords = []
		for word in words:
			replyWords.append(Ui_Doctor.replacements.get(word, word))
		return " ".join(replyWords)

	def searchpatientname(self):
		if path.exists(self.searchpatient.text()):
			self.patientn = open(self.searchpatient.text(), "a")
			self.nopatient.setText("Patient found!")
		else:
			self.nopatient.setText("Patient does not exist!")
			self.createpatient.setText("Create new patient?")
			self.yess.show()
			self.noo.show()

	def createnewpatient(self):
		self.patientn = open(self.searchpatient.text(), "w+")
		self.nopatient.setText("")
		self.createpatient.setText("Created successfuly!")
		self.yess.hide()
		self.noo.hide()

	def dontcreate(self):
		self.nopatient.setText("")
		self.createpatient.setText("")
		self.yess.hide()
		self.noo.hide()

	def setupUi(self, Doctor):
		Doctor.setObjectName(_fromUtf8("Doctor"))
		Doctor.resize(489, 410)
		self.centralwidget = QtGui.QWidget(Doctor)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.label_2 = QtGui.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(30, 30, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_2.setFont(font)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.searchpatient = QtGui.QLineEdit(self.centralwidget)
		self.searchpatient.setGeometry(QtCore.QRect(170, 32, 211, 31))
		self.searchpatient.setObjectName(_fromUtf8("searchpatient"))
		self.searchbtn = QtGui.QPushButton(self.centralwidget)
		self.searchbtn.setGeometry(QtCore.QRect(390, 30, 71, 31))
		self.searchbtn.setObjectName(_fromUtf8("searchbtn"))
		self.nopatient = QtGui.QLabel(self.centralwidget)
		self.nopatient.setGeometry(QtCore.QRect(170, 0, 211, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setItalic(True)
		self.nopatient.setFont(font)
		self.nopatient.setAlignment(QtCore.Qt.AlignCenter)
		self.nopatient.setObjectName(_fromUtf8("nopatient"))
		self.createpatient = QtGui.QLabel(self.centralwidget)
		self.createpatient.setGeometry(QtCore.QRect(170, 70, 211, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setItalic(True)
		self.createpatient.setFont(font)
		self.createpatient.setAlignment(QtCore.Qt.AlignCenter)
		self.createpatient.setObjectName(_fromUtf8("createpatient"))
		self.yess = QtGui.QPushButton(self.centralwidget)
		self.yess.setGeometry(QtCore.QRect(380, 70, 41, 31))
		self.yess.setObjectName(_fromUtf8("yess"))
		self.yess.hide()
		self.noo = QtGui.QPushButton(self.centralwidget)
		self.noo.setGeometry(QtCore.QRect(420, 70, 41, 31))
		self.noo.setObjectName(_fromUtf8("noo"))
		self.noo.hide()
		self.label_3 = QtGui.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(30, 110, 71, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_3.setFont(font)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.doc = QtGui.QLabel(self.centralwidget)
		self.doc.setGeometry(QtCore.QRect(100, 110, 381, 31))
		font = QtGui.QFont()
		font.setPointSize(13)
		self.doc.setFont(font)
		self.doc.setObjectName(_fromUtf8("doc"))
		self.label_4 = QtGui.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(30, 150, 71, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_4.setFont(font)
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.replyyou = QtGui.QLineEdit(self.centralwidget)
		self.replyyou.setGeometry(QtCore.QRect(100, 150, 361, 31))
		self.replyyou.setObjectName(_fromUtf8("replyyou"))
		self.label_5 = QtGui.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(30, 190, 151, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_5.setFont(font)
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.history = QtGui.QPlainTextEdit(self.centralwidget)
		self.history.setGeometry(QtCore.QRect(30, 220, 261, 131))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setItalic(True)
		self.history.setFont(font)
		self.history.setObjectName(_fromUtf8("history"))
		Doctor.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(Doctor)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 25))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		Doctor.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(Doctor)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		Doctor.setStatusBar(self.statusbar)

		self.retranslateUi(Doctor)
		QtCore.QObject.connect(self.searchbtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchpatientname)
		QtCore.QObject.connect(self.yess, QtCore.SIGNAL(_fromUtf8("clicked()")), self.createnewpatient)
		QtCore.QObject.connect(self.noo, QtCore.SIGNAL(_fromUtf8("clicked()")), self.dontcreate)
		QtCore.QObject.connect(self.replyyou, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.reply)
		QtCore.QMetaObject.connectSlotsByName(Doctor)

	def retranslateUi(self, Doctor):
		Doctor.setWindowTitle(_translate("Doctor", "Doctors", None))
		self.label_2.setText(_translate("Doctor", "Patient\'s name:", None))
		self.searchbtn.setText(_translate("Doctor", "Search", None))
		self.nopatient.setText(_translate("Doctor", ".", None))
		self.createpatient.setText(_translate("Doctor", ".", None))
		self.yess.setText(_translate("Doctor", "yes", None))
		self.noo.setText(_translate("Doctor", "no", None))
		self.label_3.setText(_translate("Doctor", "Doctor:", None))
		self.doc.setText(_translate("Doctor", "Good morning, I hope you are well today", None))
		self.label_4.setText(_translate("Doctor", "You:", None))
		self.label_5.setText(_translate("Doctor", "Patient\'s history: ", None))


if __name__ == "__main__":
	import sys
	patient = open("dump", "w")
	app = QtGui.QApplication(sys.argv)
	Doctor = QtGui.QMainWindow()
	ui = Ui_Doctor(patient)
	ui.setupUi(Doctor)
	Doctor.show()
	sys.exit(app.exec_())

