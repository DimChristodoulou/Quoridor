int checkValidMove(board *b, int x, int y, player *p){
    if(x<0 || y<0 || x>=b->size || y>=b->size)
        return 0;
    if((b->player_1.position.x==x && b->player_1.position.y==y) || (b->player_2.position.x==x && b->player_2.position.y==y)) //pawn already there
        return 2; //return 2 if there is another player so we can jump over it
    int distance = ABS(p->position.x-x)+ABS(p->position.y-y);
    if(distance==1){
        if(thereIsWall(b, p->position.x, p->position.y, x, y))
            return 0;
        return 1;
    }else if(distance==2&&(p->position.x==x||p->position.y==y)){ //jump over pawn
        int x_middle = (p->position.x+x)/2, y_middle = (p->position.y+y)/2;
        if(!((b->player_1.position.x == x_middle && b->player_1.position.y == y_middle) || (b->player_2.position.x == x_middle && b->player_2.position.y == y_middle))) //no pawn in between
            return 0;
        if(thereIsWall(b, p->position.x, p->position.y, x, y))
            return 0;
        return 1;
    }else if(distance==2){
        player *opponent;
        if(p->color==BLACK)
            opponent = &(b->player_2);
        else
            opponent = &(b->player_1);
        if((ABS(p->position.x - opponent->position.x)+ABS(p->position.y - opponent->position.y))!=1)
            return 0;
        int xBehind=p->position.x, yBehind=p->position.y;
        if(p->position.x+1==opponent->position.x)
            xBehind = p->position.x+2;
        else if(p->position.x-1==opponent->position.x)
            xBehind = p->position.x-2;
        else if(p->position.y+1==opponent->position.y)
            yBehind = p->position.y+2;
        else if(p->position.y-1==opponent->position.y)
            yBehind = p->position.y-2;
        else
            return 0;
        if((xBehind < 0 || xBehind >= b->size || yBehind < 0 || yBehind >= b->size ||thereIsWall(b, opponent->position.x, opponent->position.y, xBehind, yBehind) )&& !thereIsWall(b, p->position.x, p->position.y, opponent->position.x, opponent->position.y) && !thereIsWall(b, opponent->position.x, opponent->position.y, x, y))
            return 1;
    }
    return 0;
}
 
