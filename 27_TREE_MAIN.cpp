// Implementation of Octree in c++
#include <iostream>
#include <vector>
using namespace std;

/*
#define TopLeftFront 0
#define TopRightFront 1
#define BottomRightFront 2
#define BottomLeftFront 3
#define TopLeftBottom 4
#define TopRightBottom 5
#define BottomRightBack 6
#define BottomLeftBack 7
*/

// tlfz,     ,_1_3z
#define North_West_Surface  0 // tlf->x, tlf->y,tlf->z,          _1_3x,_1_3y, _1_3z   0                   
#define North_Middle_Surface 1 // _1_3x + 1, tlf->y, tlf->z,       _2_3x,_1_3y ,_1_3z  1
#define North_East_Surface   2  // _2_3x + 1, tlf->y, tlf->z,       brb->x , _1_3y ,_1_3z  2
#define Equator_West_Surface  3 // tlf->x, _1_3y + 1, tlf->z,        _1_3x, _2_3y , _1_3z  3
#define Equator_Middle_Surface 4 //  _1_3x + 1, _1_3y + 1, tlf->z,       _2_3x,_2_3y ,_1_3z  4
#define Equator_East_Surface  5 //   _2_3x + 1, _1_3y + 1,tlf->z,       brb->x,_2_3y ,_1_3z  5
#define South_West_Surface   6 //   tlf->x , _2_3y + 1, tlf->z,        _1_3x,brb->y ,_1_3z  6
#define South_Middle_Surface  7 //   _1_3x + 1, _2_3y + 1, tlf->z,        _2_3x, brb->y ,_1_3z  7
#define South_East_Surface    8 //   _2_3x + 1, _2_3y + 1, tlf->z,        brb->x,brb->y ,_1_3z  8
 
//  _1_3z + 1, _2_3z Down1
#define North_West_Down1  9 // tlf->x, tlf->y,_1_3z + 1,          _1_3x,_1_3y, _2_3z   9                  
#define North_Middle_Down1 10 // _1_3x + 1, tlf->y, _1_3z + 1,       _2_3x,_1_3y ,_2_3z  10
#define North_East_Down1   11 // _2_3x + 1, tlf->y, _1_3z + 1,       brb->x , _1_3y ,_2_3z  11
#define Equator_West_Down1  12 //  tlf->x, _1_3y + 1, _1_3z + 1,        _1_3x, _2_3y , _2_3z  12
#define Equator_Middle_Down1 13 //  _1_3x + 1, _1_3y + 1, _1_3z + 1,       _2_3x,_2_3y ,_2_3z  13
#define Equator_East_Down1   14 //  _2_3x + 1, _1_3y + 1,_1_3z + 1,       brb->x,_2_3y ,_2_3z  14
#define South_West_Down1   15 //   tlf->x , _2_3y + 1, _1_3z + 1,        _1_3x,brb->y ,_2_3z  15
#define South_Middle_Down1  16 //   _1_3x + 1, _2_3y + 1, _1_3z + 1,        _2_3x, brb->y ,_2_3z  16
#define South_East_Down1     17 //  _2_3x + 1, _2_3y + 1, _1_3z + 1,        brb->x,brb->y ,_2_3z  17

//    _2_3z + 1, ,brb->z     Down2
#define North_West_Down2  18 //tlf->x, tlf->y,_2_3z + 1,          _1_3x,_1_3y, brb->z    18                   
#define North_Middle_Down2 19 //_1_3x + 1, tlf->y, _2_3z + 1,       _2_3x,_1_3y ,brb->z   19
#define North_East_Down2   20 // _2_3x + 1, tlf->y, _2_3z + 1,       brb->x , _1_3y ,brb->z   20
#define Equator_West_Down2 21 //  tlf->x, _1_3y + 1, _2_3z + 1,        _1_3x, _2_3y , brb->z   21
#define Equator_Middle_Down2 22 // _1_3x + 1, _1_3y + 1, _2_3z + 1,       _2_3x,_2_3y ,brb->z   22
#define Equator_East_Down2   23 //  _2_3x + 1, _1_3y + 1, _2_3z + 1,       brb->x,_2_3y ,brb->z   23
#define South_West_Down2     24 // tlf->x , _2_3y + 1, _2_3z + 1,        _1_3x,brb->y ,brb->z   24
#define South_Middle_Down2  25 //   _1_3x + 1, _2_3y + 1, _2_3z + 1,        _2_3x, brb->y ,brb->z   25
#define South_East_Down2    26 //   _2_3x + 1, _2_3y + 1, _2_3z + 1,        brb->x,brb->y ,brb->z   26


// Structure of a point
struct Point {
	double x;
	double y;
	double z;
	Point()
		: x(-1.0), y(-1.0), z(-1.0)
	{
	}

	Point(double a, double b, double c)
		: x(a), y(b), z(c)
	{
	}
};

// Octree class
class Octree {

	// if point == NULL, node is internal node.
	// if point == (-1, -1, -1), node is empty.
	Point* point;

	// Represent the boundary of the cube
	//Point *topLeftFront, *bottomRightBack;  // OLD
	//vector<Octree*> children;               // OLD
	
