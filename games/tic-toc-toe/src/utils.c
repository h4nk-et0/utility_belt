
void again()
{
	char ag;
	int loop;

	printf("\x1b[32m");
	printf("\n\nthis is the game of tic toc toe.\n\n");

	init();
	double_player();

	printf("press enter to play again..........");
	getchar();

	while(1)
	{
		scanf("%c",&ag);
		if(ag = 13)
			break;
	}
	again();
}

void double_player()
{
	char block;

	block=' ';
	do
	{
		display_game();
		player1_move();

		block = check();
		if(block != ' ')
			break;

		block = draw();
		if(block == 'd')
			break;

		display_game();
		player2_move();

		block = check();
		if(block != ' ')
			break;
		block = draw();
		if(block == 'd')
			break;
	}while(block == ' ');

	display_game();
	if(block == 'X')
		printf("\n\n\t\t\t\t********player 1 won********\n\n\n");
	else if(block=='O')
		printf("\n\n\t\t\t\t********player 2 won********\n\n\n");
	else if(block=='d')
		printf("\n\n\t\t\t\t********it's a draw********\n\n\n");
}

void display_game()
{
	int loop;

	for(loop = 0;loop < MAX_ROWS;loop++)
	{
		printf("   \t\t\t\t\t  %c | %c | %c ",game[loop][0],game[loop][1],game[loop][2]);
		if(loop != 2)
			printf("\n\t\t\t\t\t ---|---|---\n");
	}
	printf("\n");
}

char check()
{
	int loop;

	for(loop = 0;loop < MAX_ROWS;loop++)
	{
		if(game[loop][0] == game[loop][1] && game[loop][0] == game[loop][2])
			return game[loop][0];
	}

	for(loop = 0;loop < MAX_COLS;loop++)
	{
		if(game[0][loop] == game[1][loop] && game[0][loop] == game[2][loop])
			return game[0][loop];
	}

	if(game[0][0] == game[1][1] && game[1][1] == game[2][2])
		return game[0][0];

	if(game[0][2] == game[1][1] && game[1][1] == game[2][0])
		return game[0][2];

	return ' ';
}

int draw()
{
	int loop,in_loop = 0;

	for(loop = 0;loop < MAX_ROWS;loop++)
	{
		for(in_loop = 0;in_loop < MAX_COLS;in_loop++)
		{
			if(game[loop][in_loop] == ' ')
				return ' ';
		}
	}
	return 'd';
}
