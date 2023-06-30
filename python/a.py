
pos1 = [11.190544128417969, -8.414779663085938, 770.0]
pos2 = [216.72702026367188, -99.75226593017578, 9193.1005859375]
# Compute slope in x and y with respect to z
dx =pos2[0] - pos1[0]
dy = pos2[1] - pos1[1]
dz =pos2[2] - pos1[2]
x = pos1[0]
y = pos1[1]
xslope = dx / dz
yslope = dy / dz

# extrapolate to z = 20000
newZ = 20000
newDz = newZ - pos1[2]
newDx = newDz * dx/dz
newDy = newDz * dy/dz
newX = x + newDx
newY = y + newDy

# Finally write a function doing all this, and returning a x,y,z tuple for the new point

def extrapolated_point(newZ, pos1, pos2):
    """ Extrapolate trajectory """
    # Compute vector in between the 2 reference points
    dx = pos2[0]- pos1[0]
    dy = pos2[1]- pos1[1]
    dz = pos2[2]- pos1[2]

    # Slope in x and y
    xslope = dx/ dz
    yslope = dy/ dz

    # finally extrapolate
    newDz = newZ - pos1[2]
    newDx = xslope* newDz
    newDy = yslope * newDz
    newX = pos1[0] +newDx
    newY = pos1[1] + newDy
    return (newX,newY,newZ)


#new point extrapolation for z=20000
p20000 = extrapolated_point(20000, pos1, pos2)
newX,newY,newZ  = p20000

points = [ pos1, pos2, p20000]
for v in [ 2000, 5000, 10000, 15000]:
    points.append(extrapolated_point(v, pos1, pos2))



import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for p in points:
    ax.scatter(p[0], p[1], p[2], marker='.')


# x = [newX]
# y = [newY]
# plt.plot
plt.show()
