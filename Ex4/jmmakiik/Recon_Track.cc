#include "Recon_Track.h"
#include <iostream>
#include "cmath"

Track::Track(){}
Track::Track(double E, double px, double py, double pz){setexyz(E,px,py,pz);}
Track::~Track(){}

double Track::TransP(){
    return sqrt(pow(prpx,2)+pow(prpy,2));
}

double Track::Theta(){
    return acos(prpz/sqrt(pow(TransP(),2)+pow(pre,2)));
}

double Track::PseudoRap(){
    double Eta = -log(tan(Theta()/2));
    return (prpz > 0) ? Eta : -Eta;
}

void Track::setexyz(double E, double x, double y, double z){
    pre = E;
    prpx = x;
    prpy = y;
    prpz = z;
}
