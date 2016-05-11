#Exercise 16: Reading and Writing Files

from sys import argv
script, filename = argv

print "We're going to erase %r: "%filename
print "If you don't want that, hit CTRL+C (^C)"
print "If you do want that, hit RETURN"

raw_input("?")
#####################################################
print "BEFORE WE WRITE INTO FILE\n"
openfile = open(filename)
print openfile.read()
#openfile.close()
#####################################################
print "Opening the file..."
target = open(filename, 'w')
print "\nNow I'm going to ask you for three lines."
line1 = raw_input("line1:" )
line2 = raw_input("line2:" )
line3 = raw_input("line3:" )

print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
#####################################################
print "AFTER WE WROTE TO FILE\n"
openfile = open(filename)
print openfile.read()
#####################################################
