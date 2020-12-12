#ifndef _UTILS_H
#define _UTILS_H



////////////////////////////////////////////////////////////////////////////////
// HEAD
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <string>
#include <time.h>
#include <math.h>
#include <unistd.h>
using namespace std;



////////////////////////////////////////////////////////////////////////////////
// PROTOTYPES

//// Random numbers ////
// Init random generator
void initRandomGenerator(int seed=0);

// Get random integer in interval [min ; max]
int getRandom(int min=0, int max=100);



//// Conversions ////
// Number to string
string toString(int nb);
string toString(double nb);
string toString(bool nb);




#endif
