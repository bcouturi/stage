#include <iostream>

int main(int argc, char* argv[]) {

    int counter = 10;
    if (argc > 2) {
        counter = atoi(argv[2]);
        std::cout << "Counter is " << counter << std::endl;
    }

    if (argc > 1) {
    
        for (int i=0; i<counter; i++) {
            std::cout << " Hello " << argv[1] << " !!!!!" << std::endl;
        }
    }

    
    return 0
}