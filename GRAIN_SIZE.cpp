#include <iostream> 
using namespace std;   

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Grain_analysis_algorithm(float Weight_in_grams[3][14] ) 
{
cout<<"MONAHANS SAND ANALYSIS:"<<endl;
   for (int y = 0; y <= 2; y++) {  
      cout<<endl;
      string SAND[] = {"SAND A :" , "SAND B :" , "SAND C :"};  
      cout << SAND[y]; cout<<endl;
      float cumulative_sum= 0;
      float cummulative_percent_retained=0;
      float Finess_Modulus=0;
       for (int x = 0; x <= 13; x++) { 
        cout << "\{" << Weight_in_grams[y][x] << "\}"<<" "; cout<<"\:";
         float percent_retained = 0;
         float total_sum= 0;
          for (int x = 0; x <= 13; x++)  
            total_sum += Weight_in_grams[y][x];
         cout<<" ";
            for (int yy =y ; yy <= y; yy++){
               percent_retained+=  Weight_in_grams[yy][x]/total_sum*100;
               float temp1[3][14];
               temp1[y][x] = percent_retained;
               cumulative_sum+= Weight_in_grams[yy][x];
               cummulative_percent_retained +=  temp1[yy][x];
               float temp2[3][14];
               temp2[y][x] = cummulative_percent_retained;
            
               cout<<" " << cumulative_sum<<"  CUMULATIVE SUM"<< "  | "<<percent_retained <<"  % RETAINED    | "<<cummulative_percent_retained<<"  CUMULATIVE % RETAINED   |"<< 100 - cummulative_percent_retained <<" %   FINER"<<" ";
            
                if (x<13 and y==yy)
            Finess_Modulus+= temp2[y][x] /100;
            cout<<" | FINESS MODULUS: "<<Finess_Modulus;cout<<endl;
               if(x==13 and y==yy and Finess_Modulus <=2.2 ){cout<<endl;cout<<"Very Fine Sand";cout<<endl;}
               if(x==13 and y==yy and Finess_Modulus >=2.2 and Finess_Modulus <=2.6){cout<<endl;cout<<"Fine Sand";cout<<endl;}
               if(x==13 and y==yy and Finess_Modulus >=2.6 and Finess_Modulus <=2.9){cout<<endl;cout<<"Medium Sand";cout<<endl;}
               if(x==13 and y==yy and Finess_Modulus >=2.9 and Finess_Modulus <=3.2){cout<<"Coarse Sand";cout<<endl;}
               
               if(x==13 and y==yy and Finess_Modulus >=6 and Finess_Modulus <=6.9){cout<<endl;cout<<"20mm size of coarse aggregate";cout<<endl;}
               if(x==13 and y==yy and Finess_Modulus >=6.9 and Finess_Modulus <=7.5){cout<<endl;cout<<"40mm size of coarse aggregate";cout<<endl;}
               if(x==13 and y==yy and Finess_Modulus >=7.5 and Finess_Modulus <=8){cout<<endl;cout<<"75mm size of coarse aggregate";cout<<endl;}
               if(x==13 and y==yy and Finess_Modulus >=8 and Finess_Modulus <=8.5){cout<<endl;cout<<"150mm size of coarse aggregate";cout<<endl;}
      }}}}   
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


void Two_to_One(int Grid[][3]){
   
   
   int Row =  3; //( sizeof(Grid) / sizeof(int) ) /  (sizeof(Grid[0]) / sizeof(int));
   int Col = ( sizeof(Grid[0]) / sizeof(int) );
   
   int vis[Row * Col] ;
   
   cout << "2 to 1"<<" = ";
   for (int r = 0  ; r < Row; r++){
   for (int c = 0  ; c < Col; c++){
   int index = (r * Col) + c ; 
   
   vis[index] = Grid[r][c];
   
   cout << vis[index] << ",";  
   
   }}cout<<"||";}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

      
void One_to_Two(int Grid[], int Row , int Col){
         
         
         
         int len = ( sizeof(Grid[0]) / sizeof(int) );
         
         int vis[Row][ Col] ;
         
         cout << "1 to 2"<<" = ";
         /// for (int c = 0  ; c < Col; c++){    ////  TRANSPOSE WHEN YOU WANT TO ROW OR COL BIND OR STACK  !!!
         for (int r = 0  ; r < Row; r++){
            for (int c = 0  ; c < Col; c++){
               int index = (r * Col) + c ; 
               
               vis[r][c] = Grid[index];
               
               cout << vis[r][c]<< ",";   
               
            }}cout<<"||";}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


