
int check(int *pointer_box[MAX_ROWS][MAX_COLS],int *pointer_row[MAX_ROWS],int *pointer_column[MAX_COLS],int *pointer_cross[MAX_CROSS])
{
	int row, column, loop;

	for(row = 0;row < MAX_ROWS;row++)
	{
		if(*pointer_row[row] == 1)
			continue;

		for(column = 1;column < MAX_COLS;column++)
			if(*pointer_box[row][0] != *pointer_box[row][column])
				break;

		if(column == 5)
		{
			*pointer_row[row] = 1;
			return 1;
		}
	}

	for(column = 0;column < MAX_COLS;column++)
	{
		if(*pointer_column[column] == 1)
			continue;
		for(row = 1;row < MAX_ROWS;row++)
			if(*pointer_box[0][column] != *pointer_box[row][column])
				break;
		if(row == 5)
		{
			*pointer_column[column] = 1;
			return 1;
		}
	}

	if(*pointer_cross[0] != 1)
	{
		for(row = 0;row < MAX_ROWS;row++)
			if(*pointer_box[row][row] != 0)
				break;

		if(row == 5)
		{
			*pointer_cross[0] = 1;
			return 1;
		}
	}

	if(*pointer_cross[1] != 1)
	{
		for(row = 0;row < MAX_ROWS;row++)
		{
			if(*pointer_box[row][4 - row] != 0)
				break;
			if(row == 4)
			{
				*pointer_cross[1] = 1;
				return 1;
			}
		}
	}

	return 0;
}


void display(int *pointer_box[MAX_ROWS][MAX_COLS])
{
	int row, column;

	printf("\t\t\t\t\t\t ----------------------------- \n\t\t\t\t\t\t");
	for(row = 0;row < MAX_ROWS;row++)
	{
		for(column = 0;column < MAX_COLS;column++)
		{
			if(*pointer_box[row][column] > 9)
				printf("|  %d ", *pointer_box[row][column]);
			else if(*pointer_box[row][column] == 0)
			{
				printf("|");
				printf("\x1b[31m");
				printf("  *  ");
				printf("\x1b[0m");
			}
			else
				printf("|  %d  ", *pointer_box[row][column]);
		}

		printf("|\n");
		if(row == 4)
			continue;

		printf("\t\t\t\t\t\t|-----|-----|-----|-----|-----|\n\t\t\t\t\t\t");
	}

	printf("\t\t\t\t\t\t ----------------------------- \n");
}


void input(int *pointer_box[MAX_ROWS][MAX_COLS])
{
	int number, loop, in_loop, check=0;

	while(1)
	{
		while(1)
		{
			printf("\nenter the number : ");
			scanf("%d",&number);

			if((number < 26) && (number != 0))
				break;
			printf("invalid number\ntry again\n");
		}

		for(loop = 0;loop < MAX_ROWS;loop++)
			for(in_loop = 0;in_loop < MAX_COLS;in_loop++)
				if(number == (*pointer_box[loop][in_loop]))
					*pointer_box[loop][in_loop] = 0, check = 1;
		if(check == 1)
			break;
		printf("already filled\ntry again\n");
	}
}
