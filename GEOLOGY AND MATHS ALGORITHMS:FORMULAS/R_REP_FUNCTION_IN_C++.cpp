#include <iostream>
using namespace std;

int main() {
int g[]={1,5,3};//REPEATED NO.OF TIMES
  
  int y[]={99,10,42};
 for (int i = 0;  i<=(sizeof(g) / sizeof(int))-1 ; i++) {
  for (int v = 0;  v<=g[i]-1; v++) {
      cout << y[i] << "\n"; 
      
  }}
  
  cout<<"///////////////////////////////////////////////////////////////////////////////";
  cout <<  "\n"; 
  
  int g1[]={1,4,3};for (int b : g1) {//# REPEATED NO. OF TIMES
    int y[]={99,10,42};for (int h : y) {
      for (int v = 0;  v<=b-1; v++) {
        cout << h << "\n"; 
      }}}
  cout<<"///////////////////////////////////////////////////////////////////////////////";
  cout <<  "\n"; 
  
    for(int k=0;k<=5;k++){
      
      for(int i = 0 ; i <=k-1 ;i++) {
        
        for(int z=k; z<=k;z++){
          cout <<z <<endl;
          
        }}}    //TO REAPEAT WITH INCREASING NUMBER
  
  return 0;
}
//(sizeof(myNumbers) / sizeof(int))-1  or 2