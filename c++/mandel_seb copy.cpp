#include <iostream>
#include <fstream>

const int NX = 10;
const int NY = 10;


void dump_img(int img[NX][NY]) {

    std::fstream fs{"out.json"};
    fs << "[ ";
    for (int i=0; i<NX; i++) {

        if (i != 0) {
            fs << ", ";
        }
        fs << "[ ";
        for (int j=0; j<NY; j++) {
            fs << img[i][j];
            if (j < (NY - 1)) {
               fs << ", ";
            }
        } 
        fs << "] \n";
    }
    fs << " ] ";
    fs.close();

}



int main(int argc, char* argv[]) {

    auto img = new int[NX][NY];

    for (int i=0; i<NX; i++) {
        for (int j=0; j<NY; j++) {
            img[i][j] = i*j;
        }   
    }

    dump_img(img);

    delete img;
    return 0;
}