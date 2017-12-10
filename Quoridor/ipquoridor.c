#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct listnode *Listptr;

struct listnode {
	char color[15];
	char orient[15];
	int line,col,pline,pcol;
	Listptr next;
};

struct player{
	int l;
	int c;
};

void list_commands()
{
	printf("List of all available commands:\n");
	printf("4.1 Adminstrative Commands\n");
	printf(" 4.1.1 name: Name of the engine.\n");
	printf(" 4.1.2 known_command: Shows if entered command is known by the engine.\n");
	printf(" 4.1.3 list_commands: Prints a list of all available commands.\n");
	printf(" 4.1.4 quit: The session is terminated and the connection is closed.\n");
	printf("4.2 Setup Commands\n");
	printf(" 4.2.1 boardsize: The board size is changed.\n");
	printf(" 4.2.2 clear_board: The board is cleared, the two pawns return to start, each player's walls become arbitrary and the move history is reset.\n");
	printf(" 4.2.3 walls: Each player has that number of walls at the begining.\n");
	printf("4.3 Core Play Commands\n");
	printf(" 4.3.1 playmove: The player of the requested color is played at the requested vertex.\n");
	printf(" 4.3.2 playwall: A wall place at the requested vertex and orientation.\n");
	printf(" 4.3.3 genmove: The engine makes a move or wall placement for the requested color.\n");
	printf(" 4.3.4 undo: The game goes one move back.\n");
	printf("4.4 Tournament Commands\n");
	printf(" 4.4.1 winner : Determines the winner\n");
	printf("4.5 Debug Commands\n");
	printf(" 4.5.1 showboard : Prints the board\n");
	printf("=\n\n");
}

void name()
{
	printf("= One Punch Program\n\n");
	fflush(stdout);
}

int winner(int player,int **board,int size)
{
	int j;
	printf("=");
	for(j=0;j<4*size+1;j++){
        	if(board[2*size][j]=='B')
                	player=1;
        	else if(board[1][j]=='W')
        		player=0;
        }
	if(player==0)
		printf(" true white");
	else if(player==1)
		printf(" true black");
	else
		printf(" false");
	printf("\n\n");
	fflush(stdout);
}

int known_command(char * com)
{
	if(!strcmp(com,"name")||!strcmp(com,"list_commands")||!strcmp(com,"known_command")||!strcmp(com,"quit"))
		printf("Correct Administrative Command.\n");
	else if(!strcmp(com,"boardsize")||!strcmp(com,"clear_board")||!strcmp(com,"walls")||!strcmp(com,"showboard"))
		printf("Correct Setup Command.\n");
	else if(!strcmp(com,"playmove")||!strcmp(com,"playwall")||!strcmp(com,"genmove")||!strcmp(com,"undo"))
		printf("Correct Core Play Command.\n");
	else
		printf("Wrong Command.\n");
	printf("=\n\n");
	fflush(stdout);
}

int boardsize(int size,int *** board)
{
		int line,col,i,j;
		(*board)=malloc((2*size+1)*sizeof(int*));
		if ((*board)==NULL)
		{
			printf("Unacceptable size\n");
			return;
		}
		for(i=0;i<2*size+1;i++)
		{
			(*board)[i]=malloc((4*size+1)*sizeof(int));
			if ((*board)[i]==NULL)
			{
		                printf("Unacceptable size\n");
		                return;
		        }
		}
		for(i=0;i<2*size+1;i++){
			for(j=0;j<4*size+1;j++){
				if(j!=4*size+1){
					if(i%2==0 && j%4==0)
						(*board)[i][j]='+';
					else if(i%2==0 && j%4!=0)
						(*board)[i][j]='-';
					else if(i%2==1 && j%4==0)
						(*board)[i][j]='|';
					else if(i%2==1 && j%4!=0)
						(*board)[i][j]=' ';
				}
			}
		}
		(*board)[1][(4*size+1)/2]='B';
		(*board)[2*size-1][(4*size+1)/2]='W';
		printf("=\n\n");
		fflush(stdout);
}

int clearboard(int size, int **board)
{
	int i,j;
	for(i=0;i<2*size+1;i++){
        	for(j=0;j<4*size+1;j++){
                	if(j!=4*size+1){
                                if(i%2==0 && j%4==0)
                                        board[i][j]='+';
                                else if(i%2==0 && j%4!=0)
                                        board[i][j]='-';
                                else if(i%2==1 && j%4==0)
                                        board[i][j]='|';
                                else if(i%2==1 && j%4!=0)
                                        board[i][j]=' ';
                        }
                }
        }
        board[1][(4*size+1)/2]='B';
        board[2*size-1][(4*size+1)/2]='W';
	printf("=\n\n");
	fflush(stdout);
}

