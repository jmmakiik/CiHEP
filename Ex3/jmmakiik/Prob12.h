#ifndef SPACE2D_H
#define SPACE2D_H

#include "cmath"

class Space2D {
    public:
        Space2D();
        ~Space2D();

        struct ErrorMatrix{
            double xx, xy, yx, yy;
        };

        void SetValues(double x, double y);
        void SetMatrixValues(double xx, double xy, double yx, double yy);

        double XValue();
        double YValue();
        void ErrorValues();
        double Distance();
        double DistError();
        double Signifigance();

    private:
        double valuex;
        double valuey;
        double valuexx;
        double valuexy;
        double valueyx;
        double valueyy;
};

#endif
