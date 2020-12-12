#include "utils.h"



////////////////////////////////////////////////////////////////////////////////
// FUNCTIONS



// Init random generator
void initRandomGenerator(int seed) {
	if (seed == 0) {
		srand(time(NULL));
	} else {
		srand(seed);
	}
}



// Get random integer in interval [min ; max]
int getRandom(int min, int max) {
	return rand()%(max-min+1) + min;
}



// Number to string
string toString(int nb) {
	std::ostringstream ss;
  ss << nb;
  return ss.str();
}
string toString(double nb) {
	std::ostringstream ss;
  ss << nb;
  return ss.str();
}
string toString(bool nb) {
	std::ostringstream ss;
  ss << nb;
  return ss.str();
}