int showboard(int ** board,int size,int * wwall,int * bwall)
{
	int i,j,a=65,b=size+1,c=65;
	printf("    ");
	for(j=0;j<4*size+1;j++){
                if(j%4==3)
                {
                        putchar(a++);
                        printf("   ");
                }
        }
        printf("\n");
	for(i=0;i<2*size+1;i++){
		if(i%2==0)
			printf("  ");
        	for(j=0;j<4*size+1;j++){
			if(i%2==1&&j==0)
				printf("%2d",b);
	                putchar(board[i][j]);
			if(i==0 && j==4*size){
				printf("\t\tWhite player walls = %d",*wwall);
			}
			if(i==2 && j==4*size){
				printf("\t\tBlack player walls = %d",*bwall);
			}
                }
		if(i%2==1)
                	printf("%d",b);
		if(i%2==0)
			b--;
                printf("\n");
        }
	printf("    ");
	for(j=0;j<4*size+1;j++){
                if(j%4==3)
                {
                        putchar(c++);
			printf("   ");
                }
        }
	printf("\n=\n\n");
}

int playwall(int size,char * color,int line,int col,int **board,char * orient,int * wwall,int * bwall,Listptr *history)
{
	int i,a,b,j=1;
	if(line>96 && line<123)
                a=line-'a';
        else if(line>64 && line<91)
                a=line-'A';
	b=col-'0';
	if((*wwall)==0 || (*bwall)==0){
		printf("?No more walls\n");
		return 0;
	}
	if(!strcasecmp(orient,"horizontal")||!strcasecmp(orient,"h"))
	{
		for(i=1;i<8;i++){
			if(board[(2*size)-(2*b)][4*a+i] == '=')
				j++;
		}
		for(i=1;i<8;i++){
			if(board[(2*size)-(2*b)][4*a+i] != '=' && j==1){
				board[(2*size)-(2*b)][4*a+i]='=';
			}
			else{
				printf("?Invalid wall placement.\n");
				i=9;
			}
			if(i==7){
				insert_at_start(history,a,b,color,orient,NULL,NULL);
				if(!strcasecmp(color,"W") || !strcasecmp(color,"WHITE")){
                                        (*wwall)--;
                                }
                                if(!strcasecmp(color,"B") || !strcasecmp(color,"BLACK")){
                                        (*bwall)--;
                                }
			}
		}
	}
	if(!strcasecmp(orient,"vertical")||!strcasecmp(orient,"v"))
        {
		for(i=1;i<4;i++){
			if(board[2*size-(2*b)+i][(4*a)+4] == 'H' || board[2*size-(2*b)+i][(4*a)+4] == '=')
				j++;
		}
		if(b<2 || b>size)
                        printf("?Invalid wall placement.\n");
		else{
                	for(i=1;i<4;i++){
				if(board[2*size-(2*b)+i][(4*a)+4] != 'H' && board[2*size-(2*b)+i][(4*a)+4] != '=' && j==1){
					board[2*size-(2*b)+i][(4*a)+4]='H';
					if(i==3){
						insert_at_start(history,a,b,color,orient,NULL,NULL);
						if(!strcasecmp(color,"W") || !strcasecmp(color,"WHITE")){
                                                	(*wwall)--;
                                        	}
                                        	if(!strcasecmp(color,"B") || !strcasecmp(color,"BLACK")){
                                        	        (*bwall)--;
                                        	}
					}
				}
                       		else{
                       	        	printf("?Invalid wall placement.\n");
                       	        	i=6;
                      		}
			}
                }
        }
	printf("=\n\n");
	fflush(stdout);
}

insert_at_start(Listptr *ptraddr, int line, int col, char* color, char* orient,int pline, int pcol)
{
	Listptr templist;
	templist = *ptraddr;
	*ptraddr = malloc(sizeof(struct listnode));
	(*ptraddr)->line = line;
	(*ptraddr)->col = col;
	strcpy((*ptraddr)->color,color);
	if(orient!=NULL)
		strcpy((*ptraddr)->orient,orient);
	(*ptraddr)->pline = pline;
	(*ptraddr)->pcol = pcol;
	(*ptraddr)->next = templist;
}

