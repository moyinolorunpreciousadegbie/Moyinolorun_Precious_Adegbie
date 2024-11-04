// Implementation of Octree in c++
#include <iostream>
#include <vector>
using namespace std;

#define TopLeftFront 0
#define TopRightFront 1
#define BottomRightFront 2
#define BottomLeftFront 3
#define TopLeftBottom 4
#define TopRightBottom 5
#define BottomRightBack 6
#define BottomLeftBack 7


#define North_West_Surface  tlfx, tlfy,tlfz,          _1_3x,_1_3y, _1_3z   0                    // tlfz,     ,_1_3z
#define North_Middle_Surface _1_3xp1, tlfy, tlfz,       _2_3x,_1_3y ,_1_3z  1
#define North_East_Surface    _2_3xp1, tlfy, tlfz,       brbx,_1_3y ,_1_3z  2
#define Equator_West_Surface   tlfx, _1_3yp1, tlfz,        _1_3x,_2_3y ,_1_3z  3
#define Equator_Middle_Surface  _1_3xp1, _1_3yp1, tlfz,       _2_3x,_2_3y ,_1_3z  4
#define Equator_East_Surface     _2_3xp1, _1_3yp1,tlfz,       brbx,_2_3y ,_1_3z  5
#define South_West_Surface      tlfx, _2_3yp1, tlfz,        _1_3x,brby ,_1_3z  6
#define South_Middle_Surface     _1_3xp1, _2_3yp1, tlfz,        _2_3x,brby ,_1_3z  7
#define South_East_Surface       _2_3xp1, _2_3yp1, tlfz,        brbx,brby ,_1_3z  8

#define North_West_Down1       tlfx, tlfy,_1_3zp1,          _1_3x,_1_3y, _2_3z   9                            //  _1_3zp1, _2_3z
#define North_Middle_Down1   _1_3xp1, tlfy, _1_3zp1,       _2_3x,_1_3y ,_2_3z  10
#define North_East_Down1      _2_3xp1, tlfy, _1_3zp1,       brbx,_1_3y ,_2_3z  11
#define Equator_West_Down1    tlfx, _1_3yp1, _1_3zp1,        _1_3x,_2_3y ,_2_3z  12
#define Equator_Middle_Down1    _1_3xp1, _1_3yp1, _1_3zp1,       _2_3x,_2_3y ,_2_3z  13
#define Equator_East_Down1      _2_3xp1, _1_3yp1,_1_3zp1,       brbx,_2_3y ,_2_3z  14
#define South_West_Down1       tlfx, _2_3yp1, _1_3zp1,        _1_3x,brby ,_2_3z  15
#define South_Middle_Down1     _1_3xp1, _2_3yp1, _1_3zp1,        _2_3x,brby ,_2_3z  16
#define South_East_Down1      _2_3xp1, _2_3yp1, _1_3zp1,        brbx,brby ,_2_3z  17


#define North_West_Down2        tlfx, tlfy,_2_3zp1,          _1_3x,_1_3y, brbz   18                                   //    _2_3zp1, ,brbz
#define North_Middle_Down2     _1_3xp1, tlfy, _2_3zp1,       _2_3x,_1_3y ,brbz  19
#define North_East_Down2      _2_3xp1, tlfy, _2_3zp1,       brbx,_1_3y ,brbz  20
#define Equator_West_Down2     tlfx, _1_3yp1, _2_3zp1,        _1_3x,_2_3y ,brbz  21
#define Equator_Middle_Down2     _1_3xp1, _1_3yp1, _2_3zp1,       _2_3x,_2_3y ,brbz  22
#define Equator_East_Down2      _2_3xp1, _1_3yp1,_2_3zp1,       brbx,_2_3y ,brbz  23
#define South_West_Down2        tlfx, _2_3yp1, _2_3zp1,        _1_3x,brby ,brbz  24
#define South_Middle_Down2     _1_3xp1, _2_3yp1, _2_3zp1,        _2_3x,brby ,brbz  25
#define South_East_Down2        _2_3xp1, _2_3yp1, _2_3zp1,        brbx,brby ,brbz  26


// Structure of a point
struct Point {
	int x;
	int y;
	int z;
	Point()
		: x(-1), y(-1), z(-1)
	{
	}

	Point(int a, int b, int c)
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
	Point *topLeftFront, *bottomRightBack;
	vector<Octree*> children;

public:
	// Constructor
	Octree()
	{
		// To declare empty node
		point = new Point();
	}

	// Constructor with three arguments
	Octree(int x, int y, int z)
	{
		// To declare point node
		point = new Point(x, y, z);
	}

	// Constructor with six arguments
	Octree(int x1, int y1, int z1, int x2, int y2, int z2)
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
		topLeftFront
			= new Point(x1, y1, z1);
		bottomRightBack
			= new Point(x2, y2, z2);

		// Assigning null to the children
		children.assign(8, nullptr);
		for (int i = TopLeftFront;
			i <= BottomLeftBack;
			++i)
			children[i] = new Octree();
	}

	// Function to insert a point in the octree
	void insert(int x,                                                         ///////////////////////////////////////////////////
				int y,
				int z)
	{ int _2_3p1;

		// If the point already exists in the octree
		if (find(x, y, z)) {
			cout << "Point already exist in the tree" << endl;
			return;
		}

		// If the point is out of bounds
		if (x < topLeftFront->x
			|| x > bottomRightBack->x
			|| y < topLeftFront->y
			|| y > bottomRightBack->y
			|| z < topLeftFront->z
			|| z > bottomRightBack->z) {
			cout << "Point is out of bound" << endl;
			return;
		}

		// Binary search to insert the point
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

		// Checking the octant of 
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

		// If an internal node is encountered
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
			children[pos]->insert(x_, y_, z_);
			children[pos]->insert(x, y, z);
		}
	}

	// Function that returns true if the point
	// (x, y, z) exists in the octree                      ///////////////////////////////////////////////////
	bool find(int x, int y, int z)
	{
		// If point is out of bound
		if (x < topLeftFront->x
			|| x > bottomRightBack->x
			|| y < topLeftFront->y
			|| y > bottomRightBack->y
			|| z < topLeftFront->z
			|| z > bottomRightBack->z)
			return 0;

		// Otherwise perform binary search
		// for each ordinate
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

		// Deciding the position
		// where to move
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

		// If an internal node is encountered
		if (children[pos]->point == nullptr) {
			return children[pos]->find(x, y, z);
		}

		// If an empty node is encountered
		else if (children[pos]->point->x == -1) {
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
	Octree tree(1, 1, 1, 5, 5, 5);

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
