#Exercise 17: More Files
from sys import argv
from os.path import exists

script, ffile, tfile = argv

print "Coppying from %s to %s" %(ffile,tfile)

# we could do this two on one line, how ?

in_file = open(ffile)
indata = in_file.read()

print "The input file is %d bytes long" %len(indata)

print "Does the output file exist? %r " %exists(tfile)
print "Ready, hit RETURN to continue, CTRL+c to abort."
raw_input("ok?")

out_file = open(tfile, 'w')
out_file.write(indata)

print "Alright, all done."
out_file.close()
in_file.close()

