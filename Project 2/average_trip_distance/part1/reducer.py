#!/usr/bin/python
# Kamran Azmat

import sys

trip_count = 0
trip_distance = 0

for line in sys.stdin:
    thisKey = line.strip()
    trip_distance += float(thisKey)
    trip_count += 1

print trip_distance//trip_count
