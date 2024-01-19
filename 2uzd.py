import csv

with open('2uzd.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        print(row[2])

