import matplotlib.pyplot as plt


# create function
def mandel(cr, ci):
    zr = 0
    zi = 0
    # repeat 100*
    for n in range(1, 100):
        nzr = zr**2 - zi**2 + cr
        nzi = 2 * zr * zi + ci
        if nzr**2 + nzi**2 > 4:
            return n
        zr = nzr
        zi = nzi
    # if we standed 100 rounds, return -2
    return -2


# setting boundaries
minx = -2
maxx = 0.5
nx = 40
miny = -1.0
maxy = 1.0
ny = 40

# compute steps in x and y
dx = (maxx - minx) / nx
dy = (maxy - miny) / ny

# fill img, with nx rows and ny cols
img = []
for iy in range(ny):
    # compute current y value
    y = miny + iy * dy
    line = []
    for ix in range(nx):
        # compute current y value
        x = minx + ix * dx
        # fill current value
        line.append(mandel(x, y))
    img.append(line)
plt.imshow(
    img,
    cmap=plt.cm.get_cmap("GnBu"),
    interpolation="none",
    extent=(minx, maxx, miny, maxy),
)
plt.savefig("mandelbrot_python.svg")
plt.show()
