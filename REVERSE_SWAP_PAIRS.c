#include <stdio.h>

int main() {
	
	char A[5] = {'A','B','C','D','E'};
	int u[]= {1,2,3,4,5};
	char greetings2[] = "Hello World!";
	int len = sizeof(A) ;
	for(int j = len - 1 ; j >= len - 2  ; --j){
		//printf( "%d" ,j); 
		//printf("\t");
		//printf( "%d" ,len - 1 + len - 2 - j);      |{ED}{DC}{CB}{BA}|{DE}{CD}{BC}{AB}      > len - 3 
		printf("%s","|");                         // |{ED}{DC}{CB}{BA}|{DE}{CD}{BC}{AB}     >= len - 2 
		for(int jj = 0; jj <= len - 1 ; ++jj){
			if( (j - jj) >= 0  &&  (len - 1 + len - 2 - j - jj)   >= 0 ){
				printf("%s","{"); 
				printf("%c", A[j - jj  ]);
				printf("%c", A[len -1 + len -2 - j - jj ]  );
				printf("%s","}"); 
								
				
			}
	}
	/*
	PYTHON CODE
	
	for j in range(len(AA)-1,len(AA)-3, -1):  #  (5, 4)
	#print(j,      (len(AA)-1+len(AA)-2) - j ) #  (5, 4) (4, 5)
	for jj in range(len(AA)):
	if(    (j - jj)  >= 0     and    (len(AA)-1 + len(AA)-2 - j - jj)   >= 0  ):
	print(AA[(j - jj ) ], AA[(len(AA)-1 + len(AA)-2 - j - jj) ])
	*/
	}	
}
