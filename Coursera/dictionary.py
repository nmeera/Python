#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter the File name: ")
fh = open(name)
dic = dict()
var = None
for line in fh:
	if line.startswith('From '):
		#line = line.strip()
		line = line.split()
		dic[line[1]] = dic.get(line[1],0) + 1

for key,val in  dic.items():
	if val >= var:
		var = val
		key1 = key
print key1,var 

