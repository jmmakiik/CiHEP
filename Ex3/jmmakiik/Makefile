OBJS = Prob12.o
OPT = -O -Wall -fPIC -D_REENTRANT
INC = -I.
LIBS = -L. -lProb12

all:
	@$(MAKE) compile; $(MAKE) libProb12.so
	$(CXX) Test.cpp $(INC) $(LIBS) -o Testexe

compile: $(OBJS)

libProb12.so: $(OBJS)
	$(CXX) -shared -O $(OBJS) -o libProb12.so
	
.cc.o:
	$(CXX) $(OPT) $(INC) -c $*.cc

.cpp.o:
	$(CXX) $(OPT) $(INC) -c $*.cpp

Test: Test.o
	$(CXX) $(LIBS) -O Test.o -o Test

clean:
	rm *.o *.so ./Testexe
