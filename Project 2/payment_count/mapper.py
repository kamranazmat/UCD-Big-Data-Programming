#!/usr/bin/python
# Kamran Azmat

import sys
import csv

payment_types = {"1": "Credit card", "2": "Cash", "3": "No charge", "4": "Dispute", "5": "Unknown", "6": "Voided trip"}
reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    data = line[0].strip().split(",")
    try:
        print payment_types[data[9]]
    except:
        try:
            print payment_types[data[11]]
        except:
            continue
