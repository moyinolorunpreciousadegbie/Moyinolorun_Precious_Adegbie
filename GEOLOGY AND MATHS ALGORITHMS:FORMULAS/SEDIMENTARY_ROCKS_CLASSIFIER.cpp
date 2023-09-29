#include <iostream>
using namespace std;

int main() {
	
int Quartz = 81;
int Feldspar  =4;   
int Lithics  =14;
	
// QUARTZ ARENITE 95,2,2
//SUB ARKOSE 81,14,4
//SUBLITHIC ARENITE  81,4,14
/// ARKOSE 9,84, 1 ,,,
///. LITHIC ARKOSE 9,57,27
///  FELDSPATHIC LITH-ARENITE  9,27,57
/// LITH-ARENITE. 9,1,84
	
	
if (Quartz >= 90 or Quartz ==100 ){
		cout << "Quartz Arenite";}
else if ((Quartz >= 75 and Quartz <= 90) and (Feldspar<=25 and Feldspar>=10)  and Lithics<=50){
		cout << "Subarkose";}
else if ((Quartz >= 75 and Quartz <= 90 )and (Lithics<=25 and Lithics>=10) and Feldspar<=50){
		cout << "Sublithic Arenite";  } 
else if (Quartz <= 75  and  Feldspar>=75 and Lithics <=25){
		cout << "Arkose"; }
	
else if (Quartz <= 75  and  (Feldspar<=75 and  Feldspar >=50) and  (Lithics >=25 and  Lithics <=50)){
		cout << "Lithic Arkose"; }
else if (Quartz <= 75  and  (Feldspar<=50 and  Feldspar >=25) and  (Lithics >=50 and   Lithics <=75)){
		cout << "Feldspathic Lith-Arenite"; }
else if (Quartz <= 75  and  Feldspar<=25  and  Lithics >=75 ){
		cout << "Lith-Arenite";      
	
}
	
	return 0;
}