///*
void One_to_Three(int Grid[], int Row , int Col, int Height){
   
   int vis[Height][Row][Col];
   
   
   cout << "1 TO 3"<<" = ";
   //int vis[[Height * Row * Col];
   for (int h = 0  ; h < Height; h++){
      for (int r = 0  ; r < Row; r++){
         for (int c = 0  ; c < Col; c++){
            
            //int indexx = c * Row + r + (h * (Col * Row )) ; // * bigger dimensions with the h
            //int indexx = c * Row + r + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
            
            int indexx = r * Col + c + (h * (Col * Row )) ; // * bigger dimensions with the h
            //int indexx = r * Col + c + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
            //cout << indexx<<"*";
            vis[h][r][c] = Grid[indexx];
            // new[indexx] = vis3[h][r][c]
            
            
            cout << vis[h][r][c] << ",";
         }}}cout<<"||";}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


//*/
void Three_to_One(int Grid[2][4][3] , int Row , int Col, int Height){
   
   
   int vis[Height * Row * Col] ;
   
   cout << "3 TO 1"<<" = ";
   //int vis[[Height * Row * Col];
   for (int h = 0  ; h < Height; h++){
      for (int r = 0  ; r < Row; r++){
         for (int c = 0  ; c < Col; c++){
            
            
           //int indexx = c * Row + r + (h * (Col * Row )) ; // * bigger dimensions with the h
            //int indexx = c * Row + r + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
            
            int indexx = r * Col + c + (h * (Col * Row )) ; // * bigger dimensions with the h
            //int indexx = r * Col + c + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
            
            vis[indexx] = Grid[h][r][c] ;
            
            cout << vis[indexx] << ",";
         }}}cout<<"||";}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


void concatenate(int arr1[3], int arr2[5]){
   
int len_1 = 3; //( sizeof(arr1) / sizeof(int));
int len_2 = 5; // ( sizeof(arr2) / sizeof(int) );

int arr3[len_1  + len_2];

cout << "concatenate"<<" = ";
   for (int l1 = 0  ; l1 < len_1; l1 ++){
      for (int l2 = 0  ; l2 < len_2; l2 ++){

arr3[l1] = arr1[l1];
arr3[len_1 + l2] = arr2[l2];}}
for (int l3 = 0  ; l3 < len_1  + len_2 ; l3 ++){
cout << arr3[l3] << ","; 

}cout<<"||";}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




int main() {
 float Weight_in_grams[3][14] = {
   {7,3,6,9,175,261,3,7,4,3,5,5,7,4 }, // MONAHANS SAMPLE A
   {1,3,2,8,198,258,10,6,2,3,2,1,2,1},   // MONAHANS SAMPLE B
   {3,2,3,14,190,253,4,5,4,5,3,4,3,3}};  // MONAHANS SAMPLE C
// -1|0|1|1.25|2|2.5|2.75|3|3.25|3.5|3.75|4|4.5 : phi(Φ) scale size 
cout<< sizeof(Weight_in_grams) / sizeof(int)<<" values"<<endl;
cout<< sizeof(Weight_in_grams[0]) / sizeof(int) << " columns represents weight in grams of each sieve"<<endl;
cout<<( sizeof(Weight_in_grams) / sizeof(int) ) /  (sizeof(Weight_in_grams[0]) / sizeof(int))<< " rows represents samples collected"<<endl;
cout<<endl;

Grain_analysis_algorithm(Weight_in_grams  );
cout<<endl;




int Grid[3][3] = {{1, 2, 3}, {4, 5, 6},{7, 8, 9}};

Two_to_One(Grid); 



int Grid_1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
int Row = 4;
int Col = 3;
One_to_Two( Grid_1, Row , Col);

int Grid_2[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24};
int Height = 2;

One_to_Three(Grid_2, Row , Col, Height);


int Grid_3[2][4][3] ={ {{1, 2, 3},
                       {4, 5, 6}, 
                       {7, 8, 9},
                       {10, 11, 12}},
                        
                     {{13, 14, 15}, 
                      {16, 17, 18},
                      {19, 20, 21}, 
                      {22, 23, 24}}   };
Three_to_One(Grid_3, Row , Col, Height);


int arr1[3] = {1, 2, 3};
   
int arr2[5] = {4, 5, 6, 7, 8};

concatenate(arr1, arr2);

return 0;
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
   