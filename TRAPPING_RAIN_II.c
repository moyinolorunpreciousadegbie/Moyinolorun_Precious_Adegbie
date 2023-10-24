#include <stdio.h>  
#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define R 5
#define C 7

// hjscoder

int dfs(int y, int x, int visited[R][C] , int min_edge, int MAT[R][C] )
{
	
	int DR[4]={1,0,-1,0};
	int DC[4]={0,1,0,-1};
	for(int i=0;i<4;i++){
		int yy = x+DR[i];
		int xx = y+DC[i];
		
		if( MAT[y][x] >= MAT[yy][xx] ){     // min_edge != 0
			
			if ( visited[yy][xx] == 0  && (0 < yy < R-1) && (0 < xx < C-1)  ){  
				visited[yy][xx] = 1;

				min_edge = dfs(yy, xx,  visited, min_edge, MAT) ;
			}
			if(  (yy == 0 || yy == R-1)  || (xx == 0 || xx == C-1 ) ){
				min_edge =   0 ;
			}
		}
		else{
			min_edge = min(min_edge, MAT[yy][xx]) ;
		}
	}return min_edge ;
}

int Trap2(int MAT[R][C] ) 
{
	int ans = 0 ;
	
	for(int i = 1; i < R - 1 ; ++i){
		for(int j = 1; j < C - 1; ++j){
			
		int visited[R][C] ;	
		for(int rr = 0; rr < R   ; ++rr){
			for(int cc = 0; cc < C ; ++cc){
				visited [rr][cc] = 0;}}
		visited [i][j] = 1;
	int inf = 999999999  ;
	int min_edge = dfs(i, j, visited, inf, MAT) ;

	if(min_edge == 0 ){
		
		/*
		for(int rrr1 = 0; rrr1 < R ; ++rrr1){
			for(int ccc1 = 0; ccc1 < C ; ++ccc1){
				if (visited[rrr1][ccc1] == 1){	
					if(MAT[rrr1][ccc1] >= MAT[i][j] ){
						visited [rrr1][ccc1] = 1;
		if(MAT[rrr1][ccc1] < MAT[i][j] ){
		visited [rrr1][ccc1] = 0;
		visited [i][j] = 1 ;
					}}}}    }
		*/
	
		continue;
	}
	
else { 
	for(int rrr = 0; rrr < R ; ++rrr){
		for(int ccc = 0; ccc < C ; ++ccc){
			
	if (visited[rrr][ccc] == 1){
	ans += min_edge - MAT[rrr][ccc] ;
	MAT[rrr][ccc] = min_edge ;
	
	}}}    }}}return ans;}

int main() {
	
	int MAT[R][C] = {{30,30,30,30,30,30,30},{30,2,2,2,2,2,30},{30,2,1,100,1,2,30},{30,2,2,2,2,2,30},{30,30,30,30,30,30,30}} ;
	
	printf( "%d" ,Trap2(MAT ) ) ;  
	
	printf("\n");
	
	int arr[3][6] = {{1, 4, 3, 1, 3, 2}, 
		{3, 2, 1, 3, 2, 4},
		{2, 3, 3, 2, 3, 1}};
	
	//printf( "%d" ,Trap2(arr ) ) ; 
	
	int u[3][4] = {{4, 4, 4, 4},    // 2
		          {4, 1, 3, 4},
		          {4, 4, 3, 4}};
	
	//printf( "%d" ,Trap2(u ) ) ; 
	
	printf("\n");
	
	int yy[5][4] =  {{12,13,1,12},{13,4,13,12},{13,8,10,12},{12,13,12,12},{13,13,13,13}};
	//printf( "%d" ,Trap2(yy) ) ;  // 14
	
	printf("\n");
	
	
	
	int heightMap[3][6] = {{1,4,3,1,3,2},{3,2,1,3,2,4},{2,3,3,2,3,1}};  // 4   NOT WORK
	//printf( "%d" ,Trap2(heightMap) ) ; 
	
	printf("\n");
	
	int heightMap1[5][5] = {{3,3,3,3,3},{3,2,2,2,3},{3,2,1,2,3},{3,2,2,2,3},{3,3,3,3,3}}; // 10
	//printf( "%d" ,Trap2(heightMap1) ) ; 
	
	printf("\n");
	return 0;
}