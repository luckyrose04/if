input=open('presidents.txt', 'r')
output=open('output.txt', 'w')

president=[]

for line in input:
    wordlist= line.split(",")
    president.append(wordlist[0])
    president.append(wordlist[2])
    
print (president)