#!/usr/bin/python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import os

# main event called from alert.py

def eventShow(showString) :
	windowframe = windowFrame()
	windowframe.mainwindow.body.setText(showString)
	windowframe.show()
	app.exec_()

# global data

class globalData() :
	def __init__(self) :
		self.showAgain = True

		if sys.platform == "linux" or sys.platform == "linux2" :
			HOME = os.getenv("HOME")
			self.DB_FILE_PATH = os.path.join(HOME, '.config/utility_belt/birthday alert/birthday_db')

			if not os.path.exists(os.path.join(HOME, '.config')) :
				try :
					os.mkdir(os.path.join(HOME, '.config/'))
					os.mkdir(os.path.join(HOME, '.config/utility_belt/'))
					os.mkdir(os.path.join(HOME, '.config/utility_belt/birthday alert'))
				except :
					eventShow('error while creating ' + self.DB_FILE_PATH)
					quit()

				try :
					birthday_db = open(self.DB_FILE_PATH, 'w')

					birthday_db.write('# edit this file with caution. wrong format leads to the program crash.\n')
					birthday_db.close()
				except :
					eventShow('error while creating ' + self.DB_FILE_PATH)

			elif not os.path.exists(os.path.join(HOME, '.config/utility_belt/')) :
				try :
					os.mkdir(os.path.join(HOME, '.config/utility_belt/'))
					os.mkdir(os.path.join(HOME, '.config/utility_belt/birthday alert'))
				except :
					eventShow('error while creating ' + self.DB_FILE_PATH)
					quit()

				try :
					birthday_db = open(self.DB_FILE_PATH, 'w')

					birthday_db.write('# edit this file with caution. wrong format leads to the program crash.\n')
					birthday_db.close()
				except :
					eventShow('error while creating ' + self.DB_FILE_PATH)

			elif not os.path.exists(os.path.join(HOME, '.config/utility_belt/birthday alert')) :
				try :
					os.mkdir(os.path.join(HOME, '.config/utility_belt/birthday alert'))
				except :
					eventShow('error while creating ' + DB_FILE_PATH)
					quit()

				try :
					birthday_db = open(self.DB_FILE_PATH, 'w')

					birthday_db.write('# edit this file with caution. wrong format leads to the program crash.\n')
					birthday_db.close()
				except :
					eventShow('error while creating ' + self.DB_FILE_PATH)

			elif not os.path.exists(self.DB_FILE_PATH) :

				try :
					birthday_db = open(self.DB_FILE_PATH, 'w')

					birthday_db.write('# edit this file with caution. wrong format leads to the program crash.\n')
					birthday_db.close()
				except :
					eventShow('error while creating ' + self.DB_FILE_PATH)

		elif sys.platform == "win32" :
			self.DB_FILE_PATH = "C:\ProgramData\UtilityBelt\BirthdayAlert\\birthday_db"
			self.DB_FILE_PATH = self.DB_FILE_PATH.replace("\\", "/")

			if not os.path.exists("C:\ProgramData") :
				try :
					os.mkdir("C:\ProgramData")
					os.mkdir("C:\ProgramData\UtilityBelt")
					os.mkdir("C:\ProgramData\UtilityBelt\BirthdayAlert")
				except :
					eventShow('error while creating ' + self.DB_FILE_PATH)
					quit()

				try :
					birthday_db = open(self.DB_FILE_PATH, 'w')

					birthday_db.write('# edit this file with caution. wrong format leads to the program crash.\n')
					birthday_db.close()
				except :
					eventShow('error while creating ' + self.DB_FILE_PATH)

			elif not os.path.exists("C:\ProgramData\UtilityBelt") :
				try :
					os.mkdir("C:\ProgramData\UtilityBelt")
					os.mkdir("C:\ProgramData\UtilityBelt\BirthdayAlert")
				except :
					eventShow('error while creating ' + self.DB_FILE_PATH)
					quit()

				try :
					birthday_db = open(self.DB_FILE_PATH, 'w')

					birthday_db.write('# edit this file with caution. wrong format leads to the program crash.\n')
					birthday_db.close()
				except :
					eventShow('error while creating ' + self.DB_FILE_PATH)

			elif not os.path.exists("C:\ProgramData\UtilityBelt\BirthdayAlert") :
				try :
					os.mkdir("C:\ProgramData\UtilityBelt\BirthdayAlert")
				except :
					eventShow('error while creating ' + DB_FILE_PATH)
					quit()

				try :
					birthday_db = open(self.DB_FILE_PATH, 'w')

					birthday_db.write('# edit this file with caution. wrong format leads to the program crash.\n')
					birthday_db.close()
				except :
					eventShow('error while creating ' + self.DB_FILE_PATH)

			elif not os.path.exists(self.DB_FILE_PATH) :

				try :
					birthday_db = open(self.DB_FILE_PATH, 'w')

					birthday_db.write('# edit this file with caution. wrong format leads to the program crash.\n')
					birthday_db.close()
				except :
					eventShow('error while creating' + self.DB_FILE_PATH)
			
