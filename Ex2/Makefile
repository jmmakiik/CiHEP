CC = g++
FILE = Prob1

all: $(FILE)

$(FILE): $(FILE).o
	${CC} -o $(FILE) $(FILE).o
	
$(FILE).o: $(FILE).cpp
	${CC} -c $(FILE).cpp
	
clean:
	rm *.o $(FILE)
