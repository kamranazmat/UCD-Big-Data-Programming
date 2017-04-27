#!/usr/bin/python
# Kamran Azmat

import datetime
import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for line in reader:
    data = line[0].strip().split(",")
    try:
        pick_up_time = datetime.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")
        day = pick_up_time.strftime("%A")
        if day not in weekdays:
            print "{0}{1}\t{2}".format(pick_up_time.strftime("%-I"), pick_up_time.strftime("%p"), data[3])
    except:
        continue
