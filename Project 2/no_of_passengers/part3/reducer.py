#!/usr/bin/python
# Kamran Azmat

import sys

passenger_count = 0
trip_count = 0
oldKey = None

for line in sys.stdin:
    thisKey, val = line.strip().split("\t")
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", int(round(passenger_count/trip_count))
        oldKey = thisKey
        passenger_count = 0
        trip_count = 0

    oldKey = thisKey
    passenger_count += int(val)
    trip_count += 1

if oldKey != None:
    print oldKey, "\t", int(round(passenger_count/trip_count))
