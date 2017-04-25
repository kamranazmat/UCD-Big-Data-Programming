#!/usr/bin/python
# Kamran Azmat

import datetime
import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

times_passenger_count = {}
times_trip_count = {}

for line in reader:
    if len(line) != 1:
        continue
    data = line[0].strip().split(",")
    try:
        pick_up_time = datetime.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")
        day = pick_up_time.strftime("%A")
        if day in weekdays:
            cur_time = pick_up_time.strftime("%-I") + pick_up_time.strftime("%p")
            if cur_time not in times_passenger_count:
                times_passenger_count[cur_time] = int(data[3])
                times_trip_count[cur_time] = 1
            else:
                times_passenger_count[cur_time] += int(data[3])
                times_trip_count[cur_time] += 1
    except:
        continue

for time in times_passenger_count:
    print "{0}\t{1}\t{2}".format(time, times_passenger_count[time], times_trip_count[time])
