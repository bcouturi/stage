
all: julia_seb

extendToCaloExercise: extendToCaloExercise.cpp
	g++ -std=c++17 -I /home/sponcec3/DEVEL/LHCb/BeatTest/ -o $@ $<

libmandel.so:mandel.cpp
	${CXX} -shared -O3 -Wall -std=c++14 -fPIC $< -o $@

clean:
	rm -rf *.o *~ *pyc *pyo *svg

clobber: clean
	rm -rf libmandel.so extendToCaloExercise

CPPFLAGS=-std=c++17 

julia_seb: julia_seb.cpp
	${CXX} ${CPPFLAGS} -o $@ $<