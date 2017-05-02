#!/usr/bin/python


#
#	title		-> birthday alert
#	description	-> creates an alert on the birthdays
#	author		-> h4nk_et0
#

import time
from utils.utils import *

def help() :
	print \
"""Usage: alert.py [options]

OPTIONS :

	-h or --help\t\t\t- show this help
	-a or -s or --add or --show\t- add a new event to the list or show the event dialog
"""

if len(sys.argv) == 2 :
	if sys.argv[1] in ['-h', '--help'] :
		help()
		quit()

	elif sys.argv[1] in ['-a', '-s', '--add', '--show'] :
		fileData = readFile()
		events = eventCheck(fileData)

		if events != [] :
			for event in events :
				showData = '\nToday is ' + event[0] + "'s birthday." + '\nDate: ' + "%02d" %(event[1][0]) + '-' + "%02d\n" %(event[1][1])
				eventShow(showData)
				time.sleep(2)
		else :
			eventShow("\nThere are no events today ...\nIf you wish to add a new event click 'add new'\n")

		quit()

	else :
		print 'invalid argument'
		help()
		quit()

elif len(sys.argv) > 2 :
	help()
	quit()


while True :
	noEvent = False
	currentDate = QDate.currentDate()
	fileData = readFile()
	events = eventCheck(fileData)

	if events != [] :
		for event in events :
			showData = '\nToday is ' + event[0] + "'s birthday." + '\nDate: ' + "%02d" %(event[1][0]) + '-' + "%02d\n" %(event[1][1])
			eventShow(showData)
			time.sleep(2)

	elif events == [] :
		noEvent = True

	if (not globaldata.showAgain) or noEvent :
		while True :
			if currentDate != QDate.currentDate() :
				globaldata.showAgain = True
				break
			time.sleep(3600)

	elif globaldata.showAgain :
		time.sleep(1800)