	Point *tlf, *brb;    ///////////////////// <<<<<<<<<<<<<
	vector<Octree*> children; // <<<<<<<<<<<<<<<<<<<<
	

public:
	// Constructor
	Octree()
	{
		// To declare empty node
		point = new Point();
	}

	// Constructor with three arguments
	Octree(double x, double y, double z)
	{
		// To declare point node
		point = new Point(x, y, z);
	}

	// Constructor with six arguments
	Octree(double x1, double y1, double z1, double x2, double y2, double z2)
	{
		// This use to construct Octree
		// with boundaries defined
		if (x2 < x1
			|| y2 < y1
			|| z2 < z1) {
			cout << "boundary points are not valid" << endl;
			return;
		}

		point = nullptr;
		//topLeftFront
		tlf ///  <<<<<<<<<<,
			= new Point(x1, y1, z1);
		//bottomRightBack
		brb  /// <<<<<<<<<<<<<<
			= new Point(x2, y2, z2);

		// Assigning null to the children
		//children.assign(8, nullptr);
		children.assign(27, nullptr);  // <<<<<<<<<<<<<<<<<<<<<<
		//for (int i = TopLeftFront;
			//i <= BottomLeftBack;
			//++i)
			
			 		for (int i = North_West_Surface; i <= South_East_Down2;  ++i)     // <<<<<<<<<<<<<<<<<<<<<,,
		
			children[i] = new Octree();
	}

	// Function to insert a point in the octree
	void insert(double x,                                                         ///////////////////////////////////////////////////
				double y,
				double z)
	{ //int _2_3p1;

		// If the point already exists in the octree
		if (find(x, y, z)) {
			cout << "Point already exist in the tree" << endl;
			return;
		}

		/* If the point is out of bounds
		if (x < topLeftFront->x
			|| x > bottomRightBack->x
			|| y < topLeftFront->y
			|| y > bottomRightBack->y
			|| z < topLeftFront->z
			|| z > bottomRightBack->z) {
			cout << "Point is out of bound" << endl;
			return;
		*/
			
		if (x < tlf->x || x > brb->x || y < tlf->y || y > brb->y || z < tlf->z || z > brb->z) {
						cout << "Point is out of bound" << endl;
						//cout << x << y << z << endl;
						//cout << tlf->x << brb->x << "||"  << tlf->y << brb->y << "||" << tlf->z << brb->z <<  endl;
						return;
		}

		/* Binary search to insert the point
		int midx = (topLeftFront->x
					+ bottomRightBack->x)
				/ 2;
		int midy = (topLeftFront->y
					+ bottomRightBack->y)
				/ 2;
		int midz = (topLeftFront->z
					+ bottomRightBack->z)
				/ 2;
		

		int pos = -1;
		
		*/
		
		
		
		double _1_3x = (tlf->x
		+ brb->x)
		/ 3.0 ;
		
		double _2_3x = ((tlf->x
		+ brb->x)
		/ 3.0 ) * 2.0 ;
		
		
		
		double _1_3y = (tlf->y
		+ brb->y)
		/ 3.0 ;
		
		double _2_3y = ((tlf->y
		+ brb->y)
		/ 3.0 ) * 2.0 ;
		
		
		
		double _1_3z = (tlf->z
		+ brb->z)
		/ 3.0 ;
		
		double _2_3z = ((tlf->z
		+ brb->z)
		/ 3.0 ) * 2.0 ;
		
		int pos = -1.0;
		
		
		
		
		
		//$$$$$$$$$$$$$$$	  // tlfz,     ,_1_3z
		//#define North_West_Surface  tlfx, tlfy,tlfz,          _1_3x,_1_3y, _1_3z   0                   
		if (  x <= _1_3x) {
			if ( y <= _1_3y) {
				if ( z <= _1_3z)
				pos = North_West_Surface; }}
			
			//#define North_Middle_Surface   _1_3x + 1, tlfy, tlfz,       _2_3x,_1_3y ,_1_3z       1
			if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
				if (  y <= _1_3y) {
					if ( z <= _1_3z)
					pos = North_Middle_Surface; }}
				
				//#define North_East_Surface    _2_3x + 1, tlfy, tlfz,       brbx,_1_3y ,_1_3z  2
				if ( _2_3x + 0.000000000000001 <= x ) {
					if (  y <= _1_3y) {
						if (  z <= _1_3z)
						pos = North_East_Surface; }}
					
