#!/usr/bin/python
# Kamran Azmat

import sys

payment_count = 0
oldKey = None

for line in sys.stdin:
<<<<<<< HEAD
    thisKey, count = line.strip().split("\t")
=======
    thisKey = line.strip()
>>>>>>> 2d4f307931ea19869f02a805b243f126743d651f
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", payment_count
        oldKey = thisKey;
        payment_count = 0

    oldKey = thisKey
<<<<<<< HEAD
    payment_count += int(count)
=======
    payment_count += 1
>>>>>>> 2d4f307931ea19869f02a805b243f126743d651f

if oldKey != None:
    print oldKey, "\t", payment_count