int undo(Listptr *ptraddr,int size,int **board,struct player *bpos,struct player *wpos,int *wwall,int *bwall)
{
	int i;
	Listptr templist;
	templist = *ptraddr;
	if((*ptraddr)!=NULL){
		if((*ptraddr)->orient==NULL || (strcasecmp((*ptraddr)->orient,"HORIZONTAL") && strcasecmp((*ptraddr)->orient,"H") && strcasecmp((*ptraddr)->orient,"VERTICAL") && strcasecmp((*ptraddr)->orient,"V"))){
			if( !strcasecmp((*ptraddr)->color,"W") || !strcasecmp((*ptraddr)->color,"WHITE")){
				board[(*ptraddr)->pline][(*ptraddr)->pcol]='W';
				wpos->l=(*ptraddr)->pline;
				wpos->c=(*ptraddr)->pcol;
			}
			else if(!strcasecmp((*ptraddr)->color,"B") || !strcasecmp((*ptraddr)->color,"BLACK")){
				board[(*ptraddr)->pline][(*ptraddr)->pcol]='B';
				bpos->l=(*ptraddr)->pline;
				bpos->c=(*ptraddr)->pcol;
			}
			board[(*ptraddr)->line][(*ptraddr)->col]=' ';
		}
		if(!strcasecmp((*ptraddr)->orient,"HORIZONTAL") || !strcasecmp((*ptraddr)->orient,"H")){
			for(i=1;i<8;i++){
        	        	board[(2*size)-(2*(*ptraddr)->col)][4*((*ptraddr)->line)+i]='-';
				if(i==4)
					board[(2*size)-(2*(*ptraddr)->col)][4*((*ptraddr)->line)+i]='+';
			}
			if(!strcasecmp((*ptraddr)->color,"W") || !strcasecmp((*ptraddr)->color,"WHITE"))
        	        	(*wwall)++;
        	        if(!strcasecmp((*ptraddr)->color,"B") || !strcasecmp((*ptraddr)->color,"BLACK"))
        	                (*bwall)++;
		}
		if(!strcasecmp((*ptraddr)->orient,"VERTICAL") || !strcasecmp((*ptraddr)->orient,"V")){
        	        for(i=1;i<6;i++){
        	                board[(2*size)-(2*(*ptraddr)->col)+i-1][4*((*ptraddr)->line)+4]='|';
        	                if(i%2==1)
        	                        board[(2*size)-(2*(*ptraddr)->col)+i-1][4*((*ptraddr)->line)+4]='+';
        	        }
        	        if(!strcasecmp((*ptraddr)->color,"W") || !strcasecmp((*ptraddr)->color,"WHITE"))
        	                (*wwall)++;
        	        if(!strcasecmp((*ptraddr)->color,"B") || !strcasecmp((*ptraddr)->color,"BLACK"))
        	                (*bwall)++;
        	}
		*ptraddr = (*ptraddr)->next;
		free(templist);
	}
	else
		printf("No moves remaining\n");
	printf("=\n\n");
	fflush(stdout);
}

int valid_move(int size,char* color, int n, int m,int ** board,struct player *bpos,struct player *wpos)
{
	if((!strcasecmp(color,"W") || !strcasecmp(color,"WHITE")) && (((wpos->l)-n==4  && board[((wpos->l)+n)/2][m]=='B') || ((wpos->c)-m==8 && board[n][(((wpos->c)+m)/2)-4]=='B') || ((wpos->c)-m==-8 && board[n][(((wpos->c)+m)/2)-4])))
                return 1;
	if((!strcasecmp(color,"B") || !strcasecmp(color,"BLACK")) && ((n-(bpos->l)==4  && board[((bpos->l)+n)/2][m]=='W') || ((bpos->c)-m==8 && board[n][(((bpos->c)+m)/2)-4]=='W') || ((bpos->c)-m==-8 && board[n][(((bpos->c)+m)/2)-4])))
                return 1;
	if((!strcasecmp(color,"W") || !strcasecmp(color,"WHITE")) && ((n!=(wpos->l) && m!=(wpos->c))||(n!=(wpos->l) && board[(n+(wpos->l))/2][m]=='=')||(m!=(wpos->c) && board[n][(m+(wpos->c))/2]=='H')||(wpos->l)-n>=4||m-wpos->c>4||(wpos->c)-m>4)){
                return 0;
        }
	else if(n>2*size || n<0 || m>=(4*size+2) || m<0){
		return 0;
	}
	else if((!strcasecmp(color,"B") || !strcasecmp(color,"BLACK")) && ((n!=(bpos->l) && m!=(bpos->c))||(n!=(bpos->l) && board[(n+(bpos->l))/2][m]=='=')||(m!=(bpos->c) && board[n][(m+(bpos->c))/2]=='H')||(n-(bpos->l)>=4||m-(bpos->c)>4||(bpos->c)-m>4))){
                return 0;
        }
        else if((n==bpos->l && m==bpos->c)||(n==wpos->l && m==wpos->c)){
                return 0;
        }
        else if(((!strcasecmp(color,"W") || !strcasecmp(color,"WHITE")) && board[n][m]=='B') || (!strcasecmp(color,"B") || !strcasecmp(color,"BLACK")) && board[n][m]=='W'){
                return 0;
        }
	else
                return 1;
}

