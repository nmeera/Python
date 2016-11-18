#Using find() 
hand =  open('mbox-short.txt')
for line in hand:
	line = line.strip()
	if line.find('From: ')>= 0:
	#	ln = line.find('From: ')
	#	print ln  # here 'ln' prints the position of search word i.e 'From: '
		print line
