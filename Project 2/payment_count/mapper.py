import sys
import csv

payment_types = {"1": "Credit card", "2": "Cash", "3": "No charge", "4": "Dispute", "5": "Unknown", "6": "Voided trip"}
reader = csv.reader(sys.stdin, delimiter='\t')
firstline = reader.next()

print firstline
payment_type_index = firstline[0].strip().split(",").index("payment_type")
print payment_type_index
for line in reader:
    data = line[0].strip().split(",")
    print payment_types[data[payment_type_index]]
