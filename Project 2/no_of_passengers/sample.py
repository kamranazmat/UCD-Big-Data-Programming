import sys
import csv

payment_types = {"1": "Credit card", "2": "Cash", "3": "No charge", "4": "Dispute", "5": "Unknown", "6": "Voided trip"}
reader = csv.reader(sys.stdin, delimiter='\t')

# mini-reducer
type_count = {"Credit card": 0, "Cash": 0, "No charge": 0, "Dispute": 0, "Unknown": 0, "Voided trip": 0}

for line in reader:
    data = line[0].strip().split(",")
    try:
        type_count[payment_types[data[9]]] += 1
    except:
        try:
            type_count[payment_types[data[11]]] += 1
        except:
            continue

print type_count
