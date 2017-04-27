#!/usr/bin/python
# Kamran Azmat

import datetime
import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')

# average number of passengers in general
for line in reader:
    if len(line) != 1:
        continue
    data = line[0].strip().split(",")
    try:
        count = int(data[3])
        print count
    except:
        continue
