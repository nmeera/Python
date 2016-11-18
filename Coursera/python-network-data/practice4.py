# Use X-P4Text.txt as input file  :)
file =  raw_input("Enter the File Name: ")
fh = open(file)
for ln in fh:
	print ln.strip()
