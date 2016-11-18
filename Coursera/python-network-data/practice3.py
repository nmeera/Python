#Using re.search() like startswith()
import re
hand  = open('mbox-short.txt')

for line in hand:
	line = line.strip()
	if line.startswith('From: '):
#	if re.search('^From: ', line): # we can use re.search() like this insted of startswith()
		print line
