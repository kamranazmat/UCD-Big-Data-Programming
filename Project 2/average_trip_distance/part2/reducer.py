#!/usr/bin/python
# Kamran Azmat

import sys

trip_distance = 0
oldKey = None

for line in sys.stdin:
    thisKey, val = line.strip().split("\t")
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", trip_distance
        oldKey = thisKey
        passengers_count = 0

    oldKey = thisKey
    trip_count += int(val)

if oldKey != None:
    print oldKey, "\t", trip_distance