# widget for adding new birthdays

class addWindow(QDialog) :
	def __init__(self, parent = None) :
		super(addWindow, self).__init__(parent)

		style_css = """

		QPushButton {
			background: #9F440D;
			font-family: Monospace;
			font-size: 13px;
			font-weight: bold;
			color: #000000;
			outline: 0;
			border-radius: 6px;
			padding: 5px;
			height: 15px;
			width: 60px;
		}

		QPushButton:pressed, QPushButton:hover, QPushButton:selected {
			background: #603108;
			font-family: Monospace;
			font-size: 15px;
			font-weight: bold;
			color: #000000;
			outline:0;
			border-radius: 0px;
			padding: 0px;
			height: 15px;
			width: 60px;
		} """

		self.setWindowTitle('add new alert')

		self.nameBox = QLineEdit('enter the name')
		self.nameBox.selectAll()

		self.monthBox = QComboBox()
		self.monthBox.insertItems(0, map(str, range(1, 13)))

		self.dateBox = QComboBox()
		self.dateBox.insertItems(0, map(str, range(1, 32)))

		self.namelabel = QLabel('name :')
		self.namelabel.setBuddy(self.nameBox)
		self.datelabel = QLabel('date :')
		self.datelabel.setBuddy(self.dateBox)
		self.monthlabel = QLabel('month :')
		self.monthlabel.setBuddy(self.monthBox)

		self.add = QPushButton('&add')
		self.add.setStyleSheet(style_css)
		self.cancel = QPushButton('&cancel')
		self.cancel.setStyleSheet(style_css)

		self.buttonlayout = QHBoxLayout()
		self.buttonlayout.addStretch(1)
		self.buttonlayout.addWidget(self.add)
		self.buttonlayout.addWidget(self.cancel)
		self.buttonlayout.setMargin(20)
		self.buttonlayout.setSpacing(8)

		self.layout = QGridLayout(self)
		self.layout.addWidget(self.namelabel, 0, 0)
		self.layout.addWidget(self.nameBox, 0, 1, 1, 3)
		self.layout.addWidget(self.monthlabel, 1, 0)
		self.layout.addWidget(self.monthBox, 1, 1)
		self.layout.addWidget(self.datelabel, 1, 2)
		self.layout.addWidget(self.dateBox, 1, 3)
		self.layout.addLayout(self.buttonlayout, 3, 0, 1, 4)

		self.connect(self.monthBox, SIGNAL("currentIndexChanged(int)"), self.setDateBox)

	def setDateBox(self) :
		month = self.monthBox.currentIndex() + 1

		if month == 2 :
			self.dateBox.clear()
			self.dateBox.insertItems(0, map(str, range(1, 30)))

		elif month not in [1, 3, 5, 7, 8, 10, 12] :
			self.dateBox.clear()
			self.dateBox.insertItems(0, map(str, range(1, 31)))

# widget for showing all birthdays

class allBdays(QDialog) :
	def __init__(self, parent = None) :
		super(allBdays, self).__init__(parent)

		style_css = """

		QTextBrowser {
			color: #F79E05;
			font-family: Monospace;
			font-size: 13px;
			font-weight: bold;
		}"""

		self.showText = QTextBrowser()
		self.showText.setStyleSheet(style_css)
		self.layout = QHBoxLayout(self)
		self.layout.addWidget(self.showText)

# widget for windows title

