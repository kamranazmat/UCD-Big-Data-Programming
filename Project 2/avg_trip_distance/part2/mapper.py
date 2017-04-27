#!/usr/bin/python
# Kamran Azmat

import datetime
import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    if len(line) != 1:
        continue
    data = line[0].strip().split(",")
    try:
        pick_up_time = datetime.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")
        print pick_up_time.strftime("%B"), "\t", flaot(data[4])
    except:
        continue