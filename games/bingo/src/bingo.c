/*

	title		-> bingo
	description	-> game of bingo
	author		-> h4nk_et0

*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <unistd.h>

#define	MAX_ROWS	5
#define	MAX_COLS	5
#define	MAX_CROSS	2

#include "init.c"
#include "utils.c"

int main()
{
	int loop, in_loop, state = 0, count = 0;
	int box[MAX_ROWS][MAX_COLS];
	int	row[MAX_ROWS] = {0,0,0,0,0},
		column[MAX_COLS] = {0,0,0,0,0},
		cross[MAX_CROSS] = {0,0};
	int *pointer_box[MAX_ROWS][MAX_COLS], *pointer_row[MAX_ROWS], *pointer_column[MAX_COLS], *pointer_cross[MAX_CROSS];

	for(loop = 0;loop < MAX_ROWS;loop++)
		for(in_loop = 0;in_loop < MAX_COLS;in_loop++)
			pointer_box[loop][in_loop] = &box[loop][in_loop];

	for(loop = 0;loop < MAX_ROWS;loop++)
		pointer_row[loop] = &row[loop], pointer_column[loop] = &column[loop];

	for(loop = 0;loop < MAX_CROSS;loop++)
		pointer_cross[loop] = &cross[loop];

	init(pointer_box);

	while(1)
	{
		input(pointer_box);
		display(pointer_box);

		for(loop = 0;loop < 7;loop++)
		{
			state = check(pointer_box,pointer_row,pointer_column,pointer_cross);
			if(state == 1)
			{
				count += 1;
				printf("\n\t\t\t\t\t\t\t");

				for(loop = 0;loop < count;loop++)
					printf("* ");

				switch(count)
				{
					case 1:printf("I N G O\n");
						break;
					case 2:printf("N G O\n");
						break;
					case 3:printf("G O\n");
						break;
					case 4:printf("O\n");
						break;
					default:printf("\n");
				}
			}
		}
		if(count == 5)
			printf("\t\t\t\t\t\t* * * *   BINGO   * * * *\n"), exit(0);
	}
}
