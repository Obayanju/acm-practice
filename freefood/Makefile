CXX := g++
CXXFLAGS := -std=c++11

all: main

main: main.cpp
		$(CXX) $(CXXFLAGS) -o $@ $^

Freefood.o: main.cpp
		$(CXX) $(CXXFLAGS) -c $<
clean:
	-rm -f main
	-rm -f *.o
