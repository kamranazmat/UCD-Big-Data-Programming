#!/usr/bin/python
# Kamran Azmat

import sys

trip_distance = 0
trip_count = 0
oldKey = None

for line in sys.stdin:
    thisKey, val = line.strip().split("\t")
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", trip_distance/trip_count
        oldKey = thisKey
        trip_distance = 0
        trip_count = 0

    oldKey = thisKey
    trip_distance += float(val)
    trip_count += 1

if oldKey != None:
    print oldKey, "\t", trip_distance/trip_count
