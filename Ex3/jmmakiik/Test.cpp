#include "Prob12.h"
#include <iostream>

using namespace std;

int main(){
    Space2D:Space2D vec;
    Space2D::ErrorMatrix ErrMat;

    double x = 2.0;
    double y = 3.0;
    double xx = 0.03;
    double xy = 0.05;
    double yx = 0.07;
    double yy = 0.09;

    vec.SetValues(x,y);
    vec.SetMatrixValues(xx,xy,yx,yy);
    cout << "The value of x is: " << vec.XValue() << endl;
    cout << "The value of y is: " << vec.YValue() << endl;
    cout << "Error Matrix is:" << endl;
    vec.ErrorValues();
    cout << "The distance r is:" << endl;
    cout << "r = " << vec.Distance() << endl;
    cout << "The error of the distance is:" << endl;
    cout << vec.DistError() << endl;
    cout << "The signifigance is:" << endl;
    cout << "S = " << vec.Signifigance() << endl;
    return 0;
}
