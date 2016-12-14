This is a keylogger which captures important keys and stores it into a log file.

Platform :
==========

	This keylogger works only on linux


Installing :
============

	run "make" in a terminal to build a binary executable and run the binary executable to start the keylogger


Description :
=============

	When the binary executable is run from a terminal,
	it daemonizes(detaches) itself from the terminal
	and runs as a seperate process. If a non-root user
	tries to run the executable, it exits the program
	saying "not enough privileges. run it as root ...".


Files used :
============

	log file	- /var/log/keylog.log