					//#define Equator_West_Surface   tlfx, _1_3y + 1, tlfz,        _1_3x,_2_3y ,_1_3z  3
					if (  x <= _1_3x) {
						if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
							if (  z <= _1_3z)
							pos = Equator_West_Surface; }}
						
						//#define Equator_Middle_Surface  _1_3x + 1, _1_3y + 1, tlfz,       _2_3x,_2_3y ,_1_3z  4
						if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
							if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
								if (  z <= _1_3z)
								pos = Equator_Middle_Surface; }}
							
							
							//#define Equator_East_Surface     _2_3x + 1, _1_3y + 1,tlfz,       brbx,_2_3y ,_1_3z  5
							if ( _2_3x + 0.000000000000001 <= x  ) {
								if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
									if (  z <= _1_3z)
									pos = Equator_East_Surface; }}
								
								//#define South_West_Surface      tlfx, _2_3y + 1, tlfz,        _1_3x,brby ,_1_3z  6
								if (  x <= _1_3x) {
									if (_2_3y + 0.000000000000001 <= y  ) {
										if ( z <= _1_3z)
										pos = South_West_Surface; }}
									
									//#define South_Middle_Surface     _1_3x + 1, _2_3y + 1, tlfz,        _2_3x,brby ,_1_3z  7
									if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
										if (_2_3y + 0.000000000000001 <= y ) {
											if (z <= _1_3z)
											pos = South_Middle_Surface; }}
										
										//#define South_East_Surface       _2_3x + 1, _2_3y + 1, tlfz,        brbx,brby ,_1_3z  8
										if ( _2_3x + 0.000000000000001 <= x ) {
											if (_2_3y + 0.000000000000001 <= y ) {
												if ( z <= _1_3z)
												pos = South_East_Surface; }}
											
											
											//$$$$$$$$$$$$$$$$$  //  ( _1_3z + 1 <= z <=  _2_3z  )        Down1
											
											//#define North_West_Down1  tlfx, tlfy,tlfz,          _1_3x,_1_3y, _1_3z   0                   
											if ( x <= _1_3x) {
												if ( y <= _1_3y) {
													if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
													pos = North_West_Down1; }}
												
												//#define North_Middle_Down1   _1_3x + 1, tlfy, tlfz,       _2_3x,_1_3y ,_1_3z       1
												if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
													if ( y <= _1_3y) {
														if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
														pos = North_Middle_Down1; }}
													
													//#define North_East_Down1    _2_3x + 1, tlfy, tlfz,       brbx,_1_3y ,_1_3z  2
													if ( _2_3x + 0.000000000000001 <= x ) {
														if (  y <= _1_3y) {
															if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
															pos = North_East_Down1; }}
														
														//#define Equator_West_Down1   tlfx, _1_3y + 1, tlfz,        _1_3x,_2_3y ,_1_3z  3
														if (  x <= _1_3x) {
															if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
																if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
																pos = Equator_West_Down1; }}
															
															//#define Equator_Middle_Down1  _1_3x + 1, _1_3y + 1, tlfz,       _2_3x,_2_3y ,_1_3z  4
															if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
																if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
																	if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
																	pos = Equator_Middle_Down1; }}
																
																
																//#define Equator_East_Down1     _2_3x + 1, _1_3y + 1,tlfz,       brbx,_2_3y ,_1_3z  5
																if ( _2_3x + 0.000000000000001 <= x  ) {
																	if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
																		if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
																		pos = Equator_East_Down1; }}
																	
																	//#define South_West_Down1      tlfx, _2_3y + 1, tlfz,        _1_3x,brby ,_1_3z  6
																	if ( x <= _1_3x) {
																		if (_2_3y + 0.000000000000001 <= y ) {
																			if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
																			pos = South_West_Down1; }}
																		
																		//#define South_Middle_Down1     _1_3x + 1, _2_3y + 1, tlfz,        _2_3x,brby ,_1_3z  7
																		if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
																			if (_2_3y + 0.000000000000001 <= y ) {
																				if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
																				pos = South_Middle_Down1; }}
																			
																			//#define South_East_Down1       _2_3x + 1, _2_3y + 1, tlfz,        brbx,brby ,_1_3z  8
																			if ( _2_3x + 0.000000000000001 <= x  ) {
																				if (_2_3y + 0.000000000000001 <= y ) {
																					if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
																					pos = South_East_Down1; }}
																				
																				
																				
																				
																				
																				//$$$$$$$$$$$$$$$$	//    ( _2_3z + 1 <= z <=  brbz )  Down2
																				//#define North_West_Down2  tlfx, tlfy,tlfz,          _1_3x,_1_3y, _1_3z   0                   
																				if ( x <= _1_3x) {
																					if ( y <= _1_3y) {
																						if ( _2_3z + 0.000000000000001 <= z  )
																						pos = North_West_Down2; }}
																					
																					//#define North_Middle_Down2   _1_3x + 1, tlfy, tlfz,       _2_3x,_1_3y ,_1_3z       1
																					if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
																						if ( y <= _1_3y) {
																							if ( _2_3z + 0.000000000000001 <= z )
																							pos = North_Middle_Down2; }}
																						
																						//#define North_East_Down2    _2_3x + 1, tlfy, tlfz,       brbx,_1_3y ,_1_3z  2
																						if ( _2_3x + 0.000000000000001 <= x ) {
																							if ( y <= _1_3y) {
																								if ( _2_3z + 0.000000000000001 <= z  )
																								pos = North_East_Down2; }}
																							
																							//#define Equator_West_Down2   tlfx, _1_3y + 1, tlfz,        _1_3x,_2_3y ,_1_3z  3
																							if (  x <= _1_3x) {
																								if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
																									if ( _2_3z + 0.000000000000001 <= z  )
																									pos = Equator_West_Down2; }}
																								
																								//#define Equator_Middle_Down2  _1_3x + 1, _1_3y + 1, tlfz,       _2_3x,_2_3y ,_1_3z  4
																								if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
																									if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
																										if ( _2_3z + 0.000000000000001 <= z  )
																										pos = Equator_Middle_Down2; }}
																									
																									
																									//#define Equator_East_Down2     _2_3x + 1, _1_3y + 1,tlfz,       brbx,_2_3y ,_1_3z  5
																									if ( _2_3x + 0.000000000000001 <= x ) {
																										if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
																											if ( _2_3z + 0.000000000000001 <= z  )
																											pos = Equator_East_Down2; }}
																										
																										//#define South_West_Down2      tlfx, _2_3y + 1, tlfz,        _1_3x,brby ,_1_3z  6
																										if (  x <= _1_3x) {
																											if (_2_3y + 0.000000000000001 <= y ) {
																												if ( _2_3z + 0.000000000000001 <= z )
																												pos = South_West_Down2; }}
																											
																											//#define South_Middle_Down2     _1_3x + 1, _2_3y + 1, tlfz,        _2_3x,brby ,_1_3z  7
																											if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
																												if (_2_3y + 0.000000000000001 <= y ) {
																													if ( _2_3z + 0.000000000000001 <= z )
																													pos = South_Middle_Down2; }}
																												
																												//#define South_East_Down2       _2_3x + 1, _2_3y + 1, tlfz,        brbx,brby ,_1_3z  8
																												if ( _2_3x + 0.000000000000001 <= x ) {
																													if (_2_3y + 0.000000000000001 <= y ) {
																														if ( _2_3z + 0.000000000000001 <= z  )
																														pos = South_East_Down2; }}
																													
