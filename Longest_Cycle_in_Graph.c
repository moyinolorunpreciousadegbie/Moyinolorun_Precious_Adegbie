#include <stdio.h>
#define len_edges 100   //  100   4 
#define MAX(a,b) ((a) > (b) ? (a) : (b))


int topSort(int node, int preCount, int color[len_edges], int longestCycle[1], int edges[len_edges]){

	if( color[node] == -1){ // No cycle afterwards so no value proceeding
		return 0;
	}
		// if (color[node] > 0){   // !=
		if (preCount - color[node] >= 2 && color[node] > 0){  
			longestCycle[0] = MAX(  longestCycle[0]  , preCount - color[node]);
		return 1 ;
	}
	
	color[node] = preCount ;
	if(edges[node] != -1){
		
		char hasCycle;
		hasCycle = topSort(edges[node],  preCount + 1,  color,  longestCycle,  edges) ;
	
		if(hasCycle == 1){
			return 1;
		}}
	
	color[node] = -1 ; 
	
	return 0 ;}



int longestCycle(int edges[len_edges]){
	
	int color[ len_edges ] ;
	for(int i = 0; i < len_edges ; i++)	{
		color[i] = 0;  // Initially all elements are not visited
	}
	
int longestCycle[1] = {-1};  // intitialize longest cycle to be smallest value

for(int i = 0; i < len_edges ; i++)	{
topSort(i, 0 , color ,longestCycle, edges ) ; 
}

return longestCycle[0] ;}



int main() {

int edges[len_edges] = {3,3,4,2,3} ;  // len 5
//Output: 3
printf( "%d", longestCycle(edges)  );

printf("\n");

int edge[4] = {2,-1,3,1} ;// -1   // len 4
//Output: -1
printf( "%d", longestCycle(edge)  );

printf("\n");

int fifty[100]= {1,19,30,87,53,91,36,6,95,14,73,2,59,76,49,41,29,28,8,9,96,80,68,10,31,24,0,42,39,4,51,64,25,90,35,71,97,32,16,18,62,22,40,78,55,13,99,93,66,26,98,5,88,74,89,81,43,12,44,57,75,47,34,72,85,77,3,65,46,20,60,33,48,94,84,21,69,54,56,11,70,83,86,79,61,37,67,15,7,38,23,52,58,27,50,63,92,45,17,82};                   // 26  //100 len

//Output: 50

printf( "%d", longestCycle( fifty)   );

	

}