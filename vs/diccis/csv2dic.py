import csv
with open('vs/diccis/names.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
