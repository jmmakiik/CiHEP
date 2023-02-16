OBJS = Recon_Track.o Sim_Par.o
OPT = -O -Wall -fPIC -D_REENTRANT
INC = -I.
LIBS = -L. -lRecon_Track -lSim_Par

all:
	@$(MAKE) --no-print-directory All

All:
	@$(MAKE) compile; $(MAKE) libRecon_Track.so; $(MAKE) libSim_Par.so
	$(CXX) main.cpp $(INC) $(LIBS) -o Testexe

compile: $(OBJS)

libRecon_Track.so: $(OBJS)
	$(CXX) -shared -O $(OBJS) -o libRecon_Track.so
	
libSim_Par.so: $(OBJS)
	$(CXX) -shared -O $(OBJS) -o libSim_Par.so
	
.cc.o:
	$(CXX) $(OPT) $(INC) -c $*.cc

.cpp.o:
	$(CXX) $(OPT) $(INC) -c $*.cpp

main: main.o
	$(CXX) $(LIBS) -O main.o -o main

clean:
	rm *.o *.so ./Testexe
