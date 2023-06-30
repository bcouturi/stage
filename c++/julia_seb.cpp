#include <iostream>
#include <fstream>

const int NX = 10000;
const int NY = 10000;
const int MAX_ITERATIONS = 100;

void dump_img(int img[NX][NY])
{

    std::ofstream fs{"out.json"};
    fs << "[ ";
    for (int i = 0; i < NX; i++)
    {

        if (i != 0)
        {
            fs << ", ";
        }
        fs << "[ ";
        for (int j = 0; j < NY; j++)
        {
            fs << img[i][j];
            if (j < (NY - 1))
            {
                fs << ", ";
            }
        }
        fs << "] \n";
    }
    fs << " ] ";
    fs.close();
}
int julia(float zr, float zi, float cr, float ci)
{

    for (int i = 0; i < MAX_ITERATIONS; i++)
    {
        float nzr = zr * zr - zi * zi + cr;
        float nzi = 2 * zr * zi + ci;

        if ((nzr * nzr + nzi * nzi) > 4)
        {
            return i;
        }
        zr = nzr;
        zi = nzi;
    }
    return MAX_ITERATIONS;
}


// Iterate with the mandelbrot equation to see if we diverge
// Returns 0 if we do, -2 otherwise
int mandel(float cr, float ci)
{

    // Real and imaginary parts of out complex number
    float zr = 0;
    float zi = 0;

    for (int i = 0; i < MAX_ITERATIONS; i++)
    {
        float nzr = zr * zr - zi * zi + cr;
        float nzi = 2 * zr * zi + ci;

        if ((nzr * nzr + nzi * nzi) > 4)
        {
            //std::cout << "We diverge\n";
            return 0;
        }
        zr = nzr;
        zi = nzi;
        //std::cout << zr << " " << zi << "\n";
    }
    return -2;
}

// create function
void create_fractal(int img[NX][NY])
{
    // setting boundaries
    float minx = -1.5;
    float maxx = 1.5;
    float nx = NX;
    float miny = -1.5;
    float maxy = 1.5;
    float ny = NY;

    // Compute variables for reference change
    float dx = (maxx - minx) / nx;
    float dy = (maxy - miny) / ny;

    // Iterate on all points to get their colour
    for (int i = 0; i < NX; i++)
    {
        for (int j = 0; j < NY; j++)
        {
            // Change coordinates from table index to x,y in the plane
            float x = minx + i * dx;
            float y = miny + j * dy;
            //img[i][j] = julia(x, y, -0.4, 0.6);
            img[i][j] = julia(x, y, -0.65, 0.371);
        }
    }
}

int main(int argc, char *argv[])
{

    auto img = new int[NX][NY];
    // for (int i=0; i<NX; i++) {
    //     for (int j=0; j<NY; j++) {
    //         img[i][j] = i*j;
    //     }
    // }
    create_fractal(img);
    std::cout << "Saving\n";
    dump_img(img);
}

