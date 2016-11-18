# Usage of re.findall(), Wild-Card Characters 
# Use X-P4Text.txt as input file  :)
import re
file =  raw_input("Enter the File Name: ")
fh = open(file)
for ln in fh:
	ln = ln.strip()
#	print re.findall('^X.*:', ln)
# prints line which are starts with X, dot '.' is Wild-Card Characters here, '*' means all
	print re.findall('^X.\S+:', ln) # here \S means non-blank char(no space) 
