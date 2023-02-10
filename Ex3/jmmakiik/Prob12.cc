#include "Prob12.h"
#include "cmath"
#include <iostream>
using namespace std;

Space2D::Space2D(){}
Space2D::~Space2D(){}

double Space2D::XValue(){
    return valuex;
}

double Space2D::YValue(){
    return valuey;
}

void Space2D::SetValues(double x, double y){
    valuex = x;
    valuey = y;
}

void Space2D::SetMatrixValues(double xx, double xy, double yx, double yy){
    valuexx = xx;
    valuexy = xy;
    valueyx = yx;
    valueyy = yy;
}

void Space2D::ErrorValues(){
    cout << "(" << valuexx << " " << valuexy << ")" << endl;
    cout << "(" << valueyx << " " << valueyy << ")" << endl;
}

double Space2D::Distance(){
    return sqrt(pow(valuex,2)+pow(valuey,2));
}

double Space2D::DistError(){
    double error1 = valuexx * pow(valuex / Distance(), 2);
    double error2 = valuexy * pow(valuex*valuey / Distance(), 2);
    double error3 = valueyx * pow(valuex*valuey / Distance(), 2);
    double error4 = valueyy * pow(valuey / Distance(), 2);

    return sqrt(error1+error2+error3+error4);
}

double Space2D::Signifigance(){
    return Distance() / DistError();
}

