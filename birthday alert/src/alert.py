#!/usr/bin/python


#
#	title		-> birthday alert
#	description	-> creates an alert on the birthdays
#	author		-> h4nk_et0
#

import time
from utils.utils import *

while True :
	noEvent = False
	currentDate = QDate.currentDate()
	fileData = readFile()
	events = eventCheck(fileData)

	if events != [] :
		for event in events :
			showData = '\nToday is ' + event[0] + "'s birthday." + ' Wish them best!\n' + 'Date: ' + str(event[1][0]) + '-' + str(event[1][1])
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

