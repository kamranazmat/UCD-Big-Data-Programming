#!/usr/bin/python
# Kamran Azmat

import datetime
import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')

# average number of passengers per day of week
# combiner
# days = {"Sunday": 0, "Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0}

for line in reader:
    if len(line) != 1:
        continue
    data = line[0].strip().split(",")
    try:
        pick_up_time = datetime.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")
        print pick_up_time.strftime("%A"), "\t", data[3]
    except:
        continue