class windowTitle(QDialog) :
	def __init__(self, parent = None) :
		super(windowTitle, self).__init__(parent)

		style_css = """
		QLabel {
			color: grey;
			font: Monospace;
			font-size: 13px;
			font-weight: bold;
		}

		QDialog {
			background: #1E140F;
		} """

		self.titleText = QLabel('Birthday Alert')
		self.titleText.setStyleSheet(style_css)
		self.layout = QHBoxLayout(self)
		self.layout.addStretch(1)
		self.layout.addWidget(self.titleText)
		self.layout.addStretch(1)
		self.layout.setSpacing(0)
		self.layout.setMargin(3)

		self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
		self.setStyleSheet(style_css)

# side frame widget

class sideFrame(QDialog) :
	def __init__(self, parent = None) :
		super(sideFrame, self).__init__(parent)

		style_css = """
		QDialog {
			background: #9F440D;
		} """

		self.layout = QHBoxLayout(self)
		self.layout.setMargin(7)

		self.setStyleSheet(style_css)

# main window consisting windowTitle and sideFrame

class mainWindow(QDialog) :
	def __init__(self, parent = None) :
		super(mainWindow, self).__init__(parent)

		try :
			image_path = sys._MEIPASS
			image_path = os.path.join(image_path, 'background.png')
		except :
			image_path = os.path.realpath(__file__)
			image_path = image_path[:image_path.find("graphics.py")] + "background.png"
			if sys.platform == "win32" :
				image_path = image_path.replace('\\', "/")

		style_css = """

		QLabel {
			color: #F79E05;
			font-family: Monospace;
			font-size: 17px;
			font-weight: bold;
		}

		QTableView {
			color: #F79E05;
			outline:0;
			font-family: Monospace;
			font-size: 12px;
			font-weight: bold;
		}

		QPushButton {
			background: #9F440D;
			font-family: Monospace;
			font-size: 13px;
			font-weight: bold;
			color: #000000;
			outline: 0;
			border-radius: 6px;
			padding-top: 10px;
			padding-bottom: 10px;
			padding-left: 5px;
			padding-right: 5px;
			height: 15px;
			width: 60px;
		}

		QPushButton:pressed, QPushButton:hover, QPushButton:selected {
			background: #603108;
			font-family: Monospace;
			font-size: 15px;
			font-weight: bold;
			color: grey;
			outline:0;
			border-radius: 0px;
			padding: 0px;
			height: 15px;
			width: 60px;
		}

		QDialog {
			background: #0BF4AB;
			background-image: url(""" + image_path + """);
		}

		QCheckBox {
			color: #F79E05;
			font-family: Monospace;
			font-weight: bold;
			background: #302210;
		}

		QCheckBox:hover {
			color: none;
			background: none;
		} """

		self.body = QLabel()
		self.body.setStyleSheet(style_css)

		self.checkAgain = QCheckBox("&Don't show this again today")
		self.checkAgain.setObjectName('check')
		self.checkAgain.setStyleSheet(style_css)
		self.checkAgain.setChecked(False)

		self.gotit = QPushButton('&Got It')
		self.gotit.setStyleSheet(style_css)
		self.gotit.setShortcut("space")

		self.add_new = QPushButton('&Add new')
		self.add_new.setStyleSheet(style_css)

		self.show_all = QPushButton('&Show all')
		self.show_all.setStyleSheet(style_css)

		self.body_layout = QHBoxLayout()
		self.body_layout.addStretch(1)
		self.body_layout.addWidget(self.body)
		self.body_layout.addStretch(1)
		self.body_layout.addStretch(1)
		self.body_layout.setMargin(0)
		self.body_layout.setSpacing(0)

		self.checkBox_layout = QHBoxLayout()
		self.checkBox_layout.addStretch(1)
		self.checkBox_layout.addWidget(self.checkAgain)
		self.checkBox_layout.setMargin(12)
		self.checkBox_layout.setSpacing(0)

		self.button_layout = QHBoxLayout()
		self.button_layout.addStretch(1)
		self.button_layout.addWidget(self.show_all)
		self.button_layout.addWidget(self.add_new)
		self.button_layout.addWidget(self.gotit)
		self.button_layout.setMargin(0)
		self.button_layout.setSpacing(8)

		self.layout = QVBoxLayout()
		self.layout.addLayout(self.body_layout)
		self.layout.addLayout(self.checkBox_layout)
		self.layout.addLayout(self.button_layout)
		self.layout.setMargin(0)
		self.layout.setSpacing(0)

		self.setLayout(self.layout)
		self.setStyleSheet(style_css)

