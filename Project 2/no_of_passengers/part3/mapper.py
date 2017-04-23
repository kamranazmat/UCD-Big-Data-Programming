#!/usr/bin/python
# Kamran Azmat

import datetime
import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')

# average number of passengers per month

for line in reader:
    data = line[0].strip().split(",")
    try:
        pick_up_time = datetime.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")
        print pick_up_time.strftime("%A"), "\t", data[3]
    except:
        continue
