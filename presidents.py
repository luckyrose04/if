import csv

president = []

with open('presidents.txt') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        president.append(row[0])
        president.append(row[2])

print president
