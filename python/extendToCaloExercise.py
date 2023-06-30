import json
import sys

# copy-paste your extrapolate function here
def extrapolate(pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    dz = pos2[2] - pos1[2]
    xslope = dx / dz
    yslope = dy / dz
    newZ = 100000
    newDz = newZ - pos1[2]
    newDx = xslope * newDz
    newDy = yslope * newDz
    newX = pos1[0] + newDx
    newY = pos1[1] + newDy
    return[newX,newY,newZ]


# reading the input data
with open("../data/LHCbEventDataV2.json") as f:
    data = json.load(f)

# loop over events in the file
for eventName in data:
    # first get the longtracks
    longTracks = data[eventName]["Tracks"]["LongTracks"]
    # loop over the tracks
    for track in longTracks:
        # extract list of positions for the track
        positions = track['pos']
        # extract positions of 2 last hits
        pos1 = positions[-2]
        pos2 = positions[-1]
        # call your extrapolation function
        newPos = extrapolate(pos1,pos2)
        # append new hit to positions
        print(f"Appending position {newPos}")
        positions.append(newPos)


# dump result to a new file
json.dump(data, open('data_pos_tracking.json', 'w'), indent= 2)
