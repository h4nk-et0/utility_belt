#!/usr/bin/python

from graphics import *

class eventData() :
	def __init__() :
		self.name = str()
		self.date = int()
		self.month = int()

def readFile():
	try :
		db_file = open(globaldata.DB_FILE_PATH,'r')
	except :
		eventShow('cannot open ' + globaldata.DB_FILE_PATH)
		quit()

	try :
		file_data = db_file.readlines()
		db_file.close()
	except :
		eventShow('cannot read from ' + globaldata.DB_FILE_PATH)
		quit()

	fileData = list()
	for data in file_data :
		if data[0] == '#' :
			continue
		elif data.strip() == '' :
			continue

		try :
			data = data.strip()
			data = [data[:data.rfind('\t')].strip(),map(int,data[data.rfind('\t'):].strip().split('-'))]
			fileData.append(data)
		except :
			eventShow('invalid table in ' + globaldata.DB_FILE_PATH)
			quit()

	return fileData

def eventCheck(fileData) :
	events = list()

	if fileData == [] :
		eventShow('There are no birthdays in the file.\nYou can add by clicking "add new" button.')

	for data in fileData :
		name = data[0]
		day = data[1][0]
		month = data[1][1]
		currentDay = QDate.currentDate().day()
		currentMonth = QDate.currentDate().month()

		if currentDay == day and currentMonth == month :
			events.append(data)

	return events
