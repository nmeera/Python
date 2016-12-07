#Following Links in Python (link in link) 
import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')

#for tag in tags:
 #      #Look at the parts of tag
#	print 'TAG: ',tag
#	print 'URL: ',tag.get('href', None)
#	print 'Contents:', tag.contents[0]
#	print 'Attrs: ',tag.attrs
#	print "\n\n"
p = raw_input("Enter the position: ")
r = raw_input("How many time it should repate:  ") 
c = 0
for tag in tags:
	c = c + 1
	if c == int(r): break
	if c == int(p) :
		x = tag.get('href', None) #;print x
		y = tag.contents[0] #;print y
print x, y
