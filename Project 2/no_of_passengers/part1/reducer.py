#!/usr/bin/python
# Kamran Azmat

import sys

trip_count = 0
passenger_count = 0

for line in sys.stdin:
    thisKey = line.strip()
    passenger_count += int(thisKey)
    trip_count += 1

# print passenger_count, trip_count
print passenger_count/float(trip_count)
