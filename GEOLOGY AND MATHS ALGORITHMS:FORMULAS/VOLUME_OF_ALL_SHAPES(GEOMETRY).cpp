#include <iostream>
using namespace std;
#include <cmath>
#define PI 3.14159265359

void Cube(int length)
{ 
cout<<"Volume of Cube is:"<<pow(length,3);
cout<<endl;
}
void Cuboid(int length, int width, int height )
{ 
cout<<"Volume of Cuboid is:"<<length * width * height ;
cout<<endl;
}
void Parallelepiped(int length, int width, int height )
{ 
cout<<"Volume of Parallelepiped is:"<<length * width * height ;
cout<<endl;
}
void Pyramid(int length, int width, int height )
{ 
cout<<"Volume of Pyramid is:"<<(length * width * height)/3;
cout<<endl;
}
void Frustrum_of_a_Pyramid(int length, int width, int height )
{ 
cout<<"Volume of Frustrum_of_a_Pyramid is:"<<(height * ( ((length * width) * (length * width)) + sqrt((length * width) * (length * width)) ) )/3;
cout<<endl;
}
void Cylinder(int diameter, int height )
{ 
cout<<"Volume of Cylinder is:"<<(PI*pow(diameter,2)*height)/4;
cout<<endl;
}
void Hollow_Cylinder(int Diameter, int diameter, int height )
{ 
cout<<"Volume of Hollow_Cylinder is:"<<(PI*(pow(Diameter,2)-pow(diameter,2)))/4;
cout<<endl;
}
void Cone(int radius, int height )
{ 
cout<<"Volume of Cone is:"<<(PI*pow(radius,2)*height)/3;
cout<<endl;
}
void Frustrum_of_a_Cone(int Diameter, int diameter,int height )
{ 
cout<<"Volume of Frustrum_of_a_Cone is:"<<( PI*height* ( pow(Diameter,2)+ (Diameter*diameter) + pow(diameter,2) ))/12;
cout<<endl;
}
void Sphere(int radius)
{ 
cout<<"Volume of Sphere is:"<<(3*PI*pow(radius,3))/3;
cout<<endl;
}
void Zone_of_Sphere(int radius, int Radius, int height )
{ 
cout<<"Volume of Zone_of_Sphere is:"<<(  PI*height* ( (3*pow(radius,2)) + (3*pow(Radius,2)) + pow(height,2) ) )/6;
cout<<endl;
}
void Segment_of_Sphere(int Diameter, int height )
{ 
cout<<"Volume of Segment_of_Sphere is:"<<  PI*height* ( ((3/4) * pow(Diameter,2)) + pow(height,2) ) / 6;
cout<<endl;
}
void Sector_of_a_Sphere(int radius, int height )
{ 
cout<<"Volume of Sector_of_a_Sphere is:"<<(2*PI*pow(radius,2)*height) /3;
cout<<endl;
}
void Sphere_with_Cylinder(int height )
{ 
cout<<"Volume of Sphere_with_Cylinder is:"<<( PI*pow(height,3) ) /6;
cout<<endl;
}
void Sphere_with_two_Cones(int height, int radius )
{ 
cout<<"Volume of Sphere_with_two_Cones is:"<<(2 *PI* pow(radius,2) * height) /3;
cout<<endl;
}
void Sliced_Cylinder(int diameter, int height )
{ 
cout<<"Volume of Sliced_Cylinder is:"<<(PI* pow(diameter,2) * height) /4;
cout<<endl;
}
void Ungula(int radius, int height )
{ 
cout<<"Volume of Ungula is:"<<(2* pow(radius,2) * height) /3;
cout<<endl;
}
void Barrel(int Diameter,int diameter, int height )
{ 
cout<<"Volume of Barrel is:"<<PI *height *( (2*pow(Diameter,2)) + pow(diameter,2) ) /12;
cout<<endl;
}
int main() {
 int length=4;
 int width=3;
 int height=5;
 int diameter=6;
 int Diameter=7; //Hollow_Cylinder
 int radius= 5;
 int Radius= 7;
 Cube(length);
 Cuboid(length, width, height);
 Parallelepiped(length, width, height );
 Pyramid(length, width, height );
 Frustrum_of_a_Pyramid(length, width, height );
 Cylinder(diameter,  height );
 Hollow_Cylinder( Diameter, diameter, height );
 Cone( radius, height );
 Frustrum_of_a_Cone( Diameter,  diameter, height );
 Sphere( radius);
 Zone_of_Sphere( radius,  Radius, height );
 Segment_of_Sphere( Diameter,  height );
 Sector_of_a_Sphere(radius, height );
 Sphere_with_Cylinder(height );
 Sphere_with_two_Cones( height, radius );
 Sliced_Cylinder( diameter,height );
 Ungula(radius, height );
 Barrel(Diameter, diameter, height );
    return 0;
}