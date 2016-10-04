#Exercise 15: Reading Files

from sys import argv
script, filename = argv

txt = open(filename)

print "\nHere's your file %r: "%filename
print txt.read()

print "Type The file name again"
newfile = raw_input('newfilename:' )
txt_again = open(newfile)

print txt_again.read()

