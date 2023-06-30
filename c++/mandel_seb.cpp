#include <iostream>
#include <fstream>

const int NX = 6000;
const int NY = 6000;
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
void create_mandelbrot(int img[NX][NY])
{
    // setting boundaries
    float minx = -2;
    float maxx = 2;
    float nx = NX;
    float miny = -2;
    float maxy = 2;
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
            img[i][j] = julia(x, y,  -0.5251993,  -0.5251993);
    
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
    create_mandelbrot(img);
    std::cout << "Savin\n";
    dump_img(img);
}

// int main(int argc, char* argv[])
// {
//     for(int j = 0; j < min; j++)
//         {
//         // get the data for the ticker
//         vector<float>  = (tickers[i]);
//         // divergence array will use all of the data that is available in both ETFs
//         min < ticker_data.size() ? min : ticker_data.size();

//         // calculate divergence and fill up some plotting arrays
//         float* divergence = new float[min];
//         vector<int> fillx, filly1, filly2, zero;
//         for(int j = 0; j < min; j++)
//         {
//         plt::plot(x, {{"x axes", tickers[i]}});
//         plt::plot(y, {{"y axes", tickers[i]}});     // plot SPY
//         plt::plot(array_to_vector(divergence, min), {{"label", "Divergence"}}); // plot the divergence line
//         plt::axhline(0, 0, 1, {{"color", "black"}});        //  draw the line at y = 0

//         plt::xlabel("Days");
//         plt::ylabel("Price");
//         plt::show();
//         delete divergence;  // don't leak memory
// }
// plt.savefig("mandelbrot_python.svg")
// plt.show()
//     free(img);
//     return 0;
// }