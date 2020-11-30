#include <iostream>
#include "large_package.h"

void large_package(){
    #ifdef NDEBUG
    std::cout << "large_package/1.4: Hello World Release!" <<std::endl;
    #else
    std::cout << "large_package/1.4: Hello World Debug!" <<std::endl;
    #endif
}
