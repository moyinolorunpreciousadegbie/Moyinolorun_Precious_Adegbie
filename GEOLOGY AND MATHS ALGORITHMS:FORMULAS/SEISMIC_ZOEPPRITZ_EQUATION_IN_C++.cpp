#include <iostream>      //////. ZOEPPRITZ READY TO G0 !!!
using namespace std;
#include <cmath> 
#define N 4

// Function to get cofactor of A[p][q] in temp[][]. n is
// current dimension of A[][]
void getCofactor(double A[N][N], double temp[N][N], int p, int q,
				int n)
{
	int i = 0, j = 0;

	// Looping for each element of the matrix
	
	//for (int row = 0; row < n; row++) { // STYLE 2
	for (int col = 0; col < n; col++) { // STYLE 1
	for (int row = 0; row < n; row++) {
	
			// Copying into temporary matrix only those
			// element which are not in given row and
			// column
	
			if (row != p && col!= q ) {	// STYLE 1
/////////////////////////////////////////////////	
// if ( (row == p) || (col== q ) ) ; //STYLE 2 //
// else{                                       //
/////////////////////////////////////////////////
/////////////////////////////////////////////////
// if ( (row == p) || (col== q ) ) { //STYLE 3 //
// continue; }                                 //
/////////////////////////////////////////////////
//////////////////////////////////////////////////////
// if (! ( (row == p) || (col== q ) )) { // STYLE 4 //
//////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////		 
// if ((row < p || row > p  ) &&  ( col < q  || col > q)){ // STYLE 5
///////////////////////////////////////////////////////////////////
	
		       	temp[i++][j] = A[row][col]; // STYLE 1
				// Row is filled, so increase row index and
				// reset col index
				 if (i == n - 1) {
					i = 0;
					j++;
			// Col is filled, so increase col index and
				// reset row index		
		     //temp[i][j++] = A[row][col]; // STYLE 2

				 // if (j == n - 1) {
				//	j = 0;
				//	i++;
		  }		 
		 }
		}
	  }
}

/* Recursive function for finding determinant of matrix.
n is current dimension of A[][]. */
double determinant(double A[N][N], int n)
{
	double D = 0; // Initialize result

	// Base case : if matrix contains single element
	if (n == 1){
		return A[0][0];}

	double temp[N][N]; // To store cofactors

	// Iterate for each element of first row
	for (int f = 0; f < n; f++) {
		// Getting Cofactor of A[0][f]
       // To store sign multiplier
	int sign=pow(-1,f); // STYLE 1
	//. int sign = 1; // STYLE 2
	// int sign = (f % 2 == 0) ? 1 : -1; // STYLE 3
	// float sign[2]={1,-1}; // STYLE 4
	
		getCofactor(A, temp, 0, f, n);
      D += sign * A[0][f] * determinant(temp, n - 1);  // STYLE 1 & 2 & 3
      // D += sign[f%2] * A[0][f] * determinant(temp, n - 1); // STYLE 4
		// terms are to be added with alternate sign
	//	sign = -sign;  // STYLE 2
	} 
return D;
}

// Function to get adjoint of A[N][N] in adj[N][N].
void adjoint(double A[N][N], double adj[N][N])
{
	if (N == 1) {
		adj[0][0] = 1;return;}
	

	// temp is used to store cofactors of A[][]
 
	double temp[N][N];

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			// Get cofactor of A[i][j]
			getCofactor(A, temp, i, j, N);
          
			// sign of adj[j][i] positive if sum of row
			// and column indexes is even.
			
			 int sign = ((i + j ) % 2 == 0) ? 1 : -1; // STYLE 1
	        //int sign=pow(-1,i+j); // STYLE 2
	       // float sign[2]={1,-1};  // STYLE 3
			// Interchanging rows and columns to get the
			// transpose of the cofactor matrix
	adj[j][i] = (sign) * (determinant(temp, N - 1)); // STYLE 1 & 2
//adj[j][i] = (sign[(i+j)%2]) * (determinant(temp, N - 1)); // STYLE 3
		}
	}
}
// Function to calculate and store inverse, returns false if
// matrix is singular
bool inverse(double A[N][N], double inv[N][N])  // double,0/ bool,true
{
	// Find determinant of A[][]
	double det = determinant(A, N);
	
	// Find adjoint
	double adj[N][N];
	adjoint(A, adj);

	// Find Inverse using formula "inverse(A) =
	// adj(A)/det(A)"
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			inv[i][j] = adj[i][j] / double(det);
}}
	return true;
}
// Generic function to display the matrix. We use it to
// display both adjoin and inverse. adjoin is integer matrix
// and inverse is a float.
template <class T> void display(T A[N][N])
{
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)
			cout << A[i][j] << " ";
		cout << endl;
	}
}