//////////////////////////////////
		
		
		
			// If an internal node is encountered
			if (children[pos]->point == nullptr) {
			children[pos]->insert(x, y, z);
			return;
			}
			
			// If an empty node is encountered
			else if (children[pos]->point->x == -1.0) {
			delete children[pos];
			children[pos] = new Octree(x, y, z);
			return;
			}
			else {
			double x_ = children[pos]->point->x;  ////  <<<<<<<<<<<<<<<<<<<<<<<<<<<<,
			double y_ = children[pos]->point->y;
			double z_ = children[pos]->point->z;
			delete children[pos];
			children[pos] = nullptr;
		
		// if (pos == TopLeftFront) {    children[pos] = new Octree(        ); }
		
		// tlfz,     ,_1_3z
		//#define North_West_Surface   tlf->x, tlf->y,tlf->z,          _1_3x,_1_3y, _1_3z   0  
		if (pos == North_West_Surface) {    children[pos] = new Octree(   tlf->x, tlf->y,tlf->z,          _1_3x,_1_3y, _1_3z   ); }
		
		//#define North_Middle_Surface  _1_3x + 1, tlf->y, tlf->z,       _2_3x,_1_3y ,_1_3z  1
		else if (pos == North_Middle_Surface) {    children[pos] = new Octree(   _1_3x + 0.000000000000001, tlf->y, tlf->z,       _2_3x,_1_3y ,_1_3z   ); }
		
		//#define North_East_Surface     _2_3x + 1, tlf->y, tlf->z,       brb->x , _1_3y ,_1_3z  2
		else if (pos == North_East_Surface) {    children[pos] = new Octree(   _2_3x + 0.000000000000001, tlf->y, tlf->z,       brb->x , _1_3y ,_1_3z  ); }
		
		//#define Equator_West_Surface   tlf->x, _1_3y + 1, tlf->z,        _1_3x, _2_3y , _1_3z  3
		else if (pos == Equator_West_Surface) {    children[pos] = new Octree(  tlf->x, _1_3y + 0.000000000000001, tlf->z,        _1_3x, _2_3y , _1_3z   ); }
		
		//#define Equator_Middle_Surface  _1_3x + 1, _1_3y + 1, tlf->z,       _2_3x,_2_3y ,_1_3z  4
		else if (pos == Equator_Middle_Surface) {    children[pos] = new Octree(   _1_3x + 0.000000000000001, _1_3y + 0.000000000000001, tlf->z,       _2_3x,_2_3y ,_1_3z  ); }
		
		//#define Equator_East_Surface     _2_3x + 1, _1_3y + 1,tlf->z,       brb->x,_2_3y ,_1_3z  5
		else if (pos == Equator_East_Surface) {    children[pos] = new Octree(   _2_3x + 0.000000000000001, _1_3y + 0.000000000000001,tlf->z,       brb->x,_2_3y ,_1_3z  ); }
		
		//#define South_West_Surface      tlf->x , _2_3y + 1, tlf->z,        _1_3x,brb->y ,_1_3z  6
		else if (pos == South_West_Surface) {    children[pos] = new Octree(     tlf->x , _2_3y + 0.000000000000001, tlf->z,        _1_3x,brb->y ,_1_3z   ); }
		
		//#define South_Middle_Surface     _1_3x + 1, _2_3y + 1, tlf->z,        _2_3x, brb->y ,_1_3z  7
		else if (pos == South_Middle_Surface) {    children[pos] = new Octree(     _1_3x + 0.000000000000001, _2_3y + 0.000000000000001, tlf->z,        _2_3x, brb->y ,_1_3z   ); }
		
		//#define South_East_Surface       _2_3x + 1, _2_3y + 1, tlf->z,        brb->x,brb->y ,_1_3z  8
		else if (pos == South_East_Surface) {    children[pos] = new Octree(   _2_3x + 0.000000000000001, _2_3y + 0.000000000000001, tlf->z,        brb->x,brb->y ,_1_3z   ); }
		
		
		
		//  _1_3z + 1, _2_3z Down1
		//#define North_West_Down1  tlf->x, tlf->y,_1_3z + 1,          _1_3x,_1_3y, _2_3z   9   
		else if (pos == North_West_Down1) {    children[pos] = new Octree(    tlf->x, tlf->y,_1_3z + 0.000000000000001,          _1_3x,_1_3y, _2_3z ); }
		
		//#define North_Middle_Down1 _1_3x + 1, tlf->y, _1_3z + 1,       _2_3x,_1_3y ,_2_3z  10
		else if (pos == North_Middle_Down1) {    children[pos] = new Octree(   _1_3x + 0.000000000000001, tlf->y, _1_3z + 0.000000000000001,       _2_3x,_1_3y ,_2_3z   ); }
		
		//#define North_East_Down1   _2_3x + 1, tlf->y, _1_3z + 1,       brb->x , _1_3y ,_2_3z  11
		else if (pos == North_East_Down1) {    children[pos] = new Octree(   _2_3x + 0.000000000000001, tlf->y, _1_3z + 0.000000000000001,       brb->x , _1_3y ,_2_3z   ); }
		
		//#define Equator_West_Down1   tlf->x, _1_3y + 1, _1_3z + 1,        _1_3x, _2_3y , _2_3z  12
		else if (pos == Equator_West_Down1) {    children[pos] = new Octree(    tlf->x, _1_3y + 0.000000000000001, _1_3z + 0.000000000000001,        _1_3x, _2_3y , _2_3z ); }
		
		//#define Equator_Middle_Down1  _1_3x + 1, _1_3y + 1, _1_3z + 1,       _2_3x,_2_3y ,_2_3z  13
		else if (pos == Equator_Middle_Down1) {    children[pos] = new Octree(   _1_3x + 0.000000000000001, _1_3y + 0.000000000000001, _1_3z + 0.000000000000001,       _2_3x,_2_3y ,_2_3z  ); }
		
		//#define Equator_East_Down1     _2_3x + 1, _1_3y + 1,_1_3z + 1,       brb->x,_2_3y ,_2_3z  14
		else if (pos == Equator_East_Down1) {    children[pos] = new Octree(  _2_3x + 0.000000000000001, _1_3y + 0.000000000000001,_1_3z + 0.000000000000001,       brb->x,_2_3y ,_2_3z    ); }
		
		//#define South_West_Down1      tlf->x , _2_3y + 1, _1_3z + 1,        _1_3x,brb->y ,_2_3z  15
		else if (pos == South_West_Down1) {    children[pos] = new Octree(   tlf->x , _2_3y + 0.000000000000001, _1_3z + 0.000000000000001,        _1_3x,brb->y ,_2_3z  ); }
		
		//#define South_Middle_Down1     _1_3x + 1, _2_3y + 1, _1_3z + 1,        _2_3x, brb->y ,_2_3z  16
		else if (pos == South_Middle_Down1) {    children[pos] = new Octree(   _1_3x + 0.000000000000001, _2_3y + 0.000000000000001, _1_3z + 0.000000000000001,        _2_3x, brb->y ,_2_3z  ); }
		
		//#define South_East_Down1       _2_3x + 1, _2_3y + 1, _1_3z + 1,        brb->x,brb->y ,_2_3z  17
		else if (pos == South_East_Down1) {    children[pos] = new Octree(   _2_3x + 0.000000000000001, _2_3y + 0.000000000000001, _1_3z + 0.000000000000001,        brb->x,brb->y ,_2_3z     ); }
		
		
		
		//    _2_3z + 1, ,brb->z     Down2
		//#define North_West_Down2  tlf->x, tlf->y,_2_3z + 1,          _1_3x,_1_3y, brb->z    18 
		else if (pos == North_West_Down2) {    children[pos] = new Octree(   tlf->x, tlf->y,_2_3z + 0.000000000000001,          _1_3x,_1_3y, brb->z   ); }
		
		//#define North_Middle_Down2 _1_3x + 1, tlf->y, _2_3z + 1,       _2_3x,_1_3y ,brb->z   19
		else if (pos == North_Middle_Down2) {    children[pos] = new Octree(   _1_3x + 0.000000000000001, tlf->y, _2_3z + 0.000000000000001,       _2_3x,_1_3y ,brb->z   ); }
		
		//#define North_East_Down2    _2_3x + 1, tlf->y, _2_3z + 1,       brb->x , _1_3y ,brb->z   20
		else if (pos == North_East_Down2) {    children[pos] = new Octree(   _2_3x + 0.000000000000001, tlf->y, _2_3z + 0.000000000000001,       brb->x , _1_3y ,brb->z   ); }
		
		//#define Equator_West_Down2   tlf->x, _1_3y + 1, _2_3z + 1,        _1_3x, _2_3y , brb->z   21
		else if (pos == Equator_West_Down2) {    children[pos] = new Octree(  tlf->x, _1_3y + 0.000000000000001, _2_3z + 0.000000000000001,        _1_3x, _2_3y , brb->z   ); }
		
		//#define Equator_Middle_Down2  _1_3x + 1, _1_3y + 1, _2_3z + 1,       _2_3x,_2_3y ,brb->z   22
		else if (pos == Equator_Middle_Down2) {    children[pos] = new Octree(    _1_3x + 0.000000000000001, _1_3y + 0.000000000000001, _2_3z + 0.000000000000001,       _2_3x,_2_3y ,brb->z ); }
		
		//#define Equator_East_Down2     _2_3x + 1, _1_3y + 1, _2_3z + 1,       brb->x,_2_3y ,brb->z   23
		else if (pos == Equator_East_Down2) {    children[pos] = new Octree(   _2_3x + 0.000000000000001, _1_3y + 0.000000000000001, _2_3z + 0.000000000000001,       brb->x,_2_3y ,brb->z   ); }
		
		//#define South_West_Down2      tlf->x , _2_3y + 1, _2_3z + 1,        _1_3x,brb->y ,brb->z   24
		else if (pos == South_West_Down2) {    children[pos] = new Octree( tlf->x , _2_3y + 0.000000000000001, _2_3z + 0.000000000000001,        _1_3x,brb->y ,brb->z      ); }
		
		//#define South_Middle_Down2     _1_3x + 1, _2_3y + 1, _2_3z + 1,        _2_3x, brb->y ,brb->z   25
		else if (pos == South_Middle_Down2) {    children[pos] = new Octree(   _1_3x + 0.000000000000001, _2_3y + 0.000000000000001, _2_3z + 0.000000000000001,        _2_3x, brb->y ,brb->z  ); }
		
		//#define South_East_Down2       _2_3x + 1, _2_3y + 1, _2_3z + 1,        brb->x,brb->y ,brb->z   26
		else if (pos == South_East_Down2) {    children[pos] = new Octree(   _2_3x + 0.000000000000001, _2_3y + 0.000000000000001, _2_3z + 0.000000000000001,        brb->x,brb->y ,brb->z   ); }

		

		/* Checking the octant of 
		// the point
		if (x <= midx) {
			if (y <= midy) {
				if (z <= midz)
					pos = TopLeftFront;
				else
					pos = TopLeftBottom;
			}
			else {
				if (z <= midz)
					pos = BottomLeftFront;
				else
					pos = BottomLeftBack;
			}
		}
		else {
			if (y <= midy) {
				if (z <= midz)
					pos = TopRightFront;
				else
					pos = TopRightBottom;
			}
			else {
				if (z <= midz)
					pos = BottomRightFront;
				else
					pos = BottomRightBack;
			}
		}
			*/

		/* If an internal node is encountered
		if (children[pos]->point == nullptr) {
			children[pos]->insert(x, y, z);
			return;
		}

		// If an empty node is encountered
		else if (children[pos]->point->x == -1) {
			delete children[pos];
			children[pos] = new Octree(x, y, z);
			return;
		}
		else {
			int x_ = children[pos]->point->x,
				y_ = children[pos]->point->y,
				z_ = children[pos]->point->z;
			delete children[pos];
			children[pos] = nullptr;
			if (pos == TopLeftFront) {
				children[pos] = new Octree(topLeftFront->x,
										topLeftFront->y,
										topLeftFront->z,
										midx,
										midy,
										midz);
			}

			else if (pos == TopRightFront) {
				children[pos] = new Octree(midx + 1,
										topLeftFront->y,
										topLeftFront->z,
										bottomRightBack->x,
										midy,
										midz);
			}
			else if (pos == BottomRightFront) {
				children[pos] = new Octree(midx + 1,
										midy + 1,
										topLeftFront->z,
										bottomRightBack->x,
										bottomRightBack->y,
										midz);
			}
			else if (pos == BottomLeftFront) {
				children[pos] = new Octree(topLeftFront->x,
										midy + 1,
										topLeftFront->z,
										midx,
										bottomRightBack->y,
										midz);
			}
			else if (pos == TopLeftBottom) {
				children[pos] = new Octree(topLeftFront->x,
										topLeftFront->y,
										midz + 1,
										midx,
										midy,
										bottomRightBack->z);
			} 
			else if (pos == TopRightBottom) {
				children[pos] = new Octree(midx + 1,
										topLeftFront->y,
										midz + 1,
										bottomRightBack->x,
										midy,
										bottomRightBack->z);
			}
			else if (pos == BottomRightBack) {
				children[pos] = new Octree(midx + 1,
										midy + 1,
										midz + 1,
										bottomRightBack->x,
										bottomRightBack->y,
										bottomRightBack->z);
			}
			else if (pos == BottomLeftBack) {
				children[pos] = new Octree(topLeftFront->x,
										midy + 1,
										midz + 1,
										midx,
										bottomRightBack->y,
										bottomRightBack->z);
			}
			
			
			*/
			children[pos]->insert(x_, y_, z_);
			children[pos]->insert(x, y, z);
		}
	}

	// Function that returns true if the point
	// (x, y, z) exists in the octree                      ///////////////////////////////////////////////////
	bool find(double x, double y, double z)
	{
		/* If point is out of bound
		if (x < topLeftFront->x
			|| x > bottomRightBack->x
			|| y < topLeftFront->y
			|| y > bottomRightBack->y
			|| z < topLeftFront->z
			|| z > bottomRightBack->z)
			return 0;
		*/
		
		if (x < tlf->x || x > brb->x || y < tlf->y || y > brb->y || z < tlf->z || z > brb->z) return 0;

		// Otherwise perform binary search
		// for each ordinate
		double _1_3x = (tlf->x
			+ brb->x)
		/ 3.0 ;
		
		double _2_3x = ((tlf->x
			+ brb->x)
		/ 3.0 ) * 2.0 ;
		
		
		
		double _1_3y = (tlf->y
			+ brb->y)
		/ 3.0 ;
		
		double _2_3y = ((tlf->y
			+ brb->y)
		/ 3.0 ) * 2.0 ;
		
		
		
		double _1_3z = (tlf->z
			+ brb->z)
		/ 3.0 ;
		
		double _2_3z = ((tlf->z
			+ brb->z)
		/ 3.0 ) * 2.0 ;
		
		int pos = -1.0;
		
		
		
		//$$$$$$$$$$$$$$$	  // tlfz,     ,_1_3z
		//#define North_West_Surface  tlfx, tlfy,tlfz,          _1_3x,_1_3y, _1_3z   0                   
		if (  x <= _1_3x) {
			if ( y <= _1_3y) {
				if ( z <= _1_3z)
				pos = North_West_Surface; }}
			
			//#define North_Middle_Surface   _1_3x + 1, tlfy, tlfz,       _2_3x,_1_3y ,_1_3z       1
			if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
				if (  y <= _1_3y) {
					if ( z <= _1_3z)
					pos = North_Middle_Surface; }}
				
				//#define North_East_Surface    _2_3x + 1, tlfy, tlfz,       brbx,_1_3y ,_1_3z  2
				if ( _2_3x + 0.000000000000001 <= x ) {
					if (  y <= _1_3y) {
						if (  z <= _1_3z)
						pos = North_East_Surface; }}
					
					//#define Equator_West_Surface   tlfx, _1_3y + 1, tlfz,        _1_3x,_2_3y ,_1_3z  3
					if (  x <= _1_3x) {
						if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
							if (  z <= _1_3z)
							pos = Equator_West_Surface; }}
						
						//#define Equator_Middle_Surface  _1_3x + 1, _1_3y + 1, tlfz,       _2_3x,_2_3y ,_1_3z  4
						if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
							if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
								if (  z <= _1_3z)
								pos = Equator_Middle_Surface; }}
							
							
							//#define Equator_East_Surface     _2_3x + 1, _1_3y + 1,tlfz,       brbx,_2_3y ,_1_3z  5
							if ( _2_3x + 0.000000000000001 <= x  ) {
								if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
									if (  z <= _1_3z)
									pos = Equator_East_Surface; }}
								
								//#define South_West_Surface      tlfx, _2_3y + 1, tlfz,        _1_3x,brby ,_1_3z  6
								if (  x <= _1_3x) {
									if (_2_3y + 0.000000000000001 <= y  ) {
										if ( z <= _1_3z)
										pos = South_West_Surface; }}
									
									//#define South_Middle_Surface     _1_3x + 1, _2_3y + 1, tlfz,        _2_3x,brby ,_1_3z  7
									if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
										if (_2_3y + 0.000000000000001 <= y ) {
											if (z <= _1_3z)
											pos = South_Middle_Surface; }}
										
										//#define South_East_Surface       _2_3x + 1, _2_3y + 1, tlfz,        brbx,brby ,_1_3z  8
										if ( _2_3x + 0.000000000000001 <= x ) {
											if (_2_3y + 0.000000000000001 <= y ) {
												if ( z <= _1_3z)
												pos = South_East_Surface; }}
											
											
											//$$$$$$$$$$$$$$$$$  //  ( _1_3z + 1 <= z <=  _2_3z  )        Down1
											
											//#define North_West_Down1  tlfx, tlfy,tlfz,          _1_3x,_1_3y, _1_3z   0                   
											if ( x <= _1_3x) {
												if ( y <= _1_3y) {
													if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
													pos = North_West_Down1; }}
												
												//#define North_Middle_Down1   _1_3x + 1, tlfy, tlfz,       _2_3x,_1_3y ,_1_3z       1
												if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
													if ( y <= _1_3y) {
														if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
														pos = North_Middle_Down1; }}
													
													//#define North_East_Down1    _2_3x + 1, tlfy, tlfz,       brbx,_1_3y ,_1_3z  2
													if ( _2_3x + 0.000000000000001 <= x ) {
														if (  y <= _1_3y) {
															if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
															pos = North_East_Down1; }}
														
														//#define Equator_West_Down1   tlfx, _1_3y + 1, tlfz,        _1_3x,_2_3y ,_1_3z  3
														if (  x <= _1_3x) {
															if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
																if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
																pos = Equator_West_Down1; }}
															
															//#define Equator_Middle_Down1  _1_3x + 1, _1_3y + 1, tlfz,       _2_3x,_2_3y ,_1_3z  4
															if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
																if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
																	if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
																	pos = Equator_Middle_Down1; }}
																
																
																//#define Equator_East_Down1     _2_3x + 1, _1_3y + 1,tlfz,       brbx,_2_3y ,_1_3z  5
																if ( _2_3x + 0.000000000000001 <= x  ) {
																	if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
																		if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
																		pos = Equator_East_Down1; }}
																	
																	//#define South_West_Down1      tlfx, _2_3y + 1, tlfz,        _1_3x,brby ,_1_3z  6
																	if ( x <= _1_3x) {
																		if (_2_3y + 0.000000000000001 <= y ) {
																			if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
																			pos = South_West_Down1; }}
																		
																		//#define South_Middle_Down1     _1_3x + 1, _2_3y + 1, tlfz,        _2_3x,brby ,_1_3z  7
																		if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
																			if (_2_3y + 0.000000000000001 <= y ) {
																				if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
																				pos = South_Middle_Down1; }}
																			
																			//#define South_East_Down1       _2_3x + 1, _2_3y + 1, tlfz,        brbx,brby ,_1_3z  8
																			if ( _2_3x + 0.000000000000001 <= x  ) {
																				if (_2_3y + 0.000000000000001 <= y ) {
																					if ( _1_3z + 0.000000000000001 <= z <=  _2_3z  )
																					pos = South_East_Down1; }}
																				
																				
																				
																				
																				
																				//$$$$$$$$$$$$$$$$	//    ( _2_3z + 1 <= z <=  brbz )  Down2
																				//#define North_West_Down2  tlfx, tlfy,tlfz,          _1_3x,_1_3y, _1_3z   0                   
																				if ( x <= _1_3x) {
																					if ( y <= _1_3y) {
																						if ( _2_3z + 0.000000000000001 <= z  )
																						pos = North_West_Down2; }}
																					
																					//#define North_Middle_Down2   _1_3x + 1, tlfy, tlfz,       _2_3x,_1_3y ,_1_3z       1
																					if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
																						if ( y <= _1_3y) {
																							if ( _2_3z + 0.000000000000001 <= z )
																							pos = North_Middle_Down2; }}
																						
																						//#define North_East_Down2    _2_3x + 1, tlfy, tlfz,       brbx,_1_3y ,_1_3z  2
																						if ( _2_3x + 0.000000000000001 <= x ) {
																							if ( y <= _1_3y) {
																								if ( _2_3z + 0.000000000000001 <= z  )
																								pos = North_East_Down2; }}
																							
																							//#define Equator_West_Down2   tlfx, _1_3y + 1, tlfz,        _1_3x,_2_3y ,_1_3z  3
																							if (  x <= _1_3x) {
																								if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
																									if ( _2_3z + 0.000000000000001 <= z  )
																									pos = Equator_West_Down2; }}
																								
																								//#define Equator_Middle_Down2  _1_3x + 1, _1_3y + 1, tlfz,       _2_3x,_2_3y ,_1_3z  4
																								if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
																									if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
																										if ( _2_3z + 0.000000000000001 <= z  )
																										pos = Equator_Middle_Down2; }}
																									
																									
																									//#define Equator_East_Down2     _2_3x + 1, _1_3y + 1,tlfz,       brbx,_2_3y ,_1_3z  5
																									if ( _2_3x + 0.000000000000001 <= x ) {
																										if (_1_3y + 0.000000000000001 <= y <= _2_3y) {
																											if ( _2_3z + 0.000000000000001 <= z  )
																											pos = Equator_East_Down2; }}
																										
																										//#define South_West_Down2      tlfx, _2_3y + 1, tlfz,        _1_3x,brby ,_1_3z  6
																										if (  x <= _1_3x) {
																											if (_2_3y + 0.000000000000001 <= y ) {
																												if ( _2_3z + 0.000000000000001 <= z )
																												pos = South_West_Down2; }}
																											
																											//#define South_Middle_Down2     _1_3x + 1, _2_3y + 1, tlfz,        _2_3x,brby ,_1_3z  7
																											if ( _1_3x + 0.000000000000001 <= x <= _2_3x) {
																												if (_2_3y + 0.000000000000001 <= y ) {
																													if ( _2_3z + 0.000000000000001 <= z )
																													pos = South_Middle_Down2; }}
																												
																												//#define South_East_Down2       _2_3x + 1, _2_3y + 1, tlfz,        brbx,brby ,_1_3z  8
																												if ( _2_3x + 0.000000000000001 <= x ) {
																													if (_2_3y + 0.000000000000001 <= y ) {
																														if ( _2_3z + 0.000000000000001 <= z  )
																														pos = South_East_Down2; }}


		// If an internal node is encountered
		if (children[pos]->point == nullptr) {
			return children[pos]->find(x, y, z);
		}

		// If an empty node is encountered
		else if (children[pos]->point->x == -1.0) {
			return 0;
		}
		else {

			// If node is found with
			// the given value
			if (x == children[pos]->point->x
				&& y == children[pos]->point->y
				&& z == children[pos]->point->z)
				return 1;
		}
		return 0;
	}
};

// Driver code
int main()                                                 ///////////////////////////////////////////////////
{
	Octree tree(0, 0, 0, 5, 5, 5);

	tree.insert(1, 2, 3);
	tree.insert(1, 2, 3);  // Point already exist in the tree
	tree.insert(6, 5, 5);  // Point is out of bound

	cout << (tree.find(1, 2, 3)    // Found
				? "Found\n"
				: "Not Found\n");

	cout << (tree.find(3, 4, 4)      // Not Found
				? "Found\n"
				: "Not Found\n");
	tree.insert(3, 4, 4);

	cout << (tree.find(3, 4, 4)    // Found
		? "Found\n"
		: "Not Found\n");
	

	return 0;
}
																											
																											
	// 0.000000000000001    tree.insert(1, 5, 4);
	
	
	