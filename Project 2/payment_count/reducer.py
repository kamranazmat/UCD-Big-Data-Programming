#!/usr/bin/python
# Kamran Azmat

import sys

payment_count = 0
oldKey = None

for line in sys.stdin:
    thisKey, count = line.strip().split("\t")
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", payment_count
        oldKey = thisKey;
        payment_count = 0

    oldKey = thisKey
    payment_count += int(count)

if oldKey != None:
    print oldKey, "\t", payment_count
