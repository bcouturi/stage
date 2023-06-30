#!/usr/bin/env python

import matplotlib.pyplot as plt
import json

with open("out.json", "r") as f:
    img = json.load(f)

# plotting the graph
plt.imshow(
    img,
    cmap=plt.cm.get_cmap("GnBu"),
    interpolation="none",
    # delimitating
    #extent=(minx, maxx, miny, maxy),
)
plt.show()