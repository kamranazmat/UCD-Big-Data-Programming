#!/usr/bin/python
# Kamran Azmat

import sys

passenger_count = 0
<<<<<<< HEAD
oldKey = None

for line in sys.stdin:
    thisKey, no_passenger = line.strip().split("\t")
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", passenger_count
        oldKey = thisKey
        passengers_count = 0

    oldKey = thisKey
    passenger_count += int(no_passenger)

if oldKey != None:
    print oldKey, "\t", passenger_count
=======
trip_count = 0
oldKey = None

for line in sys.stdin:
    thisKey, no_passenger, count = line.strip().split("\t")
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", passenger_count/float(trip_count)
        oldKey = thisKey
        passenger_count = 0
        trip_count = 0

    oldKey = thisKey
    trip_count += int(count)
    passenger_count += int(no_passenger)

if oldKey != None:
    print oldKey, "\t", passenger_count/float(trip_count)
>>>>>>> 2d4f307931ea19869f02a805b243f126743d651f
