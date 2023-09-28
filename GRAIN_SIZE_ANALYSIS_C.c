#include <stdio.h>  

void Grain_analysis_algorithm(float Weight_in_grams[3][14] ) 
{
	printf("MONAHANS SAND ANALYSIS:\n");
	for (int y = 0; y <= 2; y++) {  
		printf("\n");
		char SAND5[] = {"ABC"}; char SAND6[] = {":::"};
		printf("%s","SAND "); 
		printf("%c",SAND5[y]);printf("%c",SAND6[y]);
		
		printf("\n");
		printf("\n");
		float cumulative_sum= 0;
		float cummulative_percent_retained=0;
		float Finess_Modulus=0;
		for (int x = 0; x <= 13; x++) {
			printf( "%f" , Weight_in_grams[y][x] );
			printf("%s","  | ");
			float percent_retained = 0;
			float total_sum= 0;
			for (int x = 0; x <= 13; x++)  {
				total_sum += Weight_in_grams[y][x];}
			
			printf("%s"," ");
			for (int yy =y ; yy <= y; yy++){
				percent_retained+=  Weight_in_grams[yy][x]/total_sum*100;
				float temp1[3][14];
				temp1[y][x] = percent_retained;
				cumulative_sum+= Weight_in_grams[yy][x];
				cummulative_percent_retained +=  temp1[yy][x];
				float temp2[3][14];
				temp2[y][x] = cummulative_percent_retained;
				
				printf("%s", " ");printf("%f" ,  cumulative_sum);printf("%s","  CUMULATIVE SUM"); printf("%s", "  | " );printf("%f",percent_retained );printf("%s","  % RETAINED    | " );printf( "%f", cummulative_percent_retained );printf("%s", "  CUMULATIVE % RETAINED   |");printf("%f",100 - cummulative_percent_retained );printf("%s", " %   FINER ");
				
				if (x<13 && y==yy)
					Finess_Modulus+= temp2[y][x] /100.00;
				printf("%s"," | FINESS MODULUS: ");
				printf("%f",Finess_Modulus);
				printf("\n");
				if(x==13 &&  y==yy &&  Finess_Modulus <=2.2 ){printf("\n");printf("%s","Very Fine Sand");printf("\n");}
				if(x==13 &&  y==yy &&  Finess_Modulus >=2.2 &&  Finess_Modulus <=2.6){printf("\n");printf("%s","Fine Sand");printf("\n");}
				if(x==13 &&  y==yy &&  Finess_Modulus >=2.6 &&  Finess_Modulus <=2.9){printf("\n");printf("%s","Medium Sand");printf("\n");}
				if(x==13 &&  y==yy &&  Finess_Modulus >=2.9 &&  Finess_Modulus <=3.2){printf("%s","Coarse Sand");printf("\n");}
				
				if(x==13 &&  y==yy &&  Finess_Modulus >=6 &&  Finess_Modulus <=6.9){printf("\n");printf("%s","20mm size of coarse aggregate");printf("\n");}
				if(x==13 &&  y==yy &&  Finess_Modulus >=6.9 &&  Finess_Modulus <=7.5){printf("\n");printf("%s","40mm size of coarse aggregate");printf("\n");}
				if(x==13 &&  y==yy && Finess_Modulus >=7.5 &&  Finess_Modulus <=8){printf("\n");printf("%s","75mm size of coarse aggregate");printf("\n");}
				if(x==13 &&  y==yy && Finess_Modulus >=8 &&  Finess_Modulus <=8.5){printf("\n");printf("%s","150mm size of coarse aggregate");printf("\n");}
			}}} printf("\n");}   

int main() {
float Weight_in_grams[3][14] = {
	{7,3,6,9,175,261,3,7,4,3,5,5,7,4 }, // MONAHANS SAMPLE A
	{1,3,2,8,198,258,10,6,2,3,2,1,2,1},   // MONAHANS SAMPLE B
	{3,2,3,14,190,253,4,5,4,5,3,4,3,3}};  // MONAHANS SAMPLE C
// -1|0|1|1.25|2|2.5|2.75|3|3.25|3.5|3.75|4|4.5 : phi(Φ) scale size 
printf( "%lu", sizeof(Weight_in_grams) / sizeof(int));
printf("%s"," values"); printf("\n");
printf( "%lu", sizeof(Weight_in_grams[0]) / sizeof(int) );
printf("%s"," columns represents weight in grams of each sieve");printf("\n");
printf( "%lu", ( sizeof(Weight_in_grams) / sizeof(int) ) /  (sizeof(Weight_in_grams[0]) / sizeof(int)) );
printf("%s", " rows represents samples collected");printf("\n");
printf("\n");
	
Grain_analysis_algorithm(Weight_in_grams  );
printf("\n");

	return 0;
}
