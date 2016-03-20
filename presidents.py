import csv

in_file = open('presidents.txt')
out_file = open('output.txt', 'w')

president = []

for line in in_file:
    wordlist = line.split(',')
    president.append(wordlist[0])
    president.append(wordlist[2])

print president

president = []

with open('presidents.txt') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		president.append(row[0])
		president.append(row[2])
