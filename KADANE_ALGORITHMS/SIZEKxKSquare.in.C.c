#include <stdio.h>
#define R 4 // 4 4 4  1  1  1     1    1
#define C 5 // 5 4 4  3  2  1     4    3

int sumQuery(int mat[R][C], int r, int c, int r2, int c2){
	
	
	int vis[R * C] ;

	int sum = 0 ; // 1 for multiplication, 0 for addition
	for (int i = r  ; i <= r2; i++){
		for (int j = c  ; j <= c2; j++){
		
			int index = (i * C) +  j; 
			vis[index] = mat[i][j];
			sum += vis[index];
		}}
	return sum;}

int SIZEKxKSquare(int mat[R][C], int row, int col)
{
	if(   R == 1 && C == 1 ){
		
		printf("%s","No Sub Sum because of size 1 x 1 ");
		printf("\n");
		printf("%s","Matrix is still: ");
		for (int r = 0  ; r < R; r++){
			for (int c = 0  ; c < C; c++){
				
				return mat[r][c];
	}}}
                 
	int max_sum = -99999999;
	int sum = 0;
	
	for (int r = 0  ; r < R; r++){
		for (int c = 0  ; c < C; c++){
			for (int r2 = 0  ; r2 < R; r2++){
				for (int c2 = 0  ; c2 < C; c2++) {                                                  ///////
					if( r <= r2 && c <= c2  &&  ( (r2 + 1 - r)!= R || (c2 + 1 - c) !=C ) && ( r2 + 1 - r) == row && (c2 + 1 - c)  == col )  { 						
						if( (  (r2 + 1 - r) * (c2 + 1 - c)  )/ ( r2 + 1 - r)   ==     ( r2 + 1 - r ) || (c2 + 1 - c) && (  (r2 + 1 - r) * (c2 + 1 - c)  )/ (c2 + 1 - c)   ==  ( r2 + 1 - r ) ||   (c2 + 1 - c)     ) {   
							sum = sumQuery( mat , r, c, r2, c2);  
							if (sum > max_sum){
								max_sum = sum;
								
							}}   
							if ( max_sum == sum && sum == sumQuery( mat , r, c, r2, c2) && sumQuery( mat , r, c, r2, c2) == max_sum){
								printf("\n");
								printf("\n");
								printf("%s","Top, Left:"); printf( "%d" ,r); printf("%s",",");printf( "%d" ,c);
								printf("\n");
								printf("%s","Bottom, Right:"); printf( "%d" ,r2); printf("%s",",");printf( "%d" ,c2);
							
						 							
							
							int i, j;
							for ( i = r  ; i <= r2; i++){
								printf("\n");
								for ( j = c  ; j <= c2; j++){
									printf(",");	
									printf( "%d" , mat[i][j]) ;  
									
									
				}} }	 }}}
		}
	}printf("\n");printf("%s","SUM IS:   ");
	
	return max_sum; 
}

// 35 lines
		
int main() {
	
int M[4][5] = {{1, 2, -1, -4, -20},
             {-8, -3, 4, 2, 1}, 
             {3, 8, 10, 1, 3},
            {-4, -1, 1, 7, -6}} ;
			
int rw = 2 ;
int  cl = 3;

printf( "%d", SIZEKxKSquare(M, rw, cl)  );  // 3715891200
printf("\n");

}