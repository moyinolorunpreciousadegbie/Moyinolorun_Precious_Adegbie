#include <stdio.h>  
//#include <math.h>

/// C algorithm to flatten array to 1 dimension or change for one dimension to a higher dimension.  (I think python Numpy library might be using this in the background) !!

void One_to_Two(int Grid[], int Row , int Col){
   
   int len = ( sizeof(Grid[0]) / sizeof(int) );
   int vis[Row][ Col] ;
   
   printf("%s", "1 to 2  = ");
   for (int r = 0  ; r < Row; r++){
      for (int c = 0  ; c < Col; c++){
         int index = (r * Col) + c ; 
         
         vis[r][c] = Grid[index];
         
         printf( "%d" , vis[r][c]);
         printf("%s",",");   
         
      }}printf("%s","||");printf("\n");}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void Two_to_One(int Grid[][3]){
   
   
   int Row =  3; //( sizeof(Grid) / sizeof(int) ) /  (sizeof(Grid[0]) / sizeof(int));
   int Col = ( sizeof(Grid[0]) / sizeof(int) );
   
   int vis[Row * Col] ;
   
   printf("%s", "2 to 1  = ");
   for (int r = 0  ; r < Row; r++){
   for (int c = 0  ; c < Col; c++){
   int index = (r * Col) + c ; 
   
   vis[index] = Grid[r][c];
   
      printf( "%d" , vis[index] );
      printf("%s",",");  
   
   }}printf("%s","||");printf("\n");}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///*
void One_to_Three(int Grid[], int Row , int Col, int Height){
   
   int vis[Height][Row][Col];
   
   
   printf("%s", "1 to 3  = ");
   //int vis[[Height * Row * Col];
   for (int h = 0  ; h < Height; h++){
      for (int r = 0  ; r < Row; r++){
         for (int c = 0  ; c < Col; c++){
            
            //int indexx = c * Row + r + (h * (Col * Row )) ; // * bigger dimensions with the h
            //int indexx = c * Row + r + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
            
            int indexx = r * Col + c + (h * (Col * Row )) ; // * bigger dimensions with the h
            //int indexx = r * Col + c + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
            
            vis[h][r][c] = Grid[indexx];
            
            printf( "%d" , vis[h][r][c] );
            printf("%s",","); 
         }}}printf("%s","||");printf("\n");}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//*/
