
It is a battery monitoring software.

Platform :
==========

	Compatible for both windows and linux.

Installation :
==============

	Linux :

		Run the setup.py file. Then run the monitor.py file in the src folder to start the program
		or else run the binary compiled file monitor in the dist folder

	Windows :

		run the monitor.exe file in the dist folder

Description :
=============

	When the program is started, it checks for
	the battery level and status every 200s.
	If it is below some predefined value, then
	the user will be warned through the graphical
	user interface about the battery status.

Features :
==========

	While showing the warning, if the status of
	the adapter is changed (plugged-in or unplugged),
	the program will automatically detect the change
	and closes the window.

	Along with the battery status, it also shows the
	battery model and other information like the model,
	manufacturer etc.