# main frame hosting all the widgets

class windowFrame(QFrame) :
	def __init__(self, parent = None) :
		super(windowFrame, self).__init__(parent)

		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setFrameShadow(QFrame.Sunken)

		self.windowtitle = windowTitle()
		self.sideframe = sideFrame()
		self.mainwindow = mainWindow()

		self.vlayout = QVBoxLayout()
		self.vlayout.addWidget(self.windowtitle)
		self.vlayout.addWidget(self.mainwindow)
		self.vlayout.setMargin(0)
		self.vlayout.setSpacing(0)

		self.layout = QHBoxLayout()
		self.layout.addWidget(self.sideframe)
		self.layout.addLayout(self.vlayout)
		self.layout.setMargin(0)
		self.layout.setSpacing(0)

		self.setLayout(self.layout)
		self.resize(QDesktopWidget().screenGeometry().width(), 180)
		self.move(0, (QDesktopWidget().screenGeometry().height() / 2) - 90)

		self.connect(self.mainwindow.gotit, SIGNAL('clicked()'), app.exit)
		self.connect(self.mainwindow.add_new, SIGNAL('clicked()'), self.addNew)
		self.connect(self.mainwindow.show_all, SIGNAL('clicked()'), self.showAll)
		self.connect(self.mainwindow.checkAgain, SIGNAL('toggled(bool)'), self.updateShow)

	def updateShow(self) :
		if self.mainwindow.checkAgain.isChecked() :
			globaldata.showAgain = False
		else :
			globaldata.showAgain = True

	def showAll(self) :
		self.allbdays = allBdays()
		self.allbdays.show()

		try :
			db_file = open(globaldata.DB_FILE_PATH, 'r+')
			db_file.seek(0, 0)
		except :
			self.allbdays.hide()
			self.mainwindow.body.setText('cannot open ' + globaldata.DB_FILE_PATH)
			return

		try :
			file_data = db_file.readlines()
			db_file.close()
		except :
			self.allbdays.hide()
			self.mainwindow.body.setText('cannot read from ' + globaldata.DB_FILE_PATH)
			return

		for data in file_data :
			if data[0] == '#' :
				continue
			elif data.strip() == '' :
				continue

			try :
				data = data.strip()
				data = [data[:data.rfind('\t')].strip(), map(int, data[data.rfind('\t'):].strip().split('-'))]
				if len(data[0]) > 9 :
					self.allbdays.showText.append("%s\t%02d-%02d"%(data[0], data[1][0], data[1][1]))
				else :
					self.allbdays.showText.append("%s\t\t%02d-%02d"%(data[0], data[1][0], data[1][1]))
			except :
				self.allbdays.hide()
				self.mainwindow.body.setText('invalid table in ' + globaldata.DB_FILE_PATH)
				return

	def addNew(self) :
		self.addwindow = addWindow(self)

		self.addwindow.connect(self.addwindow.cancel, SIGNAL('clicked()'), self.addwindow.hide)
		self.addwindow.connect(self.addwindow.add, SIGNAL('clicked()'), self.addNewAdd)
		self.addwindow.show()

	def addNewAdd(self) :
		self.name = self.addwindow.nameBox.text()
		self.date = self.addwindow.dateBox.currentIndex() + 1
		self.month = self.addwindow.monthBox.currentIndex() + 1

		self.addwindow.hide()

		try :
			db_file = open(globaldata.DB_FILE_PATH, 'r+')

			if sys.platform == "win32" :
				db_file.seek(0, 2)		# windows gives error on negative offset
			else :
				db_file.seek(-1, 2)

			if db_file.read() == '\n' :
				writeData = str()
			else :
				writeData = '\n'
		except :
			self.mainwindow.body.setText('cannot open ' + globaldata.DB_FILE_PATH)
			quit()

		if len(self.name) >= 8 :
			writeData += self.name + '\t'
		else :
			writeData += self.name + '\t\t'

		db_file.write("%s%02d-%02d\n" %(writeData, self.date, self.month))
		db_file.close()
		text = 	self.mainwindow.body.text()
		text += "\nname: %s is added to the list" %(self.name)
		self.mainwindow.body.setText(text)

app = QApplication(sys.argv)
globaldata = globalData()

