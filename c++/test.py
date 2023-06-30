


# # create function
# def mandel(cr, ci):
#     zr = 0
#     zi = 0
#     # repeat 100*
#     for n in range(1, 100):
#         nzr = zr**2 - zi**2 + cr
#         nzi = 2 * zr * zi + ci
#         if nzr**2 + nzi**2 > 4:
#             return n
#         zr = nzr
#         zi = nzi
#     # if we standed 100 rounds, return -2
#     return -2


# # setting boundaries
# minx = -0.7
# maxx = -0.7025
# nx = 600
# miny = 0.35
# maxy = 0.3525
# ny = 600

# # use the equation
# dx = (maxx - minx) / nx
# dy = (maxy - miny) / ny
# create function
# def mandel(cr, ci):
#     zr = 0
#     zi = 0
#     # repeat 100*
#     for n in range(1, 100):
#         nzr = zr**2 - zi**2 + cr
#         nzi = 2 * zr * zi + ci
#         if nzr**2 + nzi**2 > 4:
#             return n
#         zr = nzr
#         zi = nzi
#     # if we standed 100 rounds, return -2
#     return -2


# # setting boundaries
# minx = -0.7
# maxx = -0.7025
# nx = 600
# miny = 0.35
# maxy = 0.3525
# ny = 600

# # use the equation
# dx = (maxx - minx) / nx
# dy = (maxy - miny) / ny

# # img,repeat forever
# img = []
# for iy in range(ny):
#     line = []
#     y = miny + iy * dy
#     # calculate new y
#     for ix in range(nx):
#         # new x
#         x = minx + ix * dx
#         # graph
#         line.append(mandel(x, y))
#     img.append(line)


# # plotting the graph
# plt.imshow(
#     img,
#     cmap=plt.cm.get_cmap("GnBu"),
#     interpolation="none",
#     # delimitating
#     extent=(minx, maxx, miny, maxy),
# )
# plt.savefig("mandelbrot_python.svg")
# plt.show()
# import matplotlib.pyplot as plt

# for iy in range(ny):
#     line = []
#     y = miny + iy * dy
#     # calculate new y
#     for ix in range(nx):
#         # new x
#         x = minx + ix * dx
#         # graph
#         line.append(mandel(x, y))
#     img.append(line)


# # plotting the graph
# plt.imshow(
#     img,
#     cmap=plt.cm.get_cmap("GnBu"),
#     interpolation="none",
#     # delimitating
#     extent=(minx, maxx, miny, maxy),
# )
# plt.savefig("mandelbrot_python.svg")
# plt.show()
# import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import json

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
minx = -0.7
maxx = -0.7025
nx = 60#0
miny = 0.35
maxy = 0.3525
ny = 60#0

# use the equation
dx = (maxx - minx) / nx
dy = (maxy - miny) / ny

# img,repeat forever
img = []
for iy in range(ny):
    line = []
    y = miny + iy * dy
    # calculate new y
    for ix in range(nx):
        # new x
        x = minx + ix * dx
        # graph
        line.append(mandel(x, y))
    img.append(line)


with open("out.json", "w") as f:
    json.dump(img, f)

# plotting the graph
plt.imshow(
    img,
    cmap=plt.cm.get_cmap("GnBu"),
    interpolation="none",
    # delimitating
    extent=(minx, maxx, miny, maxy),
)
plt.savefig("mandelbrot_python.svg")
plt.show()