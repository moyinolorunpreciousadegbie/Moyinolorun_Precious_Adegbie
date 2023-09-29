#include <stdio.h>

int main() {
	
	char A[5] = {'A','B','C','D','E'};
    int len = sizeof(A) ;
	for(int i = 0 ; i < 2 ; ++i){
		//printf( "%d" ,i); 
		//printf("\t");
		//printf( "%d" ,1 - i);
		printf("%s","|"); 
		for(int ii = 0; ii < len ; ++ii){
			if(  (i + ii)  <  len    &&   (1 - i + ii)  <  len ){
				printf("%s","{"); 
				printf("%c", A[i + ii ]);
				printf("%c", A[1 - i + ii]  );
				printf("%s","}"); 
				//printf("%d", ii + 1);
				//printf("%d", i + ii) ; 
				//printf( "%d", 1 - i + ii) ;
				
			}
	}
	/*
	
		for i in range(2):
		#print(i, (1-i)) # i = 0, 1 |   1 - i = 1, 0
		for ii in range( len(AA)):
		if(     (i + ii)  <  len(AA)     and   (1 - i + ii)  <  len(AA)  ):
		print(AA[(i + ii)], AA[(1 - i + ii) ])
	*/
	}	
}