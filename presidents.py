import csv

presidents = []

with open('presidents.txt') as csvfile:
    reader = csv.reader(csvfile)
    for president, _, party in reader:
        presidents.append(president)
        presidents.append(party)

print presidents

with open('output.txt', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for row in presidents:
        writer.writerow(row)
    writer.writerow(['president', 'party'])
