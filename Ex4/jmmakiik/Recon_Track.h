#ifndef TRACK_H
#define TRACK_H

#include "cmath"

class Track {
    public:
        Track();
        Track(double E, double px, double py, double pz);
        virtual ~Track();

        double energy(){return pre;}
        double px(){return prpx;}
        double py(){return prpy;}
        double pz(){return prpz;}

        double TransP();
        double PseudoRap();
        double Theta();

        void setexyz(double E, double x, double y, double z);

    private:
        double prpx;
        double prpy;
        double prpz;
        double pre;

};

#endif // TRACK_H