void Three_to_One(int Grid[2][4][3] , int Row , int Col, int Height){
   
   int vis[Height * Row * Col] ;
   
   printf("%s", "3 to 1  = ");
   //int vis[[Height * Row * Col];
   for (int h = 0  ; h < Height; h++){
      for (int r = 0  ; r < Row; r++){
         for (int c = 0  ; c < Col; c++){
            
           //int indexx = c * Row + r + (h * (Col * Row )) ; // * bigger dimensions with the h
            //int indexx = c * Row + r + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
            
            int indexx = r * Col + c + (h * (Col * Row )) ; // * bigger dimensions with the h
            //int indexx = r * Col + c + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
   
            vis[indexx] = Grid[h][r][c] ;
            
            printf( "%d" , vis[indexx]);
            printf("%s",","); 
         }}}printf("%s","||");printf("\n");}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void One_to_Four(int Grid[] , int Row , int Col, int Height, int Height2){
   
   int vis[Height2][Height][Row][Col] ;
   
   printf("%s", "1 to 4  = ");
   //int vis[[Height * Row * Col];
   for (int hh = 0  ; hh < Height2; hh++){
      for (int h = 0  ; h < Height; h++){
         for (int r = 0  ; r < Row; r++){
            for (int c = 0  ; c < Col; c++){
               
               //int indexx = c * Row + r + (h * (Col * Row )) ; // * bigger dimensions with the h
               //int indexx = c * Row + r + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
               
               int indexx = r * Col+ c + (h *  (Col * Row )) + (hh *  (Height * Col * Row ))  ; // * bigger dimensions with the h
               //int indexx = r * Col + c + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
               
               vis[hh][h][r][c] = Grid[indexx] ;
               
               printf( "%d" , vis[hh][h][r][c]);
               printf("%s",","); 
            }}}}printf("%s","||");printf("\n");}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void Four_to_One(int Grid[5][2][5][2] , int Row , int Col, int Height, int Height2){
   
   int vis[Height2 * Height * Row * Col] ;
   
   printf("%s", "4 to 1  = ");
   //int vis[[Height * Row * Col];
   for (int hh = 0  ; hh < Height2; hh++){
   for (int h = 0  ; h < Height; h++){
      for (int r = 0  ; r < Row; r++){
         for (int c = 0  ; c < Col; c++){
            
            //int indexx = c * Row + r + (h * (Col * Row )) ; // * bigger dimensions with the h
            //int indexx = c * Row + r + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
            
            int indexx = r * Col+ c + (h *  (Col * Row )) + (hh *  (Height * Col * Row ))  ; // * bigger dimensions with the h
            //int indexx = r * Col + c + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
            
            vis[indexx] = Grid[hh][h][r][c] ;
            
            printf( "%d" , vis[indexx]);
            printf("%s",","); 
         }}}}printf("%s","||");printf("\n");}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void One_to_Five(int Grid[] , int Row , int Col, int Height, int Height2, int Height3){
   
   int vis[Height3][Height2][Height][Row][Col] ;
   
   printf("%s", "1 to 5  = ");
   //int vis[[Height * Row * Col];
   for (int hhh = 0  ; hhh < Height3; hhh++){
   for (int hh = 0  ; hh < Height2; hh++){
      for (int h = 0  ; h < Height; h++){
         for (int r = 0  ; r < Row; r++){
            for (int c = 0  ; c < Col; c++){
               
               //int indexx = c * Row + r + (h * (Col * Row )) ; // * bigger dimensions with the h
               //int indexx = c * Row + r + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
               
               int indexx = r * Col+ c + (h *  (Col * Row )) + (hh *  (Height * Col * Row )) + (hhh *  (Height2 * Height * Col * Row )) ; // * bigger dimensions with the h
               //int indexx = r * Col + c + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
               
               vis[hhh][hh][h][r][c] = Grid[indexx] ;
               
               printf( "%d" , vis[hhh][hh][h][r][c]);
               printf("%s",","); 
            }}}}}printf("%s","||");printf("\n");}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void Five_to_One(int Grid[3][5][2][5][2] , int Row , int Col, int Height, int Height2,  int Height3){
   
   int vis[Height3 * Height2 * Height * Row * Col] ;
   
   printf("%s", "5 to 1  = ");
   //int vis[[Height * Row * Col];
   for (int hhh = 0  ; hhh < Height3; hhh++){
   for (int hh = 0  ; hh < Height2; hh++){
      for (int h = 0  ; h < Height; h++){
         for (int r = 0  ; r < Row; r++){
            for (int c = 0  ; c < Col; c++){
               
               //int indexx = c * Row + r + (h * (Col * Row )) ; // * bigger dimensions with the h
               //int indexx = c * Row + r + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
               
               int indexx = r * Col+ c + (h *  (Col * Row )) + (hh *  (Height * Col * Row )) + (hhh *  (Height2 * Height * Col * Row ))  ; // * bigger dimensions with the h
               //int indexx = r * Col + c + (h * (Col + (2 * Row) + 1))  ; // * bigger dimensions with the h
               
               vis[indexx] = Grid[hhh][hh][h][r][c] ;
               
               printf( "%d" , vis[indexx]);
               printf("%s",","); 
         }   }}}}printf("%s","||");printf("\n");}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void concatenate(int arr1[3], int arr2[5]){
   
int len_1 = 3; //( sizeof(arr1) / sizeof(int));
int len_2 = 5; // ( sizeof(arr2) / sizeof(int) );

int arr3[len_1  + len_2];

printf("%s", "concatenate   = ");
   for (int l1 = 0  ; l1 < len_1; l1 ++){
      for (int l2 = 0  ; l2 < len_2; l2 ++){

arr3[l1] = arr1[l1];
arr3[len_1 + l2] = arr2[l2];}}
for (int l3 = 0  ; l3 < len_1  + len_2 ; l3 ++){
printf( "%d" , arr3[l3]);
   printf("%s",","); 

}printf("%s","||");}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


