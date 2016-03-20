in_file = open('presidents.txt')
out_file = open('output.txt', 'w')

president = []

for line in in_file:
    wordlist = line.split(',')
    president.append(wordlist[0])
    president.append(wordlist[2])

print president

import csv
with open('private.csv', 'rb)' as csvfile:
	f = csv.reader(csvfile, delimiter=',')
	for row in f:
		print ', ' .join(row)