///////////////////////////////////////////////////////////////
#define R1 4 // number of rows in Matrix-1
#define C1 4 // number of columns in Matrix-1
#define R2 4 // number of rows in Matrix-2
#define C2 1 // number of columns in Matrix-2

void mulMat(double A1[][C1], double A2[][C2]) /// C1 C2
{
	double rslt[R1][C2];

	// cout << "Multiplication of given two matrices is:\n";

	for (int i = 0; i < R1; i++) {
		for (int j = 0; j < C2; j++) {
			rslt[i][j] = 0;

			for (int k = 0; k < R2; k++) {
				rslt[i][j] += A1[i][k] * A2[k][j];
			}

			cout << rslt[i][j] << "\t";
		}

		cout << endl;
	}
}
///////////////////////////////////////////

int main()
{


	
  
    // Function call
    if (C1 != R2) {
		cout << "The number of columns in Matrix-1 must "
				"be equal to the number of rows in "
				"Matrix-2"
			<< endl;
		cout << "Please update MACROs according to your "
				"array dimension in #define section"
			<< endl;

		exit(EXIT_FAILURE);
	}


	
    double theta1 = 2.57;
    double theta2 = 2.9;
     double phi1 = 2.57;
    double phi2 = 2.9;
    
    
    double Vp1 = 2.45;
    double Vp2 = 2.5;
    double Vs1 = 2.4;
    double Vs2 = 2.35;
    
    double Rho1 = 2.15;
    double Rho2 = 2.53;
    
double A[N][N] = { {-sin(theta1), -cos(phi1), sin(theta2), cos(phi2)     },
                { cos(theta1),  -sin(phi1), cos(theta2), -sin(phi2)   },
                
{sin(2*theta1), ((Vp1/Vs1)*cos(2*phi1)), 
 ( ( (Rho2*pow(Vs2,2)*Vp1)/(Rho1*pow(Vs1,2)*Vp2) ) * sin(2*theta2) ),
                      ( (Rho2*Vs2*Vp1)/(Rho1*pow(Vs1,2)) ) * cos(2*phi2)},
                      
{-cos(2*phi1), (Vs1/Vp1)*sin(2*phi1), 
  ( (Rho2*Vp2)/(Rho1*Vp1) ) * cos(2*phi2),
                                (-(Rho2*Vs2)/(Rho1*Vp1 )) * sin(2*phi2)}};
                               
                               
                               
                               
double adj[N][N]; // To store adjoint of A[][]
	double inv[N][N]; // To store inverse of A[][]

	cout << "\nThe Adjoint is :\n";
	adjoint(A, adj);
	display(adj);

	cout << "\nThe Inverse is :\n";
	inverse(A, inv);
	display(inv);

    cout << "\nThe Determinant is :\n";
    cout<<determinant(A, N);
    
    cout << "\nThe Zoeppritz is :\n";
    
       //double temp[R1][C1]=   {inverse(A, inv)};  
       //{inverse(A, inv) }= double A1[R1][C1];
       //double A1[R1][C1] =  double temp[R1][C1];
//  double A1[R1][C1]  = inverse(A, inv);
 
 double A2[R2][C2] = {{sin(theta1)},
                     {cos(theta1)},
                     {sin(2*theta1)},
                     {cos(2*phi1)}};
 
 
  // mulMat(A1, A2);              
  // mulMat(inverse(A, inv), A2); ////
   // mulMat( A2, inverse(A, inv)); 
   mulMat(inv, A2); 
	return 0;
}






