// Constrained Subsequence Sum - Leetcode 1425
#include <stdio.h>
#define C 5   // 3

int doit(int A[C],int k){

int maxx = -1111;
if(k == 1){
	
	for(int i = 0; i < C ; i++)	{ 
		if (A[i] > maxx) {
			maxx = A[i];} return maxx ; }}

	
int cn = 0;
int cc = 0;
	for(int i = 0; i < C ; i++)	{
			cc += 1 ;
		if (A[i] > 0 ){
			cn+=1 ;
			
			if(cn == 1 && cc == C){
				return A[i];}}}

k -=1 ;

int AC[C][C];
for(int i = 0; i < C ; i++)	{
	for(int ii = 0; ii < C ; ii++)	{
	AC[i][ii] = 0;	
	}}


	for(int jj = 0; jj < 1 ; jj++)	{
	for(int i = 0; i < C ; i++)	{
	for(int j = 0; j < C ; j++)	{
	AC[i+  C * jj][j] = A[j] ;
	}}}
	
	for(int i = 0; i < C ; i++)	{
		for(int kk = 0; kk < k ; kk++)	{
		int cnt = 0;
		for(int move = 0; move < kk  + i + 1 ; move++)	{
		if(move < C  ){
			AC[ i ][move] = 0 ;
			cnt+=1 ;
		}}}}
	
		
	for(int i = 1; i < C ; i++)	{
		
		for(int j = 0; j < i ; j++)	{
	
	AC[i][j] = A[j] ;}}

	int RR;
	
	RR = C - k + 1 ;
	
	
			int ACC[RR][C];
			for(int i = 0; i < RR ; i++)	{
				
				for(int j = 0; j < C ; j++)	{
						
						ACC[i][j] = AC[i][j];
						
					}}
				int B[C][C - k + 1];
		
		
	for (int i = 0; i < C; i++) {
		
		for (int j = 0; j < C  - k + 1; j++) {
			
			B[i][j] = ACC[j][i];
		}}
			
			
			
			
			int idx = -1;
			
			// Variable to store max sum
			int maxSum = -999999;
			
			// Traverse matrix column wise
			for (int i = 0; i < RR; i++) {
				int sum = 0;
				
				// calculate sum of column
				for (int j = 0; j < C; j++) {
					sum += B[j][i];
				}
				
				// Update maxSum if it is less than
				// current sum
				if (sum > maxSum) {
					maxSum = sum;
					
					// store index
					idx = i;
				}
			}
			
			
		
	
	return maxSum;}


	
int main() {	
	
	int A[C]  = {10,2,-10,5,20};    //     len 5                                                                        ANS 37
	int k = 2;
	printf( "%d", doit(A, k)  );
	
	printf("\n") ; 
	
	
	
	int nums1[3] = {-1,-2,-3} ; //                                                                                      ANS   -1 
	int kk = 1  ;
	printf( "%d", doit(nums1, kk) );
	
	
	printf("\n") ; 

	
	int nums2[5] = {10,-2,-10,-5,20} ; //                                                                                ANS 23			
		printf( "%d", doit(nums2, k) );
			printf("\n") ; 
				
				int numm[5]={-1000,-2000,-3000,-4000,2}; // answer is 2 working on a shorter, better faster solution     ANS  2
				
				int ki=2 ;
				
				printf( "%d",  doit(numm, ki) );


}