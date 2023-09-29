#include <iostream> 
using namespace std;
//void Molecular_wt_oxide(float Element_Atomic_wt[12] ) 
int main() {
 // float Granite_A_CN_K[4]= {14.32, 1.39, 3.68, 4.07};
// float Granodioriteite_A_CN_K[4]= {15.73, 3.15, 3.75, 2.73};
// float Tonalite_A_CN_K[4]= {16.48, 4.446666667, 3.63, 2.07 };
// float Diorite_A_CN_K[4]= {16.67, 5.513333, 3.54, 1.76};
// float Basalt_A_CN_K[4]= {15.74, 8.193333, 2.91, 1.1};
// float Plagioclase_A_CN_K[4]= {22.66, 3.26, 9.89, 0.05};
// float K_Feldspar_A_CN_K[4]= {17.43, 0, NULL, 16.35};
                    // A.     C.     N.    K.    
float A_CN_K[7][4]= {{14.32, 1.39, 3.68, 4.07}, //Granite
                    {15.73, 3.15, 3.75, 2.73},//Granodioriteite
                    {16.48, 4.446666667, 3.63, 2.07 },//Tonalite
                    {16.67, 5.513333, 3.54, 1.76},// Diorite
                    {15.74, 8.193333, 2.91, 1.1},//Basalt
                    {22.66, 3.26, 9.89, 0.05},//Plagioclase
                    {17.43, 0,    0,   16.35}};//K_Feldspar

float Al2O3_K2O[4]= {101.96 ,56.08 ,61.98 , 94.2 };


float g[2]={0,3};
for (int xx = 0; xx <= 1; xx++) {
     cout<<endl;
for (int x = g[xx]; x <= g[xx]; x++) {
 for (int y = 0; y <= 6; y++) {
 cout<<( A_CN_K[y][x]/Al2O3_K2O[x] ) / (( A_CN_K[y][0]/Al2O3_K2O[0] ) + ( A_CN_K[y][1]/Al2O3_K2O[1] ) + ( A_CN_K[y][2]/Al2O3_K2O[2] ) + ( A_CN_K[y][3]/Al2O3_K2O[3] ) )* 100 <<" AK";
 cout<<endl;
 }}}
 cout<<endl;
 for (int y = 0; y <= 6; y++) {
cout<<(( A_CN_K[y][1]/Al2O3_K2O[1] ) + ( A_CN_K[y][2]/Al2O3_K2O[2] ) )/ (( A_CN_K[y][0]/Al2O3_K2O[0] ) + ( A_CN_K[y][1]/Al2O3_K2O[1] ) + ( A_CN_K[y][2]/Al2O3_K2O[2] ) + ( A_CN_K[y][3]/Al2O3_K2O[3] ) )* 100 << " "<<" CN";
 cout<<endl;
 }
    return 0;
}