in_file=open('presidents.txt', 'r')
out_file=open('output.txt', 'w')

president=[]

for line in in_file:
    wordlist= line.split(",")
    president.append(wordlist[0])
    president.append(wordlist[2])

print (president)