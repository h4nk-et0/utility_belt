#!/usr/bin/python


#
#	title		-> battery monitor
#	description	-> monitors the battery and warns the user
#	author		-> h4nk_et0
#

import time
from graphics.graphics import *

# class for uevent file data structure

class ueventPowerSupply() :
	def __init__(self) :
		self.values = dict()

	def read_file(self) :
		self.values.clear()

		battery_file = open(BATTERY_FILE,'r')

		data = battery_file.read().strip().split('\n')
		battery_file.close()

		for count in range(15) :
			key,value = data[count].split('=')
			self.values[key] = value

# file location of the uevent file

BATTERY_FILE = '/sys/class/power_supply/BAT'

for num in range(0,10) :


	if os.path.exists(BATTERY_FILE + str(num) + '/uevent') :
		BATTERY_FILE += str(num) + '/uevent'
		break
else :
	sys.exit(1)

# initiate all the objects

uevent = ueventPowerSupply()
acpid_adapter_on.status = '00000001'

# main loop which checks the battery level

while True :

	uevent.read_file()
	if int(uevent.values['POWER_SUPPLY_CAPACITY']) <=15 and uevent.values['POWER_SUPPLY_STATUS'] == 'Discharging' :
		msg = 'You might want to plug-in the adapter'
		showWindow(uevent, msg)

	elif int(uevent.values['POWER_SUPPLY_CAPACITY']) >= 95 and uevent.values['POWER_SUPPLY_STATUS'] == 'Charging' :
		msg = '<font color = green>You might want to unplug the adapter</font>'
		showWindow(uevent, msg)

	elif int(uevent.values['POWER_SUPPLY_CAPACITY']) < 10 and uevent.values['POWER_SUPPLY_STATUS'] == 'Discharging' :
		msg = '<font color = red>Battery at critical level<br />plug-in the adapter or shutdown the system now!</font>'
		showWindow(uevent, msg)

	elif int(uevent.values['POWER_SUPPLY_CAPACITY']) >= 98 and uevent.values['POWER_SUPPLY_STATUS'] == 'Charging' :
		msg = 'Battery charged. Unplug the adapter'
		showWindow(uevent, msg)

	elif int(uevent.values['POWER_SUPPLY_CAPACITY']) == 100 and uevent.values['POWER_SUPPLY_STATUS'] == 'Charging' :
		msg = '<font color = red>Battery overcharging.<br />Unplug the adapter now!</font>'
		showWindow(uevent, msg)

	time.sleep(200)
