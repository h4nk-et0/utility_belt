
void player1_move()
{
	int x,y;

	printf("\x1b[31m");
	printf("player 1 turn: ");
	scanf("%d%*c%d",&x,&y);
	x--, y--;

	if(game[x][y] != ' ')
	{
		printf("invalid move try again\n");
		player1_move();
	}
	else
		game[x][y] = 'X';
}

void player2_move()
{
	int x,y;

	printf("\x1b[30m"); 
	printf("player 2 turn: ");
	scanf("%d%*c%d",&x,&y);
	x--, y--;

	if(game[x][y] != ' ')
	{
		printf("invalid move try again\n");
		player2_move();
	}
	else
		game[x][y] = 'O';
}
