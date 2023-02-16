#ifndef SIMPAR_H
#define SIMPAR_H

#include "Recon_Track.h"

class Sim_Par : public Track{
    public:
        Sim_Par(double E, double px, double py, double pz);
        ~Sim_Par();

        void setParID(double ID);
        void setParent(double ID);
        void Info();

    private:
        double ParticleID;
        double ParentID;

};

#endif //SIMPAR_H
