#include "Sim_Par.h"
#include <iostream>

using namespace std;

Sim_Par::Sim_Par(double E, double px, double py, double pz) : Track(E,px,py,pz) {}
Sim_Par::~Sim_Par(){}

void Sim_Par::setParID(double ID){
    ParticleID = ID;
}

void Sim_Par::setParent(double ID){
    ParentID = ID;
}

void Sim_Par::Info(){
    cout << "The ID of the particle is " << ParticleID << endl;
    cout << "The ID of the parents particle is " << ParentID << endl;
}