int genmove(char* color,int size,int **board,struct player *wpos ,struct player *bpos, Listptr *history)
{
	int k,a,b,n,m;
        srand(time(NULL));
	do{
		printf("=  ");
		fflush(stdout);
		a=rand()%10+1;
		if(!strcasecmp(color,"W") || !strcasecmp(color,"WHITE")){
			if(a<=8 && valid_move(size,color,(wpos->l)-2,wpos->c,board,bpos,wpos)){
				n=(wpos->l)-2;
				m=wpos->c;
				insert_at_start(history,(wpos->l)-2,wpos->c,color,NULL,wpos->l,wpos->c);
				playgenmove(size,color,board,wpos,bpos,history,(wpos->l)-2,wpos->c);
				putchar(((wpos->c)/4)+'a');
				putchar((size-(wpos->l)/2)+'0');
			}
			else if(a>8 && a<=9 && valid_move(size,color,wpos->l,(wpos->c)-4,board,bpos,wpos)){
				n=wpos->l;
                	        m=(wpos->c)-4;
				insert_at_start(history,wpos->l,(wpos->c)-4,color,NULL,wpos->l,wpos->c);
				playgenmove(size,color,board,wpos,bpos,history,wpos->l,(wpos->c)-4);
				putchar(((wpos->c)/4)+'a');
				putchar((size-(wpos->l)/2)+'0');
			}
			else if(a>9 && a<=10 && valid_move(size,color,wpos->l,(wpos->c)+4,board,bpos,wpos)){
				n=wpos->l;
                	        m=(wpos->c)+4;
				insert_at_start(history,wpos->l,(wpos->c)+4,color,NULL,wpos->l,wpos->c);
				playgenmove(size,color,board,wpos,bpos,history,wpos->l,(wpos->c)+4);
				putchar(((wpos->c)/4)+'a');
				putchar((size-(wpos->l)/2)+'0');
			}
		}
		printf("\n\n");
        	fflush(stdout);
	}while(valid_move(size,color,n,m,board,bpos,wpos));
	if(!strcasecmp(color,"B") || !strcasecmp(color,"BLACK")){
                if(a<=4 && valid_move(size,color,(bpos->l)+2,bpos->c,board,bpos,wpos))
                        playgenmove(size,color,board,wpos,bpos,history,(bpos->l)+2,bpos->c);
                else if(a>4 && a<=7 && valid_move(size,color,bpos->l,(bpos->c)-4,board,bpos,wpos))
                        playgenmove(size,color,board,wpos,bpos,history,bpos->l,(bpos->c)-4);
                else if(a>7 && a<=10 && valid_move(size,color,bpos->l,(bpos->c)+4,board,bpos,wpos))
                        playgenmove(size,color,board,wpos,bpos,history,bpos->l,(bpos->c)+4);
        }
}

int playgenmove(int size,char * color, int ** board,struct player *wpos,struct player *bpos,Listptr *history,int n,int m)
{
        	if(!strcasecmp(color,"W") || !strcasecmp(color,"WHITE")){
			board[wpos->l][wpos->c]=' ';
                        board[n][m]='W';
			wpos->l=n;
			wpos->c=m;
        	}
        	if(!strcasecmp(color,"B") || !strcasecmp(color,"BLACK")){
			board[bpos->l][bpos->c]=' ';
                       	board[n][m]='B';
                       	bpos->l=n;
                       	bpos->c=m;
		}
}

