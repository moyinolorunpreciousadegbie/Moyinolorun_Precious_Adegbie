#include <iostream> 
using namespace std;

void Molecular_wt_oxide(float Element_Atomic_wt[12] ) 
{
    cout<< Element_Atomic_wt[0]*2 + Element_Atomic_wt[1]<<" "<< "SiO2"<<endl;
    cout<< Element_Atomic_wt[0]*2 + Element_Atomic_wt[2]<< " "<< "TiO2"<<endl;
     cout<< Element_Atomic_wt[0]*3 + Element_Atomic_wt[3] * 2<< " "<< "Al2O3"<<endl;
    cout<< Element_Atomic_wt[0]*3 + Element_Atomic_wt[4] * 2 << " "<< "Fe2O3"<<endl;
      cout<< Element_Atomic_wt[0] + Element_Atomic_wt[5]<< " "<< "MnO"<<endl;
    cout<< Element_Atomic_wt[0] + Element_Atomic_wt[6]<< " "<< "MgO"<<endl;
    cout<< Element_Atomic_wt[0] + Element_Atomic_wt[7]<< " "<< "CaO"<<endl;
     cout<< Element_Atomic_wt[0] + Element_Atomic_wt[11] * 2<< " "<< "Na2O"<<endl;
    cout<< Element_Atomic_wt[0] + Element_Atomic_wt[8] * 2 << " "<< "K2O"<<endl;
    cout<< Element_Atomic_wt[0]*5 + Element_Atomic_wt[9] * 2 << " "<< "P2O5"<<endl;
     cout<< Element_Atomic_wt[0]*2 + Element_Atomic_wt[10]<< " "<< "CO2"<<endl;
}
     
int main() {
float Element_Atomic_wt[12]={ 16, 28.09, 47.9, 26.98, 55.85, 54.94, 24.31, 40.08, 39.1, 30.97, 12.01, 22.99};
                          //  O,   Si,    Ti,   Al,    Fe,     Mn,   Mg,    Ca, K,    P,      C,    Na.
    Molecular_wt_oxide(Element_Atomic_wt ) ;
    return 0;
}

