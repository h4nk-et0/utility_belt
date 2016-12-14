
#define DATA_PATH	".utility_belt/bingo/.bingo_data"

void init(int *pointer_box[MAX_ROWS][MAX_COLS])
{
	int position, random, row, column, loop, in_loop;
	int iteration = 1, number = 1, check = 0;
	FILE *data;
	struct stat util_belt = {0};

	for(loop = 0;loop < MAX_ROWS;loop++)
		for(in_loop = 0;in_loop < MAX_COLS;in_loop++)
			*pointer_box[loop][in_loop] = 0;

	if(chdir(getenv("HOME")) == -1)
	{
		perror("can't get HOME ");
		exit(1);
	}

	if(stat(".utility_belt/",&util_belt) == -1)
	{
		if(mkdir(".utility_belt",0755) == -1)
		{
			perror("can't create .utility_belt ");
			exit(1);
		}

		if(mkdir(".utility_belt/bingo/",0755) == -1)
		{
			perror("can't create .utility_belt/bingo/ ");
			exit(1);
		}
	}

	else if(stat(".utility_belt/bingo/",&util_belt) == -1)
	{
		if(mkdir(".utility_belt/bingo/",0755) == -1)
		{
			perror("can't create .utility_belt/bingo/ ");
			exit(1);
		}
	}

	if((data = fopen(DATA_PATH,"rb+")) == NULL)
	{
		if((data = fopen(DATA_PATH,"wb")) == NULL)
		{
			perror("can't open .bingo_data ");
			exit(1);
		}

		printf("enter a random number within 50 : ");
		scanf("%d", &loop);
		fprintf(data,"%d", loop);
	}

	fscanf(data,"%d", &position);
	fseek(data,0,SEEK_SET);

	if(position == 50)
		fprintf(data,"1");
	else
		fprintf(data,"%d",position + 12);

	fclose(data);
	while(1)
	{
		random = rand() % 25;
		if(position > iteration++)
			continue;

		row = random / 5;
		column = random % 5;

		if((*pointer_box[row][column] != 0))
			continue;

		*pointer_box[row][column] = number++;
		if(number == 26)
			break;
	}

	printf("\t\t\t\t\t\t ----------------------------- \n\t\t\t\t\t\t");
	for(loop = 0;loop < MAX_ROWS;loop++)
	{
		for(in_loop = 0;in_loop < MAX_COLS;in_loop++)
		{
			if(*pointer_box[loop][in_loop] > 9)
				printf("|  %d ", *pointer_box[loop][in_loop]);
			else
				printf("|  %d  ", *pointer_box[loop][in_loop]);}

		printf("|\n");
		if(loop == 4)
			continue;
		printf("\t\t\t\t\t\t|-----|-----|-----|-----|-----|\n\t\t\t\t\t\t");
	}

	printf("\t\t\t\t\t\t ----------------------------- \n");
}
