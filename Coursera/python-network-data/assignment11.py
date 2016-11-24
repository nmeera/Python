#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
# Use Python_to_AccessWebData_A.txt for this assignment
import re

file = raw_input("Enter file name: ")
fh = open(file, 'r')
sumn = 0
cnt = 0
for  ln in fh:
	ln = ln.strip() 
	if not re.findall('[0-9]+', ln): 
		continue
	x = re.findall('[0-9]+', ln)
	for i in x:
		sumn = sumn + int(i)
		cnt = cnt + 1


print "###Total numbers/values are = %d,  Sum of the them is =  %d### " %( cnt, sumn)
