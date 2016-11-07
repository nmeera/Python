#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour.

name = raw_input("Enter file: ")
fh = open(name,'r')
dct = dict()
lst = list()
for ln in fh:
	if ln.startswith('From '):
		ln = ln.split()  #spliting the string by space
		ln = ln[5].split(':') # here taking hours string/word from above line/split and splitting the string a second time using a colon.
		dct[ln[0]] = dct.get(ln[0],0) + 1

#t = dct.items()
for i,j  in sorted(dct.items()): # we can use sorted(t), as we assign dct.items() to variable 't'.
	print i,j

