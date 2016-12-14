#!/usr/bin/python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import socket
import os

# window title widget

class windowTitle(QDialog) :
	def __init__(self, parent = None) :
		super(windowTitle,self).__init__(parent)

		style_css = """
		QLabel {
			color: grey;
			font: Monospace;
			font-size: 14px;
			font-weight: bold;
		}

		QDialog {
			background: #1E140F;
		} """

		self.statusTitle = QLabel('Battery Status')
		self.statusTitle.setStyleSheet(style_css)
		self.infoTitle = QLabel('Battery Info')
		self.infoTitle.setStyleSheet(style_css)

		self.layout = QHBoxLayout(self)
		self.layout.addStretch(1)
		self.layout.addWidget(self.statusTitle)
		self.layout.addStretch(1)
		self.layout.addWidget(self.infoTitle)
		self.layout.addStretch(1)
		self.layout.setSpacing(0)
		self.layout.setMargin(6)

		self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
		self.setStyleSheet(style_css)

# side frame widget

class sideFrame(QDialog) :
	def __init__(self, parent = None) :
		super(sideFrame,self).__init__(parent)

		style_css = """
		QDialog {
			background: #9F440D;
		} """

		self.layout = QHBoxLayout(self)
		self.layout.setMargin(7)

		self.setStyleSheet(style_css)

# main window consisting battery status and battery info widget

class mainWindow(QDialog) :
	def __init__(self, parent = None) :
		super(mainWindow,self).__init__(parent)

		self.uevent = dict()

		image_path = os.path.realpath(__file__)
		image_path = image_path[:image_path.find("graphics.py")] + "background.png"
		style_css = """
		#batteryStatus {
			color: #F79E05;
			font-family: Monospace;
			font-size: 14px;
			font-weight: bold;
		}

		#batteryInfo {
			color: #F79E05;
			font-family: Monospace;
			font-size: 14px;
			font-weight: bold;
		}

		QPushButton {
			background: #9F440D;
			font-family: Monospace;
			font-size: 14px;
			font-weight: bold;
			color: #000000;
			outline:0;
			border-radius: 6px;
			padding: 10px;
		}

		QPushButton:pressed {
			background: #603108;
			font-family: Monospace;
			font-size: 14px;
			font-weight: bold;
			color: #000000;
			outline:0;
			border-radius: 0px;
			padding: 10px;
		}

		QPushButton:hover {
			background: #603108;
			font-family: Monospace;
			font-size: 14px;
			font-weight: bold;
			color: #000000;
			outline:0;
			border-radius: 0px;
			padding: 10px;
		}

		QDialog {
			background: #0BF4AB;
			background-image: url(""" + image_path + """);
		} """

		self.batteryStatus = QLabel()
		self.batteryStatus.setObjectName('batteryStatus')
		self.batteryStatus.setStyleSheet(style_css)
		self.batteryInfo = QLabel()
		self.batteryInfo.setObjectName('batteryInfo')
		self.batteryInfo.setStyleSheet(style_css)

		self.gotit = QPushButton('&Got It')
		self.gotit.setStyleSheet(style_css)

		self.hlayout = QHBoxLayout()
		self.hlayout.addStretch(1)
		self.hlayout.addWidget(self.gotit)
		self.hlayout.setMargin(0)
		self.hlayout.setSpacing(0)

		self.vlayout = QVBoxLayout()
		self.vlayout.addStretch(1)
		self.vlayout.addLayout(self.hlayout)

		self.layout = QHBoxLayout()
		self.layout.addStretch(1)
		self.layout.addWidget(self.batteryStatus)
		self.layout.addStretch(1)
		self.layout.addWidget(self.batteryInfo)
		self.layout.addStretch(1)
		self.layout.addLayout(self.vlayout)

		self.setLayout(self.layout)
		self.setStyleSheet(style_css)
		self.connect(self.gotit,SIGNAL('clicked()'),app.exit)

	# method for updating the text in the content window

	def updateValues(self, uevent, msg) :
		self.batteryStatus.setText('<font size = 4>Battery is at ' + uevent.values['POWER_SUPPLY_CAPACITY'] + '%</font><br /><br />' + msg)
		self.batteryInfo.setText('<pre>Technology   : ' + uevent.values['POWER_SUPPLY_TECHNOLOGY'] + '<br />'
						'Current      : ' + uevent.values['POWER_SUPPLY_CAPACITY'] + '%<br />'
						'Model Name   : ' + uevent.values['POWER_SUPPLY_MODEL_NAME'] + '<br />'
						'Manufacturer : ' + uevent.values['POWER_SUPPLY_MANUFACTURER'] + '<br />'
						'Serial No    : ' + uevent.values['POWER_SUPPLY_SERIAL_NUMBER'] + '</pre>')

# main frame hosting all the widgets

class windowFrame(QFrame) :
	def __init__(self, parent = None) :
		super(windowFrame,self).__init__(parent)

		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.setFrameShadow(QFrame.Sunken)

		# start acpi read thread

		self.acpidread = acpidRead()
		self.acpidread.start()

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
		self.resize(QDesktopWidget().screenGeometry().width(),180)
		self.connect(self.acpidread, SIGNAL("plugged-in"),app.exit)
		self.connect(self.acpidread, SIGNAL("unplugged"),app.exit)

# class for acpi event data structure

class acpidEvent() :
	def __init__(self) :
		self.cls = "ac_adapter"
		self.device = "ACPI0003:00"
		self.code = '00000080'
		self.status = '00000000'

# thread for adapter status

class acpidRead(QThread) :
	def __init__(self) :
		super(acpidRead,self).__init__()
		self.signal_plugged = SIGNAL("plugged-in")
		self.signal_unplugged = SIGNAL("unplugged")

	def run(self) :
		self.acpid_socket = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
		self.acpid_socket.connect(ACPID_FILE)

		while True :
			data = self.acpid_socket.recv(4096).strip()

			if data[:data.find(' ')] == 'ac_adapter' :
				acpid_event.cls, acpid_event.device, acpid_event.code, acpid_event.status = data.split(' ')

				if acpid_event.status == acpid_adapter_on.status :
					self.emit(self.signal_plugged, '')
					break

				elif acpid_event.status == acpid_adapter_off.status :
					self.emit(self.signal_unplugged, '')
					break

		self.acpid_socket.close()

# initiate the application and acpi event objects

ACPID_FILE = '/var/run/acpid.socket'
app = QApplication(sys.argv)
acpid_adapter_on = acpidEvent()
acpid_adapter_off = acpidEvent()
acpid_event = acpidEvent()

# function called in the monitor.py file

def showWindow(uevent, msg) :
	windowframe = windowFrame()
	windowframe.mainwindow.updateValues(uevent, msg)
	windowframe.show()
	app.exec_()
