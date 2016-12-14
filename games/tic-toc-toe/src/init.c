void init()
{
	int loop, in_loop;

	for(loop = 0;loop < MAX_ROWS;loop++)
		for(in_loop = 0;in_loop < MAX_COLS;in_loop++)
			game[loop][in_loop]=' ';
}
