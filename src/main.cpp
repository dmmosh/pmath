#include "header.h"

/*
PMATH:
programming langugae in MATH!!


clang++ ./src/main.cpp ./src/utils.cpp -o pmath

clang++ ./src/main.cpp ./src/utils.cpp -o pmath && git-all ** ./pmath
*/


int main(int argc, char* argv[]){
    for (size_t i = 0; i < argc; i++)
    {
        std::cout << argv[i];
    }
    
    

    return 0;
}