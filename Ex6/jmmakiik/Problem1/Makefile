OPT=-c -g -Wall `root-config --cflags`

LIBS=`root-config --glibs`

all: writing reading

writing: writing.cxx
	$(CXX) $(OPT) -o writing.o writing.cxx
	$(CXX) -o writing writing.o $(LIBS)

reading: reading.cxx
	$(CXX) $(OPT) -o reading.o reading.cxx
	$(CXX) -o reading reading.o $(LIBS)

clean:
	rm -f ./*~ ./*.o ./writing ./reading *.png *.C *.root
