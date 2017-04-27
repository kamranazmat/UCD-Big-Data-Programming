#!/usr/bin/python
# Kamran Azmat

import datetime
import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')

# average number of passengers per day of the week
# combiner
# months = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June": 0, "July": 0, "August": 0, "September": 0, "October": 0, "November": 0, "December": 0}

"""
months = OrderedDict()

month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for month in month_names:
    months[month] = 0
"""

for line in reader:
    if len(line) != 1:
        continue
    data = line[0].strip().split(",")
    try:
        pick_up_time = datetime.datetime.strptime(data[1], "%Y-%m-%d %H:%M:%S")
        print pick_up_time.strftime("%B"), "\t", data[3]
        # months[month] += int(data[3])
    except:
        continue

# for month in months:
#     print month, "\t", months[month]
