#include <iostream>
#include "Sim_Par.h"

using namespace std;

int main(){
    Sim_Par SomeTrack(3,5,6,-7);
    SomeTrack.setParent(12345);
    SomeTrack.setParID(2038);
    cout << "Transverse momentum (in (x,y)-plane) is " << SomeTrack.TransP() << endl;
    cout << "Pseudorapidity is " << SomeTrack.PseudoRap() << endl;
    cout << "Energy is " << SomeTrack.energy() << endl;
    cout << "Momentum in x-direction is " << SomeTrack.px() << endl;
    cout << "Momentum in y-direction is " << SomeTrack.py() << endl;
    cout << "Momentum in z-direction is " << SomeTrack.pz() << endl;
    cout << "The polar angle theta is " << SomeTrack.Theta() << endl;
    SomeTrack.Info();

}