int main() {
 

int Grid_1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
int Row = 4;
int Col = 3;
One_to_Two( Grid_1, Row , Col);
   
int Grid[3][3] = {{1, 2, 3}, {4, 5, 6},{7, 8, 9}};

Two_to_One(Grid); 

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



   int RR = 5;
   int CC = 2;
   int HH = 2;
   int HHH = 5;

int dim[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100};

int dim2[5][2][5][2] = {{{{1, 2}, {3, 4}, {5, 6}, {7, 8}, {9, 10}}, {{11, 12}, {13, 14}, {15, 16}, {17, 18}, {19, 20}}}, {{{21, 22}, {23, 24}, {25, 26}, {27, 28}, {29, 30}}, {{31, 32}, {33, 34}, {35, 36}, {37, 38}, {39, 40}}}, {{{41, 42}, {43, 44}, {45, 46}, {47, 48}, {49, 50}}, {{51, 52}, {53, 54}, {55, 56}, {57, 58}, {59, 60}}}, {{{61, 62}, {63, 64}, {65, 66}, {67, 68}, {69, 70}}, {{71, 72}, {73, 74}, {75, 76}, {77, 78}, {79, 80}}}, {{{81, 82}, {83, 84}, {85, 86}, {87, 88}, {89, 90}}, {{91, 92}, {93, 94}, {95, 96}, {97, 98}, {99, 100}}}};

One_to_Four(dim , RR , CC, HH,  HHH);
   Four_to_One(dim2 , RR , CC, HH,  HHH);
      
      
   int HHHH = 3;

int dimm[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300};

int dimm2[3][5][2][5][2] = {  {{{{1, 2}, {3, 4}, {5, 6}, {7, 8}, {9, 10}}, {{11, 12}, {13, 14}, {15, 16}, {17, 18}, {19, 20}}}, {{{21, 22}, {23, 24}, {25, 26}, {27, 28}, {29, 30}}, {{31, 32}, {33, 34}, {35, 36}, {37, 38}, {39, 40}}}, {{{41, 42}, {43, 44}, {45, 46}, {47, 48}, {49, 50}}, {{51, 52}, {53, 54}, {55, 56}, {57, 58}, {59, 60}}}, {{{61, 62}, {63, 64}, {65, 66}, {67, 68}, {69, 70}}, {{71, 72}, {73, 74}, {75, 76}, {77, 78}, {79, 80}}}, {{{81, 82}, {83, 84}, {85, 86}, {87, 88}, {89, 90}}, {{91, 92}, {93, 94}, {95, 96}, {97, 98}, {99, 100}}}}  , {{{{101, 102}, {103, 104}, {105, 106}, {107, 108}, {109, 110}}, {{111, 112}, {113, 114}, {115, 116}, {117, 118}, {119, 120}}}, {{{121, 122}, {123, 124}, {125, 126}, {127, 128}, {129, 130}}, {{131, 132}, {133, 134}, {135, 136}, {137, 138}, {139, 140}}}, {{{141, 142}, {143, 144}, {145, 146}, {147, 148}, {149, 150}}, {{151, 152}, {153, 154}, {155, 156}, {157, 158}, {159, 160}}}, {{{161, 162}, {163, 164}, {165, 166}, {167, 168}, {169, 170}}, {{171, 172}, {173, 174}, {175, 176}, {177, 178}, {179, 180}}}, {{{181, 182}, {183, 184}, {185, 186}, {187, 188}, {189, 190}}, {{191, 192}, {193, 194}, {195, 196}, {197, 198}, {199, 200}}}},     {{{{201, 202}, {203, 204}, {205, 206}, {207, 208}, {209, 210}}, {{211, 212}, {213, 214}, {215, 216}, {217, 218}, {219, 220}}}, {{{221, 222}, {223, 224}, {225, 226}, {227, 228}, {229, 230}}, {{231, 232}, {233, 234}, {235, 236}, {237, 238}, {239, 240}}}, {{{241, 242}, {243, 244}, {245, 246}, {247, 248}, {249, 250}}, {{251, 252}, {253, 254}, {255, 256}, {257, 258}, {259, 260}}}, {{{261, 262}, {263, 264}, {265, 266}, {267, 268}, {269, 270}}, {{271, 272}, {273, 274}, {275, 276}, {277, 278}, {279, 280}}}, {{{281, 282}, {283, 284}, {285, 286}, {287, 288}, {289, 290}}, {{291, 292}, {293, 294}, {295, 296}, {297, 298}, {299, 300}}}}};

   One_to_Five(dimm , RR , CC, HH,  HHH, HHHH);
   Five_to_One(dimm2 , RR , CC, HH,  HHH, HHHH);

int arr1[3] = {1, 2, 3};
   
int arr2[5] = {4, 5, 6, 7, 8};

concatenate(arr1, arr2);
return 0;
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
   