int playmove(int size,char* color,int line, int col,int ** board,struct player *bpos,struct player *wpos, Listptr *history)
{
	int a,i,b,n,m;
	if(line>96 && line<123)
		a=line-'a';
	b=col-'0';
	n=(2*size)-(2*b-1);
	m=4*a+2;
	if(valid_move(size,color,n,m,board,bpos,wpos)==1){
	if(!strcasecmp(color,"W") || !strcasecmp(color,"WHITE")){
			board[wpos->l][wpos->c]=' ';
			board[n][m]='W';
			insert_at_start(history,n,m,color,NULL,wpos->l,wpos->c);
			wpos->l=n;
			wpos->c=m;
	}
	if(!strcasecmp(color,"B") || !strcasecmp(color,"BLACK")){
			board[bpos->l][bpos->c]=' ';
			board[(2*size)-(2*b-1)][4*a+2]='B';
			insert_at_start(history,n,m,color,NULL,bpos->l,bpos->c);
			bpos->l=(2*size)-(2*b-1);
			bpos->c=4*a+2;
	}
	}
	printf("=\n\n");
	fflush(stdout);
}

print(Listptr list){
	while (list != NULL) {
		printf("%s player played a %s wall or moved to %d %d from %d %d\n", (list->color),(list->orient),(list->line),list->col,list->pline,list->pcol);
		list = list->next;
	}
}

printpath(int ** path,int size)
{
	int i,j;
	for(i=0;i<2*size+1;i++){
                for(j=0;j<4*size+1;j++){
			if(path[i][j]!=0)
                        	printf("%d   ",path[i][j]);
		}
                printf("\n");
	}
}

int main()
{
	int i,j,size=9,**board,nwall,a,b,wwall,bwall,player=-1,oldsize=0,**path;
	char *arg1,*arg2,*arg3,*command;
	char choice,argument[30];
	struct player bpos;
        struct player wpos;
	Listptr history;
	history=NULL;
	arg1=malloc(6*sizeof(char));
	arg2=malloc(3*sizeof(char));
	arg3=malloc(10*sizeof(char));
	command=malloc(15*sizeof(char));
	fgets(argument,30,stdin);
	command = strtok(argument, " \n");
	arg1 = strtok(NULL, " \n");
	arg2 = strtok(NULL, " \n");
	arg3 = strtok(NULL, " \n");
	while(strcmp(command,"quit")!=0)
	{
		if(!strcmp(command,"known_command"))
			known_command(arg1);
		else if(!strcmp(command,"name"))
			name();
		else if (strcmp(command,"boardsize")==0){
			size=atoi(arg1);
			if(size%2==1 && (size>3 && size<=25))
			{
	                        boardsize(size,&board);
				printf("\n");
				bpos.l=1;
				bpos.c=(4*size+1)/2;
				wpos.l=2*size-1;
				wpos.c=(4*size+1)/2;
			}
			else
			{
				printf("?unacceptable size\n");
				fgets(argument,30,stdin);
        			command = strtok(argument, " \n");
        			arg1 = strtok(NULL, " \n");
        			arg2 = strtok(NULL, " \n");
        			arg3 = strtok(NULL, " \n");
			}
			if(oldsize==0)
				oldsize=size;
		}
		else if(!strcmp(command,"genmove")){
			genmove(arg1,size,board,&wpos,&bpos,&history);
		}
		else if(strcmp(command,"showboard")==0)
			showboard(board,size,&wwall,&bwall);
		else if(strcmp(command,"list_commands")==0)
			list_commands();
		else if(strcmp(command,"clear_board")==0)
			clearboard(size,board);
		else if(strcmp(command,"walls")==0){
			nwall=atoi(arg1);
			wwall=nwall;
			bwall=nwall;
			printf("=\n\n");
			fflush(stdout);
		}
		else if(!strcmp(command,"printpath"))
			printpath(path,size);
		else if(!strcmp(command,"undo"))
			undo(&history,size,board,&bpos,&wpos,&wwall,&bwall);
		else if(!strcmp(command,"playmove"))
		{
			a=arg2[0];
			b=arg2[1];
			a=tolower(a);
			playmove(size,arg1,a,b,board,&bpos,&wpos,&history);
		}
		else if(!strcmp(command,"playwall"))
		{
			a=arg2[0];
			b=arg2[1];
			playwall(size,arg1,a,b,board,arg3,&wwall,&bwall,&history);
		}
		else if(!strcmp(command,"winner"))
			winner(player,board,size);
		else if(!strcmp(command,"print"))
			print(history);
		else{
			printf("?Syntax Error\n");
		}
		fgets(argument,30,stdin);
		command = strtok(argument, " \n");
                arg1 = strtok(NULL, " \n");
                arg2 = strtok(NULL, " \n");
                arg3 = strtok(NULL, " \n");
	}
}
