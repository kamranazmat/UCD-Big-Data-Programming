#!/usr/bin/python
# Kamran Azmat

import sys

passenger_count = 0
